class coffeemachine:

    def __init__(self, name):
        self.name = name

    def heat(self, temp):
        print(f"Heating water to {temp} degrees")

    def latte(self, temp, froth):
        print(f"Heating milk to {temp} and frothing to {froth}%")

    def timer(self, delay):
        print(f"Setting timer delay to {delay} hours")