from mongoengine import *


class Roles:
    def __init__(self):
        pass

    ADMIN = "admin"
    STUDENT = "student"
    TEACHER = "teacher"
    MONITOR = "monitor"


class User(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    patronymic = StringField(max_length=50)
    group = StringField(max_length=50)
    email = EmailField(max_length=100)
    github_id = StringField(max_length=100)
    stepic_id = StringField(max_length=50)
    role = StringField(max_length=30)
