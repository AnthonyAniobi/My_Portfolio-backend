from rest_framework import serializers
from web.models.experience import Experience

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields= '__all__'