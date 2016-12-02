# coding=utf-8
from django.template.loader import get_template, Context
import cStringIO
import sx.pisa3 as pisa

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = cStringIO.StringIO()
    pdf = pisa.pisaDocument(cStringIO.StringIO(html.encode('utf-8')), result, show_error_as_pdf=True, encoding='UTF-8')
    if not pdf.err:
        return result.getvalue()
    return False


def generate_pdf(pdf_file_dist,students,header):
    pdfmetrics.registerFont(TTFont('TimesNewRoman', '/home/nick1/mygit/StudentRecords/studentrecords/TimesNewRoman.ttf'))
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='h_first', fontName='TimesNewRoman', fontSize=12, alignment=TA_CENTER,
                              leftIndent=2.32 * inch))

    styleN = styles['Normal']
    style_1 = styles['h_first']

    story = []
    #В данныи момент используется в целях проверки вывода
    header_hard_code = "Список студентов"
    story.append(Paragraph(header, style_1))
    story.append(Paragraph(header_hard_code, style_1))
    # В данныи момент используется в целях проверки, в дальнейшем информация должна передаватся параметрах
    #в готовом виде
    for student in students:
        story.append(Paragraph(add_row_for_student(student), styleN))

    #story.append(Paragraph(header, style_1))
    #story.append(Paragraph(article, styleN))
    doc = SimpleDocTemplate(pdf_file_dist, pagesize=letter)
    doc.build(story)


def generate_report(stud,head):
    # TODO: Добавить относительный или автогенерирующийся путь
    generate_pdf("/home/nick1/mygit/StudentRecords/studentrecords/static/reports/report.pdf",stud,head)
    return True


def add_row_for_student(student):
    memory = ""
    if student.first_name is not None:
        memory += student.first_name
    if student.last_name is not None:
        memory += student.last_name
    if student.patronymic is not None:
        memory += student.patronymic
    result = "ФИО".decode("utf-8")
    result += "_" * (memory.__len__() - result.__len__() + 3)
    memory += "_" * 3
    if student.study_group is not None:
        memory += student.study_group
    result += "Группа".decode("utf-8")
    result += "_" * (memory.__len__() - result.__len__() + 6)
    memory += "_" * 6
    if student.github_id is not None:
        memory += student.github_id
    result += "GitHub".decode("utf-8")
    result += "_" * (memory.__len__() - result.__len__() + 6)
    memory += "_" * 6
    if student.stepic_id is not None:
        memory += student.stepic_id
    result += "Stepic".decode("utf-8")
    result += "\n"
    result += memory.encode("utf-8")
    return result
