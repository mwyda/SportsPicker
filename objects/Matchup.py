class Matchup:

    def __init__(self, sportID, team1, team2, seasonYear, weekStart, weekEnd, weekNum, winner="", matchupID=-1):
        self.sportID = sportID
        self.team1 = team1
        self.team2 = team2
        self.seasonYear = seasonYear
        self.weekStart = weekStart
        self.weekEnd = weekEnd
        self.weekNum = weekNum
        self.winner = winner
        self.matchupID = matchupID

    def __str__(self):
        return f"Week {self.weekNum} matchup: {self.team1} at {self.team2}"