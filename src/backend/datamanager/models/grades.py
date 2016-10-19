from mongoengine import *
from user import User


class Grades(Document):
    student = ReferenceField(User)
    grades = ListField(EmbeddedDocumentField(Lesson))


class Lesson(EmbeddedDocument):
    name = StringField(max_length=50)
    labs = ListField(EmbeddedDocumentField(Lab))


class Lab(EmbeddedDocument):
    title = StringField(max_length=50)
    grade = DecimalField(min_value=0.0, max_value=100.0, precision=1)
