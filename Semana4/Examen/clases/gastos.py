class GestorGastos:
    def __init__(self):
        self.gastos = []

    def agregar_gasto(self, fecha, categoria, monto, descripcion):
        gasto = {
            "fecha": fecha,
            "categoria": categoria,
            "monto": monto,
            "descripcion": descripcion
        }
        self.gastos.append(gasto)

    def total_mes(self, mes):
        total = 0
        for g in self.gastos:
            if g["fecha"].month == mes:
                total += g["monto"]
        return total

    def total_categoria(self, categoria):
        total = 0
        for g in self.gastos:
            if g["categoria"].lower() == categoria.lower():
                total += g["monto"]
        return total

    def listar_gastos(self):
        if not self.gastos:
            print("No hay gastos registrados.")
        for g in self.gastos:
            print(f"{g['fecha'].strftime('%Y-%m-%d')} | {g['categoria']} | ${g['monto']:.2f} | {g['descripcion']}")

    def gasto_promedio_categoria(self, categoria):
        total = 0
        count = 0
        for g in self.gastos:
            if g["categoria"].lower() == categoria.lower():
                total += g["monto"]
                count += 1
        return total / count if count > 0 else 0

              