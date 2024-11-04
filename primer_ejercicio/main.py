from pokemon_estructuras import Pokemon, ArbolBinarioBusqueda

def cargar_datos(pokemons, arbol_nombre, arbol_numero, arbol_tipo):
    for pokemon in pokemons:
        arbol_nombre.insertar(pokemon.nombre, pokemon)
        arbol_numero.insertar(pokemon.numero, pokemon)
        for tipo in pokemon.tipos:
            arbol_tipo.insertar(tipo, pokemon)

def buscar_pokemon(arbol_numero, arbol_nombre, numero=None, nombre=None):
    if numero:
        resultado = arbol_numero.buscar(numero)
        if resultado:
            print(resultado)
    if nombre:
        resultados = arbol_nombre.buscar_proximidad(nombre)
        for res in resultados:
            print(res)

def listar_pokemon_tipo(arbol_tipo, tipo):
    resultados = arbol_tipo.buscar_proximidad(tipo)
    for res in resultados:
        print(res)

def listar_pokemon_orden(arbol_numero, arbol_nombre):
    print("Listado por numero:")
    for pokemon in arbol_numero.listar_en_orden():
        print(pokemon)
    print("\nListado por nombre:")
    for pokemon in arbol_nombre.listar_en_orden():
        print(pokemon)

def mostrar_datos_especificos(arbol_nombre):
    for nombre in ["Jolteon", "Lycanroc", "Tyrantrum"]:
        pokemon = arbol_nombre.buscar(nombre)
        if pokemon:
            print(pokemon)

def contar_pokemon_tipo(arbol_tipo, tipo1, tipo2):
    tipo1_count = len(arbol_tipo.buscar_proximidad(tipo1))
    tipo2_count = len(arbol_tipo.buscar_proximidad(tipo2))
    print(f"Cantidad de Pokemon tipo {tipo1}: {tipo1_count}")
    print(f"Cantidad de Pokemon tipo {tipo2}: {tipo2_count}")

pokemons = [
    Pokemon("Bulbasaur", 1, ["planta", "veneno"]),
    Pokemon("Ivysaur", 2, ["planta", "veneno"]),
    Pokemon("Venusaur", 3, ["planta", "veneno"]),
    Pokemon("Charmander", 4, ["fuego"]),
    Pokemon("Charmeleon", 5, ["fuego"]),
    Pokemon("Charizard", 6, ["fuego", "volador"]),
    Pokemon("Squirtle", 7, ["agua"]),
    Pokemon("Wartortle", 8, ["agua"]),
    Pokemon("Blastoise", 9, ["agua"]),
    Pokemon("Jolteon", 135, ["electrico"]),
    Pokemon("Lycanroc", 745, ["roca"]),
    Pokemon("Tyrantrum", 697, ["roca", "dragon"]),
]

arbol_nombre = ArbolBinarioBusqueda()
arbol_numero = ArbolBinarioBusqueda()
arbol_tipo = ArbolBinarioBusqueda()

cargar_datos(pokemons, arbol_nombre, arbol_numero, arbol_tipo)

print("Buscar por numero y nombre (aproximado):")
buscar_pokemon(arbol_numero, arbol_nombre, numero=1, nombre="bul")

print("\nListar Pokemon de tipo 'agua':")
listar_pokemon_tipo(arbol_tipo, "agua")

print("\nListar Pokemon en orden ascendente por numero y nombre:")
listar_pokemon_orden(arbol_numero, arbol_nombre)

print("\nMostrar datos de Pokemon especificos:")
mostrar_datos_especificos(arbol_nombre)

print("\nContar Pokemon de tipo 'electrico' y 'acero':")
contar_pokemon_tipo(arbol_tipo, "electrico", "acero")
