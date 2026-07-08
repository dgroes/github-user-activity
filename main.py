import urllib.request
import json
from collections import Counter
from cli import main


username = main()
url = f'https://api.github.com/users/{username}/events'


# Abre una URL y lee la respuesta
with urllib.request.urlopen(url, data=None) as response:
    html = response.read()
    dato = json.loads(html)
    
    combinaciones = []
    
    for diccionario in dato:
        tipo = diccionario.get("type")
        repo = diccionario.get("repo", {}).get("name")
        
        combinaciones.append((tipo, repo))
        # Quedaría así: [('PushEvent', 'dgroes/github-user-activity'), ('PushEvent', 'dgroes/github-user-activity')...

    #Conteo final
    conteo_final = Counter(combinaciones)
    #print(combinaciones)

    # Impresión limpia
    print(f"\n📊 Actividad de {username}:")
    for (tipo, repo), cantidad in conteo_final.items():
        print(f"- {cantidad} {tipo} hacia el repositorio {repo}")


    # Guardar la última consulta "total" dentro de un fichero
    with open('output.json', 'w', encoding='utf-8') as archivo:
        json.dump(dato, archivo, indent=4)

    
