class laser:

    def __init__(self, name, wavelength, password):
        self.name = name
        self.wavelength = wavelength
        self.password = password

    def pulse(self, frequency):
        print(f"Laser pulsing at {frequency}Hz")

    def continuous(self):
        print("Turning on laser")

    def shutdown(self):
        print("Shutting down. Password will be required to turn back on.")

    def switch_on(self):
        check = input("Input password")
        if check == self.password:
            print("Switching on Laser")
        else:
            print("Wrong password. Laser deactivated.")