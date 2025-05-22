class Phone:
    manufacture = 'china'

    #Constructor 
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.pricr = price

    def send_sms(self, number, sms):
        text = f'sending a message to {number} and the messafe is {sms}'
        print(text)

myPhone = Phone('Ripon video', 'symphony', 15000)
print(myPhone.owner, myPhone.brand, myPhone.pricr)

herPhone = Phone('sadia', 'iPhone', 120000)
print(herPhone.owner, herPhone.brand, herPhone.pricr)

myPhone.send_sms(12345, "lorem ispum")