from rest_framework import serializers
from web.models.work import Work

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Work
        fields= '__all__'