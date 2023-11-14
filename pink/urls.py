from pink.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('sweety/',sweety,name='sweety'),
    path('nannu/',nannu,name='nannu'),
]