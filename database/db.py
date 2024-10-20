from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
import datetime

engine = create_engine('sqlite:///weather.db')
Base = declarative_base()

class WeatherSummary(Base):
    __tablename__ = 'weather_summaries'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    average_temp = Column(Float)
    max_temp = Column(Float)
    min_temp = Column(Float)
    dominant_weather = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def store_summary(summary_data):
    for index, row in summary_data.iterrows():
        summary = WeatherSummary(
            city=row['city'],
            average_temp=row[('temp', 'mean')],
            max_temp=row[('temp', 'max')],
            min_temp=row[('temp', 'min')],
            dominant_weather=row[('main', '<lambda>')]
        )
        session.add(summary)
    session.commit()
