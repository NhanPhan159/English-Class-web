from rest_framework import serializers
from api_class_detail.models import classDetail

class classDetailSerializer(serializers.ModelSerializer):
    class Meta :
        model = classDetail
        fields = '__all__'