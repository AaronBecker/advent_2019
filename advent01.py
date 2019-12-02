
def advent01(input):
    return sum(int(m)//3 - 2 for m in input.strip().split('\n'))
