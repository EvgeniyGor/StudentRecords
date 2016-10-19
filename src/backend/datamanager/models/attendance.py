from mongoengine import *
from user import User


class Attendance(Document):
    student = ReferenceField(User)
    attendance_records = ListField(EmbeddedDocumentField(AttendanceRecord))


class AttendanceRecord(EmbeddedDocument):
    lesson_name = StringField(max_length=30)
    date = DateTimeField()

