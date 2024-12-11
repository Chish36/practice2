from Kitchen import coffee
from Kitchen import fridge

machine_coffee = coffee.coffeemachine(name = "Brewmaster")

machine_coffee.heat(temp=60)

machine_fridge = fridge.fridge(name = "coolMachine")

machine_fridge.defrost()

machine_fridge.temp_adjust(temp=-6)

machine_coffee.defrost()