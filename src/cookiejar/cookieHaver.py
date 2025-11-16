import cookiejar

class CookieHaver:
    def __init__(self, name):
        self.name = name
        self.jar = cookiejar.CookieJar(0, 0, 0)

customer = CookieHaver('Alice')
customer.jar.cChip += 10
print(f'{customer.name} has {customer.jar.value()} chips in their cookies.')
print(f'{customer.name}\'s cookies weigh {customer.jar.weightInGrams()} grams.')