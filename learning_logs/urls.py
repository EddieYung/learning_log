"""Defines URL patterns for learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    # An empty string will mean the deafault url, 
    # but the 'Home' means you need to specify the home path    
    path('home/', views.index, name='index'),
    #the page that shows all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for each topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]