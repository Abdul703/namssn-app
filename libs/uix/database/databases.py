import sqlite3
from pprint import pprint


def all_courses():
    '''return list of all courses, each item is tuple of
       (code,title, unit, type)'''
    conn = sqlite3.connect('libs/uix/database/database')
    c = conn.cursor()

    c.execute("SELECT * FROM courses")
    l = c.fetchall()

    conn.close()

    return l


def courses_per_level_semester(level, semester):
    '''take level and semester number, eg ('1', '2') for
       100 level first semester and return list of all correspondents
       courses in form of (s/no., code, title, unit, type)'''
    all_course = all_courses()

    l = [list(line) for line in all_course if
         (line[0][-3] == level and
          line[0][-2] == semester)]
    k = [tuple([i+1]+line) for i, line in enumerate(l)]

    return k


def all_lecturers():
    '''return list of all lecturers as a tuple in form of
       (code(image-name), fullname, rank, phone-number)'''
    conn = sqlite3.connect('libs/uix/database/database')
    c = conn.cursor()

    c.execute("SELECT * FROM lecturers")
    l = c.fetchall()

    conn.close()

    return l


def all_excos():
    '''return list of all excos as a tuple in form of
       (code(image-name), fullname, rank, phone-number)'''
    conn = sqlite3.connect('libs/uix/database/database')
    c = conn.cursor()

    c.execute("SELECT * FROM excos")
    l = c.fetchall()

    conn.close()

    return l


def all_sras():
    '''return list of all SRAs as a tuple in form of
       (code(image-name), fullname, rank, phone-number)'''
    conn = sqlite3.connect('libs/uix/database/database')
    c = conn.cursor()

    c.execute("SELECT * FROM sras")
    l = c.fetchall()

    conn.close()

    return l
