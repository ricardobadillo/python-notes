import copy

# El map no muta el diccionario inicial.

productos = [
    {"nombre": "PS5", "precio": 600},
    {"nombre": "Audífonos", "precio": 100},
    {"nombre": "TV", "precio": 400}
]

precios = list(map(lambda producto: producto["precio"], productos))
print(f"El gasto total de la lista de los productos es: {sum(precios)}.")
print("=" * 20)


# Se utilizó una copia profunda.
def crear_impuestos(producto):
    producto_copy = copy.deepcopy(producto)
    producto_copy["impuesto"] = producto_copy["precio"] * 0.25
    return producto_copy


# Imprimir datos para observar inmutabilidad.
productos_impuestos = list(map(crear_impuestos, productos))
print(f"Los productos son:\n{productos}")
print("=" * 20)
print(f"Los productos con el campo impuestos agregado son:\n{productos_impuestos}")