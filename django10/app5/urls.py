from django.urls import path
from app5.views import home
urlpatterns = [
	path('', home),]