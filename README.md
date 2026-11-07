# Generador de Presupuestos CLI

Una herramienta de línea de comandos escrita en Python para calcular, desglosar y guardar presupuestos de clientes rápidamente.

## Qué hace
- Calcula automáticamente el subtotal, descuentos, base imponible e IVA de un servicio por horas.
- Previene bloqueos del programa: si escribes texto en lugar de números en la tarifa o las horas, te avisará y volverá a preguntar.
- Guarda un registro `.txt` de cada presupuesto en la carpeta `presupuestos/`.
- Permite configurar el IVA personalizado al final del proceso (con un valor por defecto del 21%).
- Incluye un comando de resumen para auditar la suma total de facturación histórica.

## Cómo se ejecuta

Asegúrate de tener Python instalado en tu sistema. Puedes ejecutar el script utilizando `uv` o el intérprete estándar de Python.

**Para crear un nuevo presupuesto (Flujo normal):**
```bash
uv run python main.py
```

**Para ejecutar el comando "resumen":**
```bash
uv run python main.py resumen
```
