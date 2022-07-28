from django.shortcuts import render
from web.models import category, work, experience, education
from web.mock_data import icons_contact, personal_info, skills

def index(request):

    context = {
        "personal_info":personal_info.PersonalInfo(),
        "codeSkills":skills.MySkills.getCoding(),
        "designSkills":skills.MySkills.getDesign(),
        'education': education.Education.objects.all(),
        'experience': experience.Experience.objects.all(),
        'works': work.Work.objects.all(),
        'worksCategory': category.Category.objects.all(),
        'first_row_icons': icons_contact.firstRow,
        'second_row_icons': icons_contact.secondRow,
    }
    return render(request, 'index.html', context=context)


def portfolio(request):
    context = {}

    return render(request, 'portfolio.html', context=context)