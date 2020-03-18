from django.urls import path
from . import views

urlpatterns = [
    path('/purple/banana', views.elephanttoe),
    path('/no', views.yes),
    path('/yellow/tomato', views.beansprout),
    path('/orange/yellow', views.fungus),
    path('/orange', views.octopus),
    path('/<int:numberofgreenhouses>/sharpies', views.rubberducky)
]