from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('hostel/<str:pk>', views.deleteHostel, name="hostel"),
    path('about/', views.about, name="about"),
]