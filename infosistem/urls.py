from django.urls import path
from . import views

urlpatterns = [
    path('newcopybook', views.newcopybook, name ='newcopybook'),
    # path('<int:feed_id/>', views.detail, name='detail'),

]