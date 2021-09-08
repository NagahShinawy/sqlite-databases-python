import sqlite3
from collections import namedtuple

Profile = namedtuple("Profile", ["username", "id", "email", "dob"])

connection = sqlite3.connect("students.sql")

profiles = connection.execute("SELECT * FROM profiles;")

for profile in profiles:
    prf = Profile(*profile)
    print(prf.id, prf.username, prf.dob, prf.email)


connection.close()