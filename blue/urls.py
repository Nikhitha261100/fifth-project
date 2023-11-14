from blue.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('keerthi/',keerthi,name='keerthi'),
    path('sunny/',sunny,name='sunny'),
]