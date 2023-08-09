from django.shortcuts import render
from .models import Topic

# Create your views here.
# The views modlue is responsible for what you see when you open the webpage

# this function renders whatever is in index.html 
# found in the learning_logs directory
def index(request):
    """The home page of learning logs"""
    return render(request, 'learning_logs/index.html')


# This function queries the database for topics added according
# to the dates added and the topics.html template displays that page
def topics(request):
    """The page that displays all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


# A function that queries the db using the objects.get() function
#to get the topic Id then orders it according to the most recrently
#added topic using -date_added, then renders it for use to the topic.html template
def topic(request, topic_id):
    """Show the entries associated with a selected topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)