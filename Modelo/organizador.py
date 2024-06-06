from openpyxl.workbook import Workbook

class Factura:
    def __init__(self, numero: int, fecha: str, cliente: str, descripcion: str, subtotal: str, iva: str, total: str, condiciones: str, metodo: str):
        self.numero: int = numero
        self.fecha: str = fecha
        self.cliente: str = cliente
        self.descripcion: str = descripcion
        self.subtotal: str = subtotal
        self.iva: str = iva
        self.total: str = total
        self.condiciones: str = condiciones
        self.metodo: str = metodo

class GestorCartera:
    def __init__(self, archivo: str):
        self.archivo = archivo
        self.list_facturas: list[Factura] = []

    def procesar_datos(self) -> tuple[list[Factura], bool, str]:
        try:
            with open(self.archivo, "r", encoding="utf8") as file:
                num = None
                fecha = None
                cliente = None
                descripcion = None
                subtotal = None
                iva = None
                total = None
                condiciones = None
                metodo = None

                for line in file:
                    if line.startswith('Número: '):
                        num = int(line.split(': ')[1])
                    elif line.startswith('Fecha: '):
                        fecha = line.split(': ')[1].strip()
                    elif line.startswith('Cliente: '):
                        cliente = line.split(': ')[1].strip()
                    elif line.startswith('Descripción: '):
                        descripcion = line.split(': ')[1].strip()
                    elif line.startswith('Subtotal: '):
                        subtotal = line.split(': ')[1].strip()
                    elif line.startswith('IVA colombiano: '):
                        iva = line.split(': ')[1].strip()
                    elif line.startswith('Total: '):
                        total = line.split(': ')[1].strip()
                    elif line.startswith('Condiciones de pago: '):
                        condiciones = line.split(': ')[1].strip()
                    elif line.startswith('Método de pago: '):
                        metodo = line.split(': ')[1].strip()
                        factura = Factura(num, fecha, cliente, descripcion, subtotal, iva, total, condiciones, metodo)
                        self.list_facturas.append(factura)
                        num = None
                        fecha = None
                        cliente = None
                        descripcion = None
                        subtotal = None
                        iva = None
                        total = None
                        condiciones = None
                        metodo = None

            return self.list_facturas, True, "Procesado con éxito"

        except FileNotFoundError:
            return [], False, "El archivo no existe."
        except Exception as e:
            return [], False, f"Se produjo un error al procesar el archivo: {str(e)}"

class Exportador:
    def __init__(self, lista_facturas: list[Factura], nombre_archivo_excel: str):
        self.lista_facturas: list[Factura] = lista_facturas
        self.nombre_archivo_excel: str = nombre_archivo_excel

    def exportar_a_excel(self) -> str:
        try:
            wb = Workbook()
            ws = wb.active
            ws.append(["Número", "Fecha", "Cliente", "Descripción", "Subtotal", "IVA", "Total", "Condiciones de pago", "Método de pago"])

            for factura in self.lista_facturas:
                ws.append([
                    factura.numero,
                    factura.fecha,
                    factura.cliente,
                    factura.descripcion,
                    factura.subtotal,
                    factura.iva,
                    factura.total,
                    factura.condiciones,
                    factura.metodo
                ])

            wb.save(self.nombre_archivo_excel)
            return "¡Exportación exitosa!"
        except Exception as e:
            return f"Se produjo un error al exportar a Excel: {str(e)}"