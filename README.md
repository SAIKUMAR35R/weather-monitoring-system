
```markdown
# Real-Time Data Processing System for Weather Monitoring

## Objective
Develop a real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates from the OpenWeatherMap API.

## Data Source
- Continuously retrieve weather data from the OpenWeatherMap API.
- Focus on parameters: 
  - `main`: Main weather condition (e.g., Rain, Snow, Clear)
  - `temp`: Current temperature in Celsius
  - `feels_like`: Perceived temperature in Celsius
  - `dt`: Time of the data update (Unix timestamp)

## Processing and Analysis
- Call the OpenWeatherMap API every 5 minutes to retrieve weather data for major metros in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
- Convert temperature values from Kelvin to Celsius.

## Rollups and Aggregates
1. **Daily Weather Summary**:
   - Calculate average, maximum, and minimum temperatures, and identify the dominant weather condition.
   - Store daily summaries in a database.

2. **Alerting Thresholds**:
   - User-configurable thresholds for temperature or specific conditions.
   - Trigger alerts for current weather conditions if thresholds are breached.

3. **Implement Visualizations**:
   - Display daily weather summaries, historical trends, and alerts.

## Test Cases
1. **System Setup**: Verify successful connection to OpenWeatherMap API using a valid API key.
2. **Data Retrieval**: Simulate API calls and ensure correct data retrieval.
3. **Temperature Conversion**: Test temperature conversion from Kelvin to Celsius.
4. **Daily Weather Summary**: Verify daily summary calculations for multiple days.
5. **Alerting Thresholds**: Configure thresholds and verify alerts when violated.

## Bonus Features
- Support additional weather parameters (e.g., humidity, wind speed).
- Explore weather forecasts retrieval and summary generation based on predicted conditions.

## Installation
1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd [repository-directory]
