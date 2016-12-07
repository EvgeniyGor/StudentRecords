# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models.term_project import TermProject


@login_required
def term_projects(request):
    projects = TermProject.objects.all()

    project_list = {}

    for project in projects:
        group = project.user.study_group
        if group not in project_list:
            project_list[group] = []

        project_list[group].append(project)

    return render(request, 'term-projects.html', {'projectlist': project_list})
