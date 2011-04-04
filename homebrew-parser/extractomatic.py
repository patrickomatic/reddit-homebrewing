import urllib, re
from BeautifulSoup import BeautifulSoup

def extractomatic(url):
    source = urllib.urlopen(url)
    html = BeautifulSoup(source.read())
    source.close()
    
    divz = []
    for i in html.body.findAll(attrs = {'class': re.compile('commentarea')}):
        for j in i.findAll(attrs = {'class': re.compile('author gray|usertext-body')}, recursive = True):
            divz.append(j)
    
    result = []
    strip = re.compile('<.*?>|\n')
    count = 0
    for k in divz[::2]:
        user = re.sub(strip, '' , str(k))
        count += 1
        text = re.sub(strip, '', str(divz[count]))
        result.append({user: text})
        count += 1
    
    return result
