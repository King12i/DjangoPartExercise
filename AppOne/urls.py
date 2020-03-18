from django.urls import path
from . import views

urlpatterns = [
    path('/showallthings', views.show_all),
    path('/duckbill', views.platypus),
    path('/duckbill/<whatsmyname>', views.beyonce),
    path('/green/hat', views.yellow_shoe),
    path('/dog/ear', views.pumpernickel),
    path('/telephone', views.ear)
]