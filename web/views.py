from django.shortcuts import render
from web.models import category, work, experience, education
from web.mock_data import icons_contact, personal_info, skills

def index(request):

    #     personal_info=personal_info.PersonalInfo(),
    #     codeSkills=skills.MySkills.getCoding(),
    #     designSkills=skills.MySkills.getDesign(),
    #     education=education.Education.getAll(),
    #     experience=experience.Experience.getAll(),
    #     works=works.MyWorks.getAll(),
    #     worksCategory = works.MyWorks.categories(),
    #     icons=IconsContact,
    #     getmore=works.MyWorks.getMore()
    #     )

    context = {
        "personal_info":personal_info.PersonalInfo(),
        "codeSkills":skills.MySkills.getCoding(),
        "designSkills":skills.MySkills.getDesign(),
        'education': education.Education.objects.all(),
        'experience': experience.Experience.objects.all(),
        'works': work.Work.objects.all(),
        'worksCategory': category.Category.objects.all(),
    }
    return render(request, 'index.html', context=context)
