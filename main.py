import datetime
import os

print("=== NUEVO PRESUPUESTO ===")

# 1. PEDIR EL NOMBRE
cliente = input("Nombre del cliente: ")

# 2. PEDIR LAS HORAS (Con un bucle para que no se rompa si meten texto)
while True:
    try:
        texto = input("Horas estimadas: ")
        horas = float(texto)
        break # Si es un número, rompe el bucle y sigue adelante
    except ValueError:
        print("Error: Tienes que escribir un número, no texto.")

# 3. PEDIR LA TARIFA
while True:
    try:
        texto = input("Tarifa por hora (€): ")
        tarifa = float(texto)
        break
    except ValueError:
        print("Error: Tienes que escribir un número.")

# 4. PEDIR EL DESCUENTO
while True:
    try:
        texto = input("% de descuento (Pulsa Enter para 0): ")
        if texto == "": # Si el usuario solo pulsa Enter, la respuesta está vacía
            descuento_pct = 0.0
            break
        descuento_pct = float(texto)
        break
    except ValueError:
        print("Error: Tienes que escribir un número.")

# 5. HACER LOS CÁLCULOS
subtotal = horas * tarifa
descuento_val = subtotal * (descuento_pct / 100)
base = subtotal - descuento_val
iva_val = base * 0.21 # El IVA fijo al 21%
total = base + iva_val

# 6. CREAR EL TEXTO DEL PRESUPUESTO
# La 'f' antes de las comillas triples permite meter las variables entre llaves {}
documento = f"""
PRESUPUESTO - {cliente}
---
Subtotal:   {subtotal} €
Descuento: -{descuento_val} €
Base:       {base} €
IVA (21%):  {iva_val} €
TOTAL:      {total} €
"""

# Mostrarlo por pantalla
print(documento)

# 7. GUARDARLO EN UN ARCHIVO
# Creamos la carpeta (exist_ok=True evita que dé error si la carpeta ya existe)
os.makedirs("presupuestos", exist_ok=True) 

# Conseguimos la fecha de hoy para el nombre del archivo
fecha_hoy = datetime.date.today()
ruta_archivo = f"presupuestos/{fecha_hoy}-{cliente}.txt"

# Abrimos el archivo, escribimos el documento y lo cerramos con un gestor de contexto
with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    archivo.write(documento)

print(f"✅ Guardado en: {ruta_archivo}")