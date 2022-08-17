from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import (
    CategorySerializer, ContactIconsSerializer,EducationSerializer,
    ExperienceSerializer, PersonalInfoSerializer,
    SkillSerializer, WorkSerializer,
)

from web.models import(
    category, contact_icons, education, experience, personal_info,
    skill, work,
)

class IndexView(APIView):
    def get(self, request):
        return Response({
            'Title': 'list of api calls',
            '--': '-----------------',
            'education': 'api endpoint for education list',
            'categories': 'api endpoint for work categories',
            'experience': 'api endpoint for exprience category',
            'personal_info': 'api endpoint for my personal information',
            'skill': 'api endpoint for my list of skills',
            'work': 'api endpoint for my works',
            'contact_icons': 'api endpoint for my contact icons',
        })

class CategoriesView(viewsets.ModelViewSet):
    queryset= category.Category.objects.all()
    serializer_class = CategorySerializer

class ContactIconsView(viewsets.ModelViewSet):
    queryset= contact_icons.ContactIcons.objects.all()
    serializer_class = ContactIconsSerializer

class EducationView(viewsets.ModelViewSet):
    queryset= education.Education.objects.all()
    serializer_class = EducationSerializer

class ExperienceView(viewsets.ModelViewSet):
    queryset= experience.Experience.objects.all()
    serializer_class = ExperienceSerializer

class PersonalInfoView(viewsets.ModelViewSet):
    queryset= personal_info.PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer

class SkillView(viewsets.ModelViewSet):
    queryset= skill.Skill.objects.all()
    serializer_class = SkillSerializer

class WorkView(viewsets.ModelViewSet):
    queryset= work.Work.objects.all()
    serializer_class = WorkSerializer