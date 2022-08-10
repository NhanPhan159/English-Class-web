from xml.etree.ElementInclude import include
from rest_framework import routers
from api_class_detail.views import ClassDetailModelViewSet
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'',ClassDetailModelViewSet)
urlpatterns = [
    path('',include(router.urls))
    ]
