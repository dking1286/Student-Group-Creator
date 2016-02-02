from datetime import datetime

from peewee import *

db = SqliteDatabase('student_group_data.db')

class BaseModel(Model):
    class Meta:
        database = db
        
class Student(BaseModel):
    first_name = CharField()
    last_name = CharField()
    
class Pairing(BaseModel):
    from_student = ForeignKeyField(
        rel_model=Student,
        related_name='pairings_from')
    to_student = ForeignKeyField(
        rel_model=Student,
        related_name='pairings_to')
    timestamp = DateTimeField(default=datetime.now)
    
def initialize():
    db.create_tables([Student, Pairing], safe=True)