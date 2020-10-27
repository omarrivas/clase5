from automagica import *
from difflib import SequenceMatcher
import random

lstLicitaciones = []

navegador = Chrome()
navegador.get("https://www.smt.gob.ar/licitaciones")
resultado = navegador.find_element_by_xpath('//*[@id="faux"]/div[1]') #//*[@id="faux"]/div[1]/div[2]/div[4]
textolicitaciones= resultado.text

#NORMALIZA
textolicitaciones= textolicitaciones.replace("ADQUISICION", "adquisición")
textolicitaciones= textolicitaciones.replace("Adquisición", "adquisición")
textolicitaciones= textolicitaciones.replace("Adquisicion", "adquisición")

#PARSEO
licitacion= ""
posicion1 = textolicitaciones.find("adquisición")
while posicion1!= -1:
    posicion2 = textolicitaciones.find("Ver documentación y novedades")
    if posicion2 != -1:
        licitacion= textolicitaciones[posicion1:posicion2]

    if licitacion!= "":
        lstLicitaciones.append(licitacion)
        #print(licitacion)

    textolicitaciones= textolicitaciones[posicion2+29:len(textolicitaciones)]
    posicion1 = textolicitaciones.find("adquisición")

navegador.quit()

SALUDOS = ("hola", "hey", "buenas", "que tal?", "buen dia necesito informacion", "buenas tardes")
RESPUESTA_SALUDO = ["Hola un gusto!", "Que tal, un gusto", "Un gusto saludarte", "Hola!"]
LICITACION = ("informacion sobre licitaciones", "quiero conocer las licitaciones", "cuales son las licitaciones")
RESPUESTA_LICITACION = ["Te comparto la info:", "A continuación te paso la informacion de licitaciones existentes"]


def detectaSaludo(frase):
    if frase.lower() in SALUDOS:
        return random.choice(RESPUESTA_SALUDO)


def detectaLicitacion(frase):
    if frase.lower() in LICITACION:
        licitacion= ""
        for valor in lstLicitaciones:
            licitacion= licitacion + valor + "-------------------------------------------\n"
        return random.choice(RESPUESTA_LICITACION) + "\n" + licitacion



def diferencia_de_textos(text1, text2):
    a = text1.strip().lower()
    b = text2.strip().lower()

    ratio = 0.00
    if a == b:
        ratio = 1.00
    else:
        ratio = SequenceMatcher(None, a, b).ratio()
    return (ratio)


def detectaRespuestas(frase):
    dist = 0
    distancia = 0
    tipoRpta = 0

    for palabra in SALUDOS:
        dist = diferencia_de_textos(palabra, frase)
        if dist >= distancia:
            distancia= dist
            tipoRpta= 1
    for palabra in LICITACION:
        dist = diferencia_de_textos(palabra, frase)
        if dist >= distancia:
            distancia= dist
            tipoRpta= 2

    if tipoRpta== 1:
        return random.choice(RESPUESTA_SALUDO)
    elif tipoRpta== 2:
        licitacion = ""
        for valor in lstLicitaciones:
            licitacion = licitacion + valor + "-------------------------------------------\n"
        return random.choice(RESPUESTA_LICITACION) + "\n" + licitacion


flag=True
print("ROBO: Hola. Mi nombre es Robotin. Responderé todas tus consultas sobre licitaciones de la Municipalidad de SM Tucumán. Si quieres terminar escribe chau!")
while(flag==True):
 respuesta_usuario = input()
 respuesta_usuario = respuesta_usuario.lower()
 if(respuesta_usuario!='chau'):
    if(respuesta_usuario=='gracias' or respuesta_usuario=='muchas gracias' ):
        print("ROBO: De nada...")
    else:
        respuesta_robo= detectaRespuestas(respuesta_usuario)
        if respuesta_robo != None:
            print("ROBO: " + respuesta_robo)
        else:
            print("ROBO: Diculpa, no entiendo...")
 else:
    flag=False
    print("ROBO: Adios! Cuidate..")

