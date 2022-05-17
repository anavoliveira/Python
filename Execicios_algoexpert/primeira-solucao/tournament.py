def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == 1 else awayTeam

        updateScores(winningTeam, 3, scores)
        
        if scores[winningTeam]> scores[currentBestTeam]:
            currentBestTeam = winningTeam

        return currentBestTeam

def updateScores(team, points, scores):
    if team not in scores:
        scores[team]=0

    scores[team] += points
    print(f'Score = {scores}')     

if __name__ == '__main__':
    print(tournamentWinner([
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]],
        [0, 0, 1]))
    # lst = ["HTML", "C#", "Python"]

    # lst = np.array(lst)

    # result = np.where(lst == lst[0])

    # print(result[0])