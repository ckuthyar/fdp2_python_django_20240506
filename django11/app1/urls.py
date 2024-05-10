from django.urls import path
from app1.views import landing,sign_in,Sign_up,home
urlpatterns = [
	path('',landing),
	path('login',sign_in,name='login'), # here name is used to alias the function name so that we can use shorter name while calling it in html URL
	path('signup',Sign_up,name='signup'),
	path('home',home,name='home'),
]