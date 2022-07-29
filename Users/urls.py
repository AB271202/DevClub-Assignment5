from django.urls import path, include
from . import views
#We cannot just write import views as views is a generic name and python mat import some other module named views
urlpatterns = [
    path('', views.index, name='Home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('completereg/', views.complete_reg, name='completereg'),
    path('success/', views.success, name='success'),
]