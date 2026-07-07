import urllib.request
import sys
import json
from collections import Counter

def main():
    # sys.argv[0] es siempre el nombre del archivo ("main.py")
    # Validamos que se hayan pasado suficientes argumentos
    if len(sys.argv) < 1:
        print("[GITHUB-ACTIVITY]: Para buscar la actividad de un usuario introdusca un username. Uso: python main.py <username>")
        return

    elif len(sys.argv) > 2:
        print("[ERROR]: El programa solo recibe un parametro. Uso: python main.py <username>")
        return
    username = sys.argv[1] # Captura del username

    return username


username = main()
url = f'https://api.github.com/users/{username}/events'


# Abre una URL y lee la respuesta
with urllib.request.urlopen(url, data=None) as response:
    html = response.read()
    
    dato = json.loads(html)
    lista = []
    for diccionario in dato:
        if diccionario.get("type") == "PushEvent":
                #print("---- Evento Push Encontrado ----")
                name = diccionario.get("repo", {}).get("name")
                lista.append(name)

               
                #print(json.dumps(diccionario, indent=4, ensure_ascii=False))

    
    # print(diccionario.get("repo"))
    contador = Counter(lista)
    for repo, cantidad in contador.items():
         print(f" - {cantidad} Push Events hacia el repositorio {repo}")

    with open('salida.json', 'w', encoding='utf-8') as archivo:
        json.dump(dato, archivo, indent=4)

    
