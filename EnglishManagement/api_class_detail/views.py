from api_class_detail.models import classDetail
from api_class_detail.serializers import classDetailSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ClassDetailModelViewSet(viewsets.ModelViewSet):
    queryset = classDetail.objects.all()
    serializer_class = classDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['begin', 'end','session']
