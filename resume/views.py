from django.shortcuts import render

# Create your views here.
from .models import Header,Education, Experience, TechnicalSkill, Project

def resume_view(request):
    header = Header.objects.first()
    education_list = Education.objects.all()
    experience_list = Experience.objects.all()
    skill_list = TechnicalSkill.objects.all()
    project_list = Project.objects.all()


    context = {
        'header': header,
        'education_list': education_list,
        'experience_list': experience_list,
        'skill_list': skill_list,
        'project_list':project_list,
    }
    return render(request, 'resume/resume.html', context)

