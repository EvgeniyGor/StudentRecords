# -*- coding: utf-8 -*-

from django.shortcuts import render
from ..models.user_profile import UserProfile
from ..pdf_generator import render_to_pdf


def get_report(request):
    students = UserProfile.objects.filter(role='s')
    header = "List of the students. Список студентов."
    pdf = render_to_pdf('students-to-pdf.html', {
        'article': header,
        'students': students
    })

    if pdf:
        # TODO: Добавить относительный или автогенерирующийся путь
        pdf_file = open("/home/nick1/mygit/StudentRecords/studentrecords/static/reports/report.pdf", 'w').write(pdf)

    return render(request, 'report-download.html')
