"""
Basic sql statements to be executed
"""


def create_users_table():
    return """ CREATE TABLE IF NOT EXISTS users (
                                        userID integer PRIMARY KEY,
                                        fname text NOT NULL,
                                        lname text NOT NULL,
                                        username text NOT NULL UNIQUE,
                                        hashedPass text NOT NULL,
                                        salt text NOT NULL,
                                        phoneNum text,
                                        email text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """


def create_group_table():
    return


def create_matchup_table():
    return


def create_leaderboard_table():
    return
