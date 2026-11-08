import datetime
import os


# Función para pedir un número al usuario
def pedir_numero(pregunta, valor_por_defecto=None):
    """
    Esta función hace la pregunta que le pasemos y no te deja avanzar 
    hasta que escribas un número válido.
    """
    while True:
        texto = input(pregunta)
        
        # Si el usuario no escribe nada (pulsa Enter) y hemos configurado un valor por defecto
        if texto == "" and valor_por_defecto is not None:
            return valor_por_defecto
            
        try:
            numero = float(texto)
            return numero # 'return' hace dos cosas: sale de la función (rompe el bucle) y devuelve el número
        except ValueError:
            print("Error: Tienes que escribir un número.")
# Final de la función pedir_numero

print("=== NUEVO PRESUPUESTO ===")

# 1. PEDIR EL NOMBRE
cliente = input("Nombre del cliente: ")

# 2. PEDIR LAS HORAS (Con la nueva función)
horas = pedir_numero("Horas previstas: ")

# 3. PEDIR LA TARIFA
tarifa = pedir_numero("Tarifa por hora: ")

# 4. PEDIR EL DESCUENTO
descuento_pct = pedir_numero("% de descuento (Pulsa Enter para 0%): ", valor_por_defecto=0.0)

# 4.1. Verificar el IVA
iva_pct = pedir_numero("% de IVA (Pulsa Enter para 21%): ", valor_por_defecto=21.0)

# 5. HACER LOS CÁLCULOS
subtotal = horas * tarifa
descuento_val = subtotal * (descuento_pct / 100)
base = subtotal - descuento_val
iva_val = base * (iva_pct / 100)
total = base + iva_val

# 6. CREAR EL TEXTO DEL PRESUPUESTO
# La 'f' antes de las comillas triples permite meter las variables entre llaves {}
documento = f"""
PRESUPUESTO
===
Nombre: {cliente}
Fecha: {datetime.date.today()}
---
Previsión:  {horas} horas
Tarifa:    x{tarifa:.2f} €/hora
---
Subtotal:   {subtotal:.2f} €
Descuento: -{descuento_val:.2f} €
---
Base:       {base:.2f} €
IVA ({iva_pct:.0f}%): +{iva_val:.2f} €
---
TOTAL:      {total:.2f} €
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