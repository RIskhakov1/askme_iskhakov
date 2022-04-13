from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('intro/', views.intro, name="intro"),
    path('', views.index, name="index"),
    path('ask/', views.ask, name="ask"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('<int:i>/', views.question_page, name="question_page"),
]
