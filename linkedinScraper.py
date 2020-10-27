from linkedin_scraper import Person, actions
from selenium import webdriver

cantPaginasaBuscar= 1
linksLinkedin = []

###################################################
## 1ero BUSCA LOS LINKEDINS
navegadorGoogle = webdriver.Chrome()
try:
    queryBusqueda = 'site:linkedin.com/in/ AND "python developer" AND "Argentina"'

    for i in range(cantPaginasaBuscar+1):
        navegadorGoogle.get("https://www.google.com/search?q=" + queryBusqueda + "&start=" + str(10 * i))
        linkEncontrados = navegadorGoogle.find_elements_by_xpath('//a[starts-with(@href, "https://uk.linkedin.com")]')

        for link in linkEncontrados:
            print(link.get_attribute("href"))
            linksLinkedin.append(link.get_attribute("href"))

    navegadorGoogle.close()
    navegadorGoogle.quit()
except:
    navegadorGoogle.close()
    navegadorGoogle.quit()


###################################################
## 2do BUSCA EMAILS
navegadorLinkedin = webdriver.Chrome() #Chrome_Options is deprecated. So we use options instead.

try:
    archivoResultado = open(r"C:\\Users\\orivas\\AppData\\Local\\Programs\\Python\\Code\\00-linkedin\\contactos.txt", "w+")

    ###################################################
    ## LOGIN
    email = 'info@educae.com.ar'
    password = "turk182182"
    actions.login(navegadorLinkedin, email, password) # if email and password isnt given, it'll prompt in terminal

    for cadaLink in linksLinkedin:
        print("Scrapea " + cadaLink)

        ###################################################
        ## TOMA DATOS PERSONA
        person = Person(cadaLink, driver=navegadorLinkedin, scrape=True, close_on_complete=False)
        nombre= person.name
        link= person.linkedin_url
        experiencia= person.experiences
        educacion= person.educations
        interes= person.interests
        empresa= person.company
        puesto= person.job_title

except:
    navegadorLinkedin.close()
    navegadorLinkedin.quit()
