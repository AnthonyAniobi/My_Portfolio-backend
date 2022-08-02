from rest_framework import serializers
from web.models.skill import Skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields= '__all__'