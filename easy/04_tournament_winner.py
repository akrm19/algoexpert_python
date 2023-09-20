def tournamentWinner(competitions, results):
    # Write your code here.
    team_results = {}
    curr_max = 0
    current_winner = ""

    for idx, teams in enumerate(competitions):
        home_team = teams[0]
        away_team = teams[1]
        winner = home_team if results[idx] == 1 else away_team

        team_results[winner] = 3 if winner not in team_results.keys() else team_results[winner] + 3
        if team_results[winner] > curr_max:
            curr_max = team_results[winner]
            current_winner = winner

    return current_winner
