from django.urls import path
from detector import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('check-url/',views.UrlChecker.as_view(), name='check-url')
]