# declaración de variables
nombre_cliente = input("Ingrese el nombre del cliente: ")
horas_estimadas = float(input("Ingrese las horas estimadas de trabajo: "))
tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

# operaciones
subtotal = horas_estimadas * tarifa_por_hora
descuento = subtotal * (descuento / 100)
base_imponible = subtotal - descuento
iva = base_imponible * (0.21 if iva_impuesto == "" else float(iva_impuesto) / 100)
total = base_imponible + iva

# factura
print(f"\nFactura para: {nombre_cliente}€")
print(f"Subtotal: {subtotal:.2f}€")
print(f"Descuento: {descuento:.2f}€")
print(f"Base Imponible: {base_imponible:.2f}€")
print(f"IVA (21%): {iva:.2f}€")
print(f"Total a pagar: {total:.2f}€")