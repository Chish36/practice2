class calculator:

    def __init__(self, name):
        self.name = name

    def addition(self, int1, int2):
        '''Adds two integers together
        
        input: int1 and int2 must be integers
        returns: Sum of int1 and int2
        '''
        print(f"Answer is {int1 + int2}")

    def subtraction(self, int1, int2):
        print(f"Answer is {int1 - int2}")

    def division(self, int1, int2):
        print(f"Answer is {int1 / int2}")

    def multiplication(self, int1, int2):
        print(f"Answer is {int1 * int2}")