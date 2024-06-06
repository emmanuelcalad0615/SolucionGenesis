from Modelo.Factura import Factura


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