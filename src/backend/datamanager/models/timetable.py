from mongoengine import *


class TimeTable(Document):
    group = StringField(max_length=30)
    timetable = ListField(EmbeddedDocumentField(TimeTableDay))


class TimeTableDay(EmbeddedDocument):
    day_of_week = IntField(default=1)
    is_first_week = BooleanField()
    records = ListField(EmbeddedDocumentField(TimeTableRecord))


class TimeTableRecord(EmbeddedDocument):
    order_number = IntField(default=1)
    lesson_name = StringField(max_length=50)
