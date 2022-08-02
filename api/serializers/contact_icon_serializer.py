from rest_framework import serializers
from web.models.contact_icons import ContactIcons

class ContactIconsSerializer(serializers.ModelSerializer):
    class Meta:
        model= ContactIcons
    fields='__all__'
