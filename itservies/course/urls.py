from django.urls import path
from course import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('contact/',views.contact),
    path('about/',views.about),
    path('faculty/',views.faculty),

]