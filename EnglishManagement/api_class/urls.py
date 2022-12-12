from rest_framework import routers
from api_class.views import ClassModelViewSet
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r"",ClassModelViewSet)
urlpatterns = [
    path('',include(router.urls))
    ]
