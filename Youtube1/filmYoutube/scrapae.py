import requests
from bs4 import BeautifulSoup
import json

myUrl = 'https://lastofafrika.com/category/long-metrage/'
#myUrl = 'https://lastofafrika.com/category/long-metrage/page/3/'
urlSite2 = 'https://chalawoodtv.com/category/videos/'



#---------- PAGINATION ----------------
req = requests.get(urlSite2)
if req.status_code == 200:
    html_doc = req.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    pagination = soup.find('div', attrs={'class':"wp-pagenavi"})
    spana = pagination.findAll('a')
    print(len(spana))
    number_page = int(spana[-3].text)
    print(number_page, '+++++ pages')


def getFilmLongMetrage(url):
    nbvideo = 0
    nbPage = 0
    for i in range(1,2):
        nbPage += 1
        urls = url + 'page/{}/'.format(i)
        req = requests.get(urls)
        if req.status_code == 200:
            html_doc = req.text
            soup = BeautifulSoup(html_doc, 'html.parser')
            videoDiv = soup.find('div', attrs={'id': 'primary'})
            videoUl = videoDiv.find('ul', attrs={'class': 'g1-collection-items'})
            videoUnic = videoUl.findAll('li')

            for item in videoUnic:
                nbvideo +=1

                try:
                    img = item.find('img')
                    link = item.find('a')
                    lien = link['href']
                    titree = item.find('h3')
                    disponibilitee = item.find('time')

                    titre = titree.text
                    disponibilite = disponibilitee.text
                    image = img['src']
                    print('ok')

                    #============== lien de lecture video ======#
                    req2 = requests.get(lien)
                    if req2.status_code == 200:
                        html_doc = req2.text
                        soup = BeautifulSoup(html_doc, 'html.parser')
                        try:
                            urlV = soup.find('iframe', attrs={"class": "youtube-player"})
                            dureV = soup.find('div', attrs={'div': 'ytp-time-display'})
                            dureSpan = dureV.find('span', attrs={'class': 'ytp-time-duration'}).text
                        except  Exception as e:
                            print('pas de lien de lecture')


                        urlVideo = urlV['src']

                    print('Titre =====>', titre)
                    print('duree =====>', dureSpan)
                    print('Url video =====>', urlVideo)
                    print(lien)
                except Exception as e:
                    print("nooooonnn")
                
                # print('Titre =====>',titre)
                # print('disponibilite =====>', disponibilite)
                # print('image =====>', image)
                # print('=+=' *20)
        else:
            print('page {} non trouvé!'.format(nbPage))
        
    print(nbvideo, 'Videos scrapé')
    print(nbPage, 'pages scrapé')

def getAfric(url):
    nbvideo = 0
    for i in range(1,number_page+1):
        urls = url + 'page/{}/'.format(i)
        req = requests.get(urls)
        if req.status_code == 200:
            html_doc = req.text
            soup = BeautifulSoup(html_doc, 'html.parser')
            allVideo = soup.find('div', attrs={'class': 'post_ajax_tm'})
            videoDiv = allVideo.findAll('div', attrs={'class': 'row'})
            print(len(videoDiv))
            count = 0
            for items in videoDiv:
                count +=1
                videos = items.findAll('div', attrs={'class':'col-md-3 col-sm-6 col-xs-6'})
                nbvideo += int(len(videos))
                print(count)
                print(len(videos), '0000000000')
                
                # for item in videos:
                #     titr = item.find('p')
                #     img = item.find('img')
                #     image = img['src']

                #     titre = titr.text
                    
                #     print('Titre =====>',titre)
                #     print('image =====>',image)
                #     print('**++**'*20)

    print(nbvideo, 'Videos')

        


#getAfric(urlSite2)
getFilmLongMetrage(myUrl)