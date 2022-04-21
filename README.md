# scraping_NewsPortal
This code will scrape data from the news web and the output is a new web that displays the most popular news on detik.com in real time
## How this code works
####1. Install package
    Install requests:
        pip install requests
    Install beatifulsoup
        pip install beautifulsoup4
####2. Ceate new folder **'detik_scraper.py'**
````
import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})

soup = BeautifulSoup(html_doc.text, 'html.parser')

populer_area = soup.find(attrs={'class': 'grid-row list-content'})
titles = populer_area.findAll(attrs={'class' : 'media__title'})
images = populer_area.findAll(attrs={'class':'media__image'})
#print(populer_area)

for image in images:
    print(image.find('a').find('img')['title']
````
####3. Create new folder **'run.py'**
````
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detik.populer')
#fungsi scrapter
def detik_populer():
    html_doc = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})

    soup = BeautifulSoup(html_doc.text, 'html.parser')

    populer_area = soup.find(attrs={'class': 'grid-row list-content'})
    titles = populer_area.findAll(attrs={'class': 'media__title'})
    images = populer_area.findAll(attrs={'class': 'media__image'})

    return render_template('index.html',images=images)






if __name__=='__main__':
    app.run(debug=True)
````
####4 Create new directory **'templates'**
####5. In **_templates_** create new file **'index.html'**
## For finishing run on folder run.py