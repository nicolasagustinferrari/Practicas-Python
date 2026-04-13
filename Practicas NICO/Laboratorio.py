ventas = [
    {'fecha': '07-05-25', 'producto': 'mouse Logitech', 'cantidad': 1, 'precio': 125.5},
    {'fecha': '10-05-25', 'producto': 'monitor LG', 'cantidad': 2, 'precio': 475.2},
    {'fecha': '10-05-25', 'producto': 'teclado Razer', 'cantidad': 5, 'precio': 155.0},
    {'fecha': '12-05-25', 'producto': 'mousepad xl', 'cantidad': 2, 'precio': 90.0},
    {'fecha': '13-05-25', 'producto': 'auriculares Hyperx', 'cantidad': 3, 'precio': 140.5},
]


ingresosTotales = 0
for venta in ventas:
    ingresosTotales += venta['cantidad'] * venta['precio']



ventas_por_producto = {}
for venta in ventas: 
    prod = venta['producto']
    ventas_por_producto[prod] = ventas_por_producto.get(prod, 0) + venta['cantidad']
    
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)



precios_por_producto = {}
for venta in ventas:
    prod = venta["producto"]
    subtotal = venta["cantidad"] * venta["precio"]
    cant = venta["cantidad"]
    
    if prod not in precios_por_producto:
        precios_por_producto[prod] = (subtotal, cant)
    else:
        acumulado_dinero, acumulado_cant = precios_por_producto[prod]
        precios_por_producto[prod] = (acumulado_dinero + subtotal, acumulado_cant + cant)



ingresos_por_dia = {}
for venta in ventas:
    fecha = venta['fecha']
    subtotal = venta['cantidad'] * venta['precio']
    ingresos_por_dia[fecha] = ingresos_por_dia.get(fecha, 0) + subtotal


resumen_ventas = {}
for prod, (total_dinero, total_cant) in precios_por_producto.items():
    resumen_ventas[prod] = {
        "cantidad_total": total_cant,
        "ingresos_totales": total_dinero,
        "precio_promedio": total_dinero / total_cant
    }

print(f"Ingresos Totales: ${ingresosTotales}")
print('\n')
print(f"Producto más vendido: {producto_mas_vendido}")
print('\n')
print("Resumen por producto:", resumen_ventas)
print('\n')
print("Ingresos por día:", ingresos_por_dia)