import pandas as pd

def cargar_excel(ruta):
    try:
        df = pd.read_excel(ruta, engine="openpyxl")
        print("✅ Archivo cargado correctamente.\n")
        return df
    except Exception as e:
        print("❌ Error al cargar el archivo:", e)
        return None

def mostrar_info(df):
    print("\n📊 Información del archivo:")
    print(df.info())
    print("\nPrimeras filas:")
    print(df.head())

def filtrar(df, columna, valor):
    if columna not in df.columns:
        print(f"❌ La columna '{columna}' no existe.")
        return df
    return df[df[columna] == valor]

def modificar_valor(df, fila, columna, nuevo_valor):
    try:
        df.at[fila, columna] = nuevo_valor
        print(f"✏️ Valor en fila {fila}, columna '{columna}' cambiado a '{nuevo_valor}'.")
    except Exception as e:
        print("❌ Error modificando el valor:", e)

def guardar_excel(df, nombre_archivo):
    try:
        df.to_excel(nombre_archivo, index=False, engine="openpyxl")
        print(f"✅ Archivo guardado como '{nombre_archivo}'")
    except Exception as e:
        print("❌ Error al guardar el archivo:", e)

# -------------------------
# 🧪 Ejemplo de uso real
# -------------------------

if __name__ == "__main__":
    ruta = input("📂 Ruta del archivo Excel: ")
    df = cargar_excel(ruta)

    if df is not None:
        mostrar_info(df)

        # Filtro opcional
        if input("\n¿Quieres filtrar datos? (s/n): ").lower() == 's':
            col = input("Columna por la que filtrar: ")
            val = input("Valor que debe tener: ")
            df = filtrar(df, col, val)
            print(df)

        # Modificación opcional
        if input("\n¿Quieres modificar algún valor? (s/n): ").lower() == 's':
            f = int(input("Número de fila (empezando desde 0): "))
            col = input("Columna a modificar: ")
            val = input("Nuevo valor: ")
            modificar_valor(df, f, col, val)

        # Guardar resultado
        nombre_salida = input("\n📁 Nombre del nuevo archivo Excel (ej: resultado.xlsx): ")
        guardar_excel(df, nombre_salida)
