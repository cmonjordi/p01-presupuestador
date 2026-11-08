import datetime
import glob
import os
import sys

CARPETA_PRESUPUESTOS = ".datos/presupuestos"

def mostrar_resumen():
    print("=== RESUMEN DE FACTURACIÓN ===")
    
    # glob busca todos los archivos que terminen en .txt dentro de la carpeta presupuestos
    archivos = glob.glob(os.path.join(CARPETA_PRESUPUESTOS, "*.txt"))
    
    if len(archivos) == 0:
        print(f"No hay presupuestos guardados en '{CARPETA_PRESUPUESTOS}/' todavía.")
        return # Salimos de la función sin hacer nada más

    total_facturado = 0.0

    for archivo in archivos:
        # Extraemos solo el nombre del archivo, no toda la ruta
        nombre_limpio = os.path.basename(archivo)
        nombre_sin_extension = os.path.splitext(nombre_limpio)[0]
        total_factura = 0.0
        
        # Abrimos el archivo en modo lectura ("r")
        with open(archivo, "r") as archivo_abierto:
            # Leemos el archivo línea por línea
            for linea in archivo_abierto:
                linea = linea.strip()
                # Si la línea empieza por la palabra "TOTAL:"
                if linea.startswith("TOTAL:"):

                    # 1. Partimos la frase por los dos puntos y nos quedamos la segunda parte
                    parte_derecha = linea.split(":")[1]

                    # 2. Le quitamos el símbolo del euro y los espacios en blanco
                    numero_limpio = parte_derecha.replace("€", "").strip()

                    # 3. Lo convertimos a número y lo sumamos al total
                    total_factura = float(numero_limpio)
                    total_facturado += total_factura

        print(f"- {total_factura:.2f} € ({nombre_sin_extension})")

    print("-" * 30)
    print(f"💰 SUMA TOTAL: {total_facturado:.2f} €\n")

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
            if numero < 0:
                print("Error: El número no puede ser negativo.")
                continue
            return numero # 'return' hace dos cosas: sale de la función (rompe el bucle) y devuelve el número
        except ValueError:
            print("Error: Tienes que escribir un número.")
# Final de la función pedir_numero

if len(sys.argv) > 1 and sys.argv[1].lower() == "resumen":
    # Si se escribe una segunda palabra y es "resumen", se ejecuta la función mostrar_resumen()
    mostrar_resumen()
else:
    # Si no, sigue el presupuesto normal
    print("=== NUEVO PRESUPUESTO ===")

    # 1. PEDIR EL NOMBRE
    cliente = input("Nombre del cliente: ")

    # 2. PEDIR LAS HORAS (Con la nueva función)
    horas = pedir_numero("Horas previstas: ")

    # 3. PEDIR LA TARIFA
    tarifa = pedir_numero("Tarifa por hora: ")

    # 4. PEDIR EL DESCUENTO
    descuento_pct = pedir_numero("% de descuento (Pulsa Enter para 0%): ", valor_por_defecto=0.0)

    # 4.1. VERIFICAR EL IVA
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
=== PRESUPUESTO ===
Fecha: {datetime.date.today()}
------------------------------
Previsión:  {horas} horas
Tarifa:    x{tarifa:.2f} €/hora
------------------------------
Subtotal:   {subtotal:.2f} €
Descuento: -{descuento_val:.2f} €
------------------------------
Base:       {base:.2f} €
IVA ({iva_pct:.0f}%): +{iva_val:.2f} €
------------------------------
TOTAL:      {total:.2f} €
"""

    # Preguntar si se quiere mostrar por pantalla
    while True:
        mostrar = input("¿Ver el presupuesto? (Pulsa Enter o escribe s para verlo/n = no): ").strip().lower()
        if mostrar in ("", "s", "si", "sí"):
            print(documento)
            break
        if mostrar in ("n", "no"):
            break
        print("Respuesta no válida. Escribe 's' o 'n'.")

    # 7. GUARDARLO EN UN ARCHIVO
    # Creamos la carpeta (exist_ok=True evita que dé error si la carpeta ya existe)
    os.makedirs(CARPETA_PRESUPUESTOS, exist_ok=True)

    # Conseguimos la fecha de hoy para el nombre del archivo
    fecha_hoy = datetime.date.today()
    ruta_archivo = os.path.join(CARPETA_PRESUPUESTOS, f"{fecha_hoy}-{cliente}.txt")

    # Abrimos el archivo, escribimos el documento y lo cerramos con un gestor de contexto
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(documento)

    print(f"✅ Guardado en: {ruta_archivo}")