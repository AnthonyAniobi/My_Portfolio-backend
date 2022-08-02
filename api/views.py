from rest_framework import viewsets
from api.serializers import (
    category_serializer, contact_icon_serializer,
    education_serializer, experience_serializer, personal_info_serializer,
    skill_serializer, work_serializer,
)

from web.models import(
    category, contact_icons, education, experience, personal_info,
    skill, work,
)

class CategoriesView(viewsets.ModelViewSet):
    queryset= category.Category.objects.all()
    serializer_class = category_serializer.CategorySerializer

class ContactIconsView(viewsets.ModelViewSet):
    queryset= contact_icons.ContactIcons.objects.all()
    serializer_class = contact_icon_serializer.ContactIconsSerializer

class EducationView(viewsets.ModelViewSet):
    queryset= education.Education.objects.all()
    serializer_class = education_serializer.EducationSerializer

class ExperienceView(viewsets.ModelViewSet):
    queryset= experience.Experience.objects.all()
    serializer_class = experience_serializer.ExperienceSerializer

class PersonalInfoView(viewsets.ModelViewSet):
    queryset= personal_info.PersonalInfo.objects.all()
    serializer_class = personal_info_serializer.PersonalInfoSerializer

class SkillView(viewsets.ModelViewSet):
    queryset= skill.Skill.objects.all()
    serializer_class = skill_serializer.SkillSerializer

class WorkView(viewsets.ModelViewSet):
    queryset= work.Work.objects.all()
    serializer_class = work_serializer.WorkSerializer