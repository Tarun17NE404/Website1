from django.urls import path, include
from . import views

urlpatterns = [
    #/genres/
    path('', views.index.as_view(), name="index"),

    #/genres/1
    path('<pk>/', views.details.as_view(), name="details")
]
    #path('register/', views.userform.as_view(), name="userform"),