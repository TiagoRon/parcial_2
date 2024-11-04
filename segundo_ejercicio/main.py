from grafo import Graph

star_wars_graph = Graph(dirigido=False)

personajes = ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", 
              "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"]

for personaje in personajes:
    star_wars_graph.insert_vertice(personaje)

aristas = [
    ("Luke Skywalker", "Darth Vader", 4),
    ("Luke Skywalker", "Yoda", 2),
    ("Luke Skywalker", "Leia", 3),
    ("Luke Skywalker", "Han Solo", 3),
    ("Darth Vader", "Yoda", 1),
    ("Leia", "Han Solo", 2),
    ("Han Solo", "Chewbacca", 3),
    ("Rey", "Kylo Ren", 2),
    ("C-3PO", "R2-D2", 4),
    ("Rey", "BB-8", 1)
]

for origen, destino, peso in aristas:
    star_wars_graph.insert_arista(origen, destino, peso)

print("Grafo de personajes de Star Wars:")
star_wars_graph.show_graph()

print("\nArbol de expansion minimo (Kruskal):")
bosque = star_wars_graph.kruskal("Luke Skywalker")
print("Arbol de expansion minimo:", bosque)

contiene_yoda = any("Yoda" in arbol for arbol in bosque)
print("¿El arbol de expansion minimo contiene a Yoda?", "Si" if contiene_yoda else "No")

def obtener_maximo_episodios(grafo):
    max_episodios = 0
    personajes_maximos = (None, None)
    
    for nodo in grafo.elements:
        for arista in nodo['aristas']:
            if arista['peso'] > max_episodios:
                max_episodios = arista['peso']
                personajes_maximos = (nodo['value'], arista['value'])
    
    return personajes_maximos, max_episodios

personajes_max, max_episodios = obtener_maximo_episodios(star_wars_graph)
print(f"\nEl maximo de episodios compartidos es {max_episodios}, entre {personajes_max[0]} y {personajes_max[1]}.")
