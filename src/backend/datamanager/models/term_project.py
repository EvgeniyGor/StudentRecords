from mongoengine import *
from user import User


class TermProject(Document):
    student = ReferenceField(User)
    projects = ListField(EmbeddedDocumentField(Project))


class Project(EmbeddedDocument):
    lesson_name = StringField(max_length=30)
    project_title = StringField(max_length=100)
    github_link = StringField(max_length=100)
