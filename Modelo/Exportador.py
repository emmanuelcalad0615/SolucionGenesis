from openpyxl.workbook import Workbook

from Modelo.Factura import Factura


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