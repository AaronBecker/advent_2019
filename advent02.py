
def module_fuel(mass):
    fuel_total = 0
    fuel = mass // 3 - 2
    while fuel > 0:
        fuel_total += fuel
        fuel = fuel // 3 - 2
    return fuel_total

def advent02(input):
    return sum(module_fuel(int(m)) for m in input.strip().split('\n'))
