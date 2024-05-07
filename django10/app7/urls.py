from django.urls import path
from app7.views import home
urlpatterns = [
	path('', home),]