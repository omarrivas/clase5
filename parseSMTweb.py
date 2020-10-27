import bs4
import requests

# Capturamos la url ingresada en la variable "url"
url = "https://www.smt.gob.ar/"

# Capturamos el hml de la pagina web y creamos un objeto Response
r  = requests.get(url)
data = r.text

# Creamos el objeto soup y le pasamos lo capturado con request
soup = bs4.BeautifulSoup(data, 'lxml')

# Capturamos el titulo de la página y luego lo mostramos
# Lo que hace BeautifulSoup es capturar lo que esta dentro de la etiqueta title de la url
titulo = soup.title.text
print ("El titulo de la pagina es: " + titulo)

# Buscamos todas etiquetas HTML (a) y luego imprimirmos todo lo que viene despues de "href"
for link in soup.find_all('a'):
    print(link.get('href'))
