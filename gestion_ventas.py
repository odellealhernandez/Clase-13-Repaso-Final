import datetime as datetime
import csv
import pandas as pd


def ingresar_ventas():
    """Función para ingresar una venta y guardarla en un archivo CSV."""
    IVA = 0.13 # Tasa de IVA del 13%
    ventas = []
    fecha_venta = ""
    nombre_cliente = ""
    
    while True:    
        try:
            nombre_producto = input("Ingrese el nombre del producto: ").upper()
            cantidad = int(input("Ingrese la cantidad vendida: "))
            precio_unitario = float(input("Ingrese el precio unitario: "))
            
            
            if fecha_venta == "" or nombre_cliente == "":
                fecha_venta = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                nombre_cliente = input("Ingrese el nombre del cliente (opcional): ").upper()
            
            # validaciones de datos
            if nombre_cliente == "":
                nombre_cliente = "CLIENTE GENERICO"

            if cantidad <= 0:
                print("❌ La cantidad debe ser un número positivo.")
                continue
            
            if precio_unitario < 0:
                print("❌ El precio unitario debe ser un número positivo.")
                continue
            
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingrese los datos correctamente.")
            continue
        
        # crear una lista con datos de la venta
        venta = {
            "Producto": nombre_producto,
            "Cantidad": cantidad,
            "Precio": precio_unitario,
            "Fecha": fecha_venta,
            "Cliente": nombre_cliente
        }
        
        ventas.append(venta)
        continuar = input("¿Desea ingresar otra venta? (s/n): ").lower()
        if continuar != 's':
            if not guardar_ventas_csv(ventas):
                print("❌ Error al guardar las ventas en CSV. Ingrese nuevamente las ventas.")
                break
            
            # IMPRIMIR EL TICKET DE VENTA
            print("\n🎟️  ======== Ticket de Venta ======== 🎟️")
            print("-" * 40)
            print(f"Cliente: {ventas[0]['Cliente']} | {ventas[0]['Fecha']}")
            print("-" * 40)
            
            for venta in ventas:
                # imprimir detalles de cada venta en una sola línea con formato ticket
                print(f"{venta['Producto']} x {venta['Cantidad']} @ ${venta['Precio']:.2f} c/u = ${venta['Cantidad'] * venta['Precio']:.2f}")
                print("-" * 40)
                
            subtotal = sum(venta['Cantidad'] * venta['Precio'] for venta in ventas)
            iva = subtotal * IVA
            print("Subtotal: ${:.2f}".format(subtotal))
            print("IVA total: ${:.2f}".format(iva))
            print(f"Total a pagar: ${subtotal + iva:.2f}")
            
            print("\n✅ Ventas guardadas exitosamente.")
            break
        
def guardar_ventas_csv(ventas):
    """Guarda las ventas en un archivo CSV."""
    ARCHIVO_CSV = 'ventas.csv'
    
    if not (ventas):
        print("No hay ventas para guardar.")
        return False
    try:
        # abrir el archivo CSV en modo esritura y agregar las ventas usando csv.DictWriter
        with open(ARCHIVO_CSV, mode='a', newline='', encoding='utf-8') as archivo:
            campos = ['Producto', 'Cantidad', 'Precio', 'Fecha', 'Cliente']
            escritor_csv = csv.DictWriter(archivo, fieldnames=campos)
            
            # escribir la fila de encabezado solo si el archivo está vacío
            if archivo.tell() == 0:
                escritor_csv.writeheader()
            
            for venta in ventas:
                escritor_csv.writerow(venta)
            
            print(f"✅ Ventas guardadas exitosamente en {ARCHIVO_CSV}.")
            return True
            
    except Exception as e:
        print(f"❌ Error al guardar las ventas en CSV: {e}")
        return False

def cargar_ventas(archivo_csv='ventas.csv'):
    """Carga las ventas desde un archivo CSV y devuelve una lista de diccionarios."""
    ventas = []
    try:
        ventas = pd.read_csv(archivo_csv)
        print(f"✅ Ventas cargadas exitosamente desde {archivo_csv}.")
        print(f"se han cargado {len(ventas)} ventas.")
        return ventas
    except FileNotFoundError:
        print(f"❌ El archivo {archivo_csv} no existe.")
        return None
    except Exception as e:
        print(f"❌ Error al cargar las ventas desde CSV: {e}")
        return None
    
    
if __name__ == "__main__":
    ingresar_ventas()