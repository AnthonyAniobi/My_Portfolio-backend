from rest_framework import serializers
from web.models import (
    category, contact_icons, education,
    experience, personal_info, skill, work,
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category.Category
        fields = '__all__'

class ContactIconsSerializer(serializers.ModelSerializer):
    class Meta:
        model= contact_icons.ContactIcons
        fields='__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=education.Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=experience.Experience
        fields = '__all__'

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=personal_info.PersonalInfo
        fields= '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=skill.Skill
        fields= '__all__'

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model=work.Work
        fields= '__all__'