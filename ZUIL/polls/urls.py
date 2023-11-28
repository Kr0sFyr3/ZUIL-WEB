from django.urls import path

from . import views
#from .views import execute_script

urlpatterns = [
    path("", views.home, name="home"),
    path("choise/", views.choiseScreen, name="choiseScreen"),
    path("scan/", views.scanScreen, name='scanScreen'),
    path("scanItem/", views.scanItemScreen, name="scanItemScreen"),
    path("return/", views.returnScreen, name="returnScreen"),
    #path('execute_script/', execute_script, name='execute_script'),
]