"""
Main game loop. Runs on Tuesday at 12am, pulls in picks, compiles results, writes to DB, and emails updated leaderboard to all players
@auth: Michael Wyda
"""
import datetime
from datetime import date


def pullInScores():
    pass


def gameLoop():
    dayOfWeek = datetime.date.weekday(date.today())
    if dayOfWeek is not 2:
        pullInScores()
    else:
        return
