#HomeWork No.2

class pen:

    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price


MyPen = pen('Econo', 'Blackish', '$5')
            
MourisPen = pen('Matador', 'Green', '$10')

KalidPen = pen('Matador', 'Transparent White', '$50')

print(MyPen.brand, MyPen.color, MyPen.price)
print(MourisPen.brand, MourisPen.color, MourisPen.price)
print(KalidPen.brand, KalidPen.color, KalidPen.price)