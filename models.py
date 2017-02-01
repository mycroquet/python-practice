import datetime

from peewee import *

DATABASE = SqliteDatabase('courses.sqlite')

class Course(Model):
    title = CharField()
    url = CharField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Course], safe=True)
    DATABASE.close()
