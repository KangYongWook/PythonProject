from django.shortcuts import render
from bs4 import BeautifulSoup
import requests , re
from .models import Information, Topic
# Create your views here.

def get_infos(request):
    topics = Topic.objects.all()
    context = {
        'topics' : topics
    }
    return render(request,'itess.html',context)

