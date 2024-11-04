
class Pokemon:
    def __init__(self, nombre, numero, tipos):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos

    def __repr__(self):
        return f"{self.nombre} (# {self.numero}, Tipo: {', '.join(self.tipos)})"


class NodoArbol:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.root = None

    def insertar(self, key, data):
        if self.root is None:
            self.root = NodoArbol(key, data)
        else:
            self._insertar_recursivo(self.root, key, data)

    def _insertar_recursivo(self, nodo, key, data):
        if key < nodo.key:
            if nodo.left is None:
                nodo.left = NodoArbol(key, data)
            else:
                self._insertar_recursivo(nodo.left, key, data)
        else:
            if nodo.right is None:
                nodo.right = NodoArbol(key, data)
            else:
                self._insertar_recursivo(nodo.right, key, data)

    def buscar(self, key):
        return self._buscar_recursivo(self.root, key)

    def _buscar_recursivo(self, nodo, key):
        if nodo is None or nodo.key == key:
            return nodo.data if nodo else None
        elif key < nodo.key:
            return self._buscar_recursivo(nodo.left, key)
        else:
            return self._buscar_recursivo(nodo.right, key)

    def buscar_proximidad(self, prefix):
        resultados = []
        self._buscar_proximidad_recursivo(self.root, prefix.lower(), resultados)
        return resultados

    def _buscar_proximidad_recursivo(self, nodo, prefix, resultados):
        if nodo:
            if prefix in nodo.key.lower():
                resultados.append(nodo.data)
            self._buscar_proximidad_recursivo(nodo.left, prefix, resultados)
            self._buscar_proximidad_recursivo(nodo.right, prefix, resultados)

    def listar_en_orden(self):
        resultados = []
        self._listar_en_orden_recursivo(self.root, resultados)
        return resultados

    def _listar_en_orden_recursivo(self, nodo, resultados):
        if nodo:
            self._listar_en_orden_recursivo(nodo.left, resultados)
            resultados.append(nodo.data)
            self._listar_en_orden_recursivo(nodo.right, resultados)
