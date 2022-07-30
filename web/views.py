from urllib import response
from django.shortcuts import render
# from web.models import (
#     category, work, experience, education, skill,
#     personal_info, contact_icons
#     )
from web.mock_data import (
    education, icons_contact, works, experience, personal_info,
    skills
)


def index(request):

    # context = {
    #     "personal_info":personal_info.PersonalInfo.objects.first(),
    #     "codeSkills":skill.Skill.objects.filter(isCoding='True'),
    #     "designSkills":skill.Skill.objects.filter(isCoding='False'),
    #     'education': education.Education.objects.all(),
    #     'experience': experience.Experience.objects.all(),
    #     'works': work.Work.objects.all(),
    #     'worksCategory': category.Category.objects.all(),
    #     'first_row_icons': contact_icons.ContactIcons.objects.filter(first_row='True'),
    #     'second_row_icons': contact_icons.ContactIcons.objects.filter(first_row='False'),
    # }

    context = {
        "personal_info":personal_info.PersonalInfo(),
        "codeSkills":skills.coding,
        "designSkills":skills.design,
        'education': education.getAll,
        'experience': experience.getAll,
        'works': works.MyWorks.getAll(),
        'worksCategory': works.MyWorks.categories(),
        'first_row_icons': icons_contact.IconsContact.firstRow(),
        'second_row_icons': icons_contact.IconsContact.secondRow(),
    }

    return render(request, 'index.html', context=context)


def portfolio(request):
    
    context = {}
    return render(request, 'portfolio.html', context=context)

def not_found(request, exception):
    context = {
        "personal_info":personal_info.PersonalInfo.objects.first(),
    }
    return render(request, '404.html', context=context)

def server_error(request):
    return render(request, '500.html')