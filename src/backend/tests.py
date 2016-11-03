from django.test import TestCase
from django.test.client import Client

client = Client()


class GetPagesTests(TestCase):
    def get_index(self):
        response = client.get("/")

        expected = 200
        actual = response.status_code

        self.assertEqual(expected, actual)

    def get_students(self):
        response = client.get('/students')

        expected = 200
        actual = response.status_code

        self.assertEqual(expected, actual)

    def get_attendance(self):
        response = client.get('/attendance')

        expected = 200
        actual = response.status_code

        self.assertEqual(expected, actual)

    def get_grades(self):
        response = client.get('/grades')

        expected = 200
        actual = response.status_code

        self.assertEqual(expected, actual)

    def get_group_list(self):
        response = client.get('/group-list')

        expected = 200
        actual = response.status_code

        self.assertEqual(expected, actual)

    def get_timetable(self):
        response = client.get('/timetable')

        expected = 200
        actual = response.status_code

        self.assertEqual(expected, actual)

    def get_term_projects(self):
        response = client.get('/term-projects')

        expected = 200
        actual = response.status_code

        self.assertEqual(expected, actual)


class DataTests(TestCase):
    def get_students(self):
        pass

    def get_attendance(self):
        pass

    def get_grades(self):
        pass

    def get_group_list(self):
        pass

    def get_timetable(self):
        pass

    def get_term_projects(self):
        pass
