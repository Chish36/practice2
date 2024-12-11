from Lab import calculator, laser, mirror

laser = laser.laser("Red", 600, "openflexure")
calculator = calculator.calculator("Model 620")
mirror = mirror.mirror("mirror")

mirror.rotate("x", 63)
laser.pulse(60)
calculator.addition(63,7)
laser.shutdown()
laser.switch_on()