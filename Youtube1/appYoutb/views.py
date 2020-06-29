from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json

# Create your views here.
def home(request):
    url =  'https://youtubemp4.to/download_ajax/'

    datas = {'url': 'https://www.youtube.com/watch?v=GnSj28eryK0'}

    # recuperer la page à scraper

    response = requests.post(url, data=datas)


    # Parser le resultat en HTML pour l'exploitation

    html_soup = BeautifulSoup(response.text, 'html.parser')


    # Verifier que le scrapping à marché

    #print(response.text)
    #200 tout va bien
    try:
        result = response.text
        result = json.loads(result)
        data_html = result['result']
    except Exception as e :
        print('Exception :', e)

    data = {
        'code': data_html 
    }
    return render(request, 'index.html', data )

def Test(request):
    url1 = 'https://www.4kdownload.com/taskio/parse/?media_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DQoSXegxwpPY'
    url =  'https://www.4kdownload.com/taskio/tasks/?task_id=427e1cd8-469b-486b-b218-dd03509b8ee8'

    # recuperer la page à scraper



    response = requests.get(url1)


    # Parser le resultat en HTML pour l'exploitation

    html_soup = BeautifulSoup(response.text, 'html.parser')

    result = response.text
    result = json.loads(result).decode('utf-8')
    data_html = result['task']['task_id']
    # Verifier que le scrapping à marché
    print(data_html)

    req = requests.get(url)
    result = req.text
    result = json.loads(result).decode('utf-8')
    data_html1 = result[0]['task_result']['results']
    data_html2 = result[0]['task_result']['results'][3]['mediaurl']

    data = {
        'video': data_html2
    }
    print(data_html2)
    return render(request, 'test.html', data)