class fridge:

    def __init__(self, name):
        self.name = name

    def defrost(self):
        print("Beginning defrost cycle")

    def temp_adjust(self, temp):
        print(f"Changing temperature to {temp}")

    def open_door(self):
        print("Open door")
