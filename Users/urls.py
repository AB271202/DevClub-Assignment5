from django.urls import path, include
from . import views
#We cannot just write import views as views is a generic name and python mat import some other module named views
urlpatterns = [
    #path('', views.index),
]