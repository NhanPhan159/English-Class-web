from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/v1/classes/', include("api_class.urls")),
    path('api/v1/classDetail/',include("api_class_detail.urls"))
]
