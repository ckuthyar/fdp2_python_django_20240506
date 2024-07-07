from django.urls import path
from app1.views import doctor1,doctor2,doctor3,doctorlayout
urlpatterns = [
    path('doctor1/',doctor1,name='doctor1'),
    path('doctor2/',doctor2,name='doctor2'),
    path('doctor3/',doctor3,name='doctor3'),
    path('doctorlayout/',doctorlayout,name='doctorlayout')
]