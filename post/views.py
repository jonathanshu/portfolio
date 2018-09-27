from django.shortcuts import render
from django.http import HttpResponse
from celery import Celery
import requests

app = Celery()
app.config_from_object('post.config')
# Create your views here.
def index(request):
    fetch_url('http://stats.nba.com/stats/boxscore')
    return render(request, 'post/index.html')

@app.task
def fetch_url(url):
    r = requests.get(url)
    print(r.status_code)
    return r.status_code
