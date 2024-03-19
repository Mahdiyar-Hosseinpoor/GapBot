from bot import views
from django.urls import path

urlpatterns = [
    path('', views.reqst, name='mybot')
]