from django.urls import  path
from . import views

urlpatterns = [
    path('conatct' , views.contact, name='contact')
]