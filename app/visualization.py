import matplotlib.pyplot as plt # type: ignore

def visualize_weather(df):
    df.plot(x='city', y=[('temp', 'mean'), ('temp', 'max'), ('temp', 'min')], kind='bar')
    plt.title('Daily Weather Summary')
    plt.show()
