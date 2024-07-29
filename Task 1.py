import requests
import pandas as pd

# API endpoint and headers
API_KEY = '84062074bf534c9f80fcac72eaad956d'
COMPETITION_ID = 'PL'  # Example: English Premier League
URL = f'http://api.football-data.org/v4/competitions/{COMPETITION_ID}/matches'
HEADERS = {'X-Auth-Token': API_KEY}

# Fetch data
response = requests.get(URL, headers=HEADERS)
matches = response.json()['matches']

# Convert to DataFrame for easier handling
matches_df = pd.DataFrame(matches)
# Initialize lists to store results
home_win_half_full = []

for match in matches:
    if match['score']['halfTime'] and match['score']['fullTime']:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        half_time_home = match['score']['halfTime']['home']
        half_time_away = match['score']['halfTime']['away']
        full_time_home = match['score']['fullTime']['home']
        full_time_away = match['score']['fullTime']['away']

        # Check for home team winning at half-time and full-time
        if half_time_home > half_time_away and full_time_home > full_time_away:
            home_win_half_full.append(home_team)

# Convert list to DataFrame
home_win_half_full_df = pd.DataFrame(home_win_half_full, columns=['Team'])

# Calculate metrics
home_win_count = home_win_half_full_df['Team'].value_counts()
home_win_percentage = home_win_count / matches_df['homeTeam'].value_counts() * 100

# Display results
print("Home Win Half-Time and Full-Time Count:")
print(home_win_count)
print("\nHome Win Half-Time and Full-Time Percentage:")
print(home_win_percentage)

