class Product:
    def __call__(self, *args, **kwds):
        self.id = ""
        self.name = ""
        self.quantity = 0
        self.price = 0
        self.statusW="A"
    def ShowData(self):
        return f'Product Data:\nId: {self.id}\nName:{self.name}\nQuantity:{self.quantity}\nPrice:{self.price}'
def LoadData(obj):
    print()
    print("Please enter the worker data:\n")
    obj.id=input('Id: ')
    obj.name=input('Name: ')
    obj.quantity=int(input('Quantity: '))
    obj.price=float(input('Price:'))

def main():
    objProduct =Product()
    LoadData(objProduct)
    print(objProduct.ShowData())
    print('Finalizado.')
if __name__=='__main__':
    main()
