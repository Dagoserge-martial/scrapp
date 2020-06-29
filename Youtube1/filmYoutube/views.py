from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json

# Create your views here.
def home(request):
    
    data = {
        
    }
    return render(request, 'index.html', data )

def Test(request):
   
    data = {
        
    }
    return render(request, 'test.html', data)