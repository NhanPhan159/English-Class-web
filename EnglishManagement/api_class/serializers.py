from rest_framework import serializers
from api_class.models import Class

class classSerializer(serializers.ModelSerializer):
    class Meta :
        model = Class
        fields = '__all__'