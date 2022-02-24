from django.urls import path, include

from .views import *

urlpatterns = [
    path('users/', User_Data_ListView.as_view()),
    path('users/<int:id>/', User_Data_UpdateView.as_view()),

]
