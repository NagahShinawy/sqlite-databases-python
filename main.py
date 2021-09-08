import sqlite3
from collections import namedtuple


Profile = namedtuple("Profile", ["username", "id", "email", "dob"])

connection = sqlite3.connect("students.sql")

profiles = connection.execute("SELECT * FROM profiles;")

for profile in profiles:
    prf = Profile(*profile)
    print(prf.id, prf.username, prf.dob, prf.email)

# todo: take care about sql injection


# delete
connection.execute("DELETE FROM profiles WHERE id = 10")

# update
connection.execute("UPDATE profiles SET username='Jone Jose' WHERE id=5")
connection.commit()
connection.close()