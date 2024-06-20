import mlbgame
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#retrieve game data for a specific date
games = mlbgame.day(2023, 11, 1, home='Mets')

#extract relevant stats
winning_pitcher = games[0].w_pitcher
losing_pitcher = games[0].l_pitcher
hits = games[0].home_team_hits + games[0].away_team_hits
rbis = games[0].home_team_rbi + games[0].away_team_rbi
home_runs = games[0].home_team_home_runs + games[0].away_team_home_runs
errors = games[0].home_team_errors + games[0].away_team_errors
assists = games[0].home_team_assists + games[0].away_team_assists

#create a dataframe to store the data
data = {
    'Team': [games[0].w_team, games[0].l_team],
    'Winning Pitcher': [winning_pitcher, None],
    'Losing Pitcher': [None, losing_pitcher],
    'Hits': [hits, None],
    'RBIs': [rbis, None],
    'Home Runs': [home_runs, None],
    'Errors': [errors, None],
    'Assists': [assists, None]
}
df = pd.DataFrame(data)
print(df)

#create a bar plot using seaborn
plt.figure(figsize=(8, 6))
sns.barplot(x='Team', y='RBIs', data=df, palette='Set2')
plt.title('MLB Game Stats - RBIs')
plt.xlabel('Team')
plt.ylabel('RBIs')
plt.show()

#function to compare team performance over time
def compare_team_performance(team1, team2):
    team1_stats = []
    team2_stats = []

    for year in range(2023, 2024 + 1):
        #retrieve game data for both teams in the given year
        team1_games = mlbgame.day(year, home=team1) + mlbgame.day(year, away=team1)
        team2_games = mlbgame.day(year, home=team2) + mlbgame.day(year, away=team2)

        #calculate team-specific metrics (e.g., wins, runs scored, batting averages)
        team1_wins = sum(1 for game in team1_games if game.w_team == team1)
        team2_wins = sum(1 for game in team2_games if game.w_team == team2)
        team1_stats.append(team1_wins)
        team2_stats.append(team2_wins)

    return team1_stats, team2_stats

#example usage:
team1_name = 'Mets'
team2_name = 'Yankees'
team1_wins, team2_wins = compare_team_performance(team1_name, team2_name)
print(f"{team1_name} wins: {team1_wins}")
print(f"{team2_name} wins: {team2_wins}")