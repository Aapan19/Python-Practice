class phone:
    price = 20000
    color = 'blue'
    brand = 'xiaomi'
    features = ['camera', 'speaker', 'heamer']

    def call(self):
        print('calling one person ........ ')
    def send_sms(self, phone, sms):
        text = f'sending sms to: {phone} and message is {sms}'
        return text

my_phone = phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(101742, 'I missed to miss you')
print(result)