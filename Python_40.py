class Product:
    def somopum(self, item, quantity, price):
        amount = quantity * price
        print("품명:", item)
        print("수량:", quantity)
        print("단가:", price)
        print("금액:", amount)

product = Product()

product.somopum("노트", 5, 1500)
