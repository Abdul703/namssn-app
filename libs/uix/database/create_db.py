import sqlite3


conn = sqlite3.connect('database')
c = conn.cursor()

querry1 = """CREATE TABLE courses(
code TEXT NOT NULL,
title TEXT NOT NULL,
unit TEXT NOT NULL,
type TEXT NOT NULL
)
"""

querry2 = """CREATE TABLE lecturers(
code TETXT NOT NULL,
name TEXT NOT NULL,
rank TEXT NOT NULL,
phone TEXT NOT NULL
)"""

querry3 = """CREATE TABLE excos(
code TETXT NOT NULL,
name TEXT NOT NULL,
rank TEXT NOT NULL,
phone TEXT NOT NULL
)"""

querry4 = """CREATE TABLE sras(
code TETXT NOT NULL,
name TEXT NOT NULL,
rank TEXT NOT NULL,
phone TEXT NOT NULL
)"""

c.execute(querry1)
c.execute(querry2)
c.execute(querry3)
c.execute(querry4)

conn.commit()
conn.close()
