from django.urls import path
from app6.views import home
urlpatterns = [
	path('', home),]