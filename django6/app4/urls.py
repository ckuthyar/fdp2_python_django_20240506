from django.urls import path
from app4.views import home
urlpatterns = [
	path('', home),]