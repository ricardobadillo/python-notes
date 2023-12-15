productos = [
    {"nombre": "PS5", "precio": 600},
    {"nombre": "Audífonos", "precio": 100},
    {"nombre": "TV", "precio": 400}
]

productos_caros = list(filter(lambda producto: producto["precio"] > 500, productos))
print(productos_caros)

