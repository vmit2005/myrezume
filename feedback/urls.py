from django.urls import path
from django.contrib import  admin
from . import views

urlpatterns = [
    path('', views.feedbacks, name ='feedback'),
    # path('<int:feed_id/>', views.detail, name='detail'),

    # Auth (страница для входа в личный кабинет)
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    # path('new_feedback/', views.new_feedback, name='newfeedback'),
    path('new_feedback2/', views.new_feedback2, name='newfeedback2'),





]