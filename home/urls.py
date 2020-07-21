from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('reg/', views.reg, name='reg'),
    path('add/',views.add, name='add')

]