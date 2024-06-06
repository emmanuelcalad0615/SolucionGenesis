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



