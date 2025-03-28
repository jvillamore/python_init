class Producto:
    def __init__(self, name, precio, stock):
        self.name = name
        self._precio = precio
        self._stock = stock

    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self._stock

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("Precio no puede ser negativo")
        self._precio = nuevo_precio

    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise ValueError("Stock no puede ser negativo")
        self._stock = nuevo_stock

    @precio.deleter
    def precio(self):
        print(f"El precio del producto {self.name} a sido eliminado")
        del self._precio

    @stock.deleter
    def stock(self):
        print(f"El stock del producto {self.name} a sido eliminado")
        del self.stock

    def precio_intentario_total_producto(self):
        total = self._precio * self._stock
        return f"Valor total del inventario del producto es = $ {total:.2f}"


producto1 = Producto("Teclado", 100, 10)
print(producto1.precio)
print(producto1.stock)

producto1.precio = 150
producto1.stock = 20
print(producto1.precio)
print(producto1.stock)
print(producto1.precio_intentario_total_producto())
