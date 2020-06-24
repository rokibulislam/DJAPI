"""
 Create a Module "api" and create an empty file __init__.py in the persons app
 [simple create a folder named "api" and create "__init__.py" file containes nothing. It will help to detect this folder
 as a module by the system]
 Then create urls.py file here
 This is done because it's better to separate api's view logic from normal views as well as url patterns
"""
from django.conf.urls import url
from django.urls import path,re_path
from .views import (
    SingleApiView,
    ListAPIView
)

urlpatterns = [
    path('', ListAPIView.as_view()),
    re_path('(?P<id>\d+)/',SingleApiView.as_view()),
]