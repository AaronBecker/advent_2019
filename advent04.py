import copy

def apply_op(n, context):
    if context[n] == 99:
        return False
    elif context[n] == 1:
        context[context[n+3]] = context[context[n+1]] + context[context[n+2]]
    elif context[n] == 2:
        context[context[n+3]] = context[context[n+1]] * context[context[n+2]]
    else:
        raise Exception('Invalid opcode in position %d: %d' % (n, context[n]))
    return True

def result(x, y, intcode):
    intcode[1] = x
    intcode[2] = y
    op = 0
    try:
        while apply_op(op, intcode):
            op += 4
        return intcode[0]
    except:
        return -1

    
def advent04(input):
    intcode = [int(x) for x in input.strip().split(',')]
    op = 0
    for noun in range(len(intcode)):
        for verb in range(len(intcode)):
            if result(noun, verb, copy.deepcopy(intcode)) == 19690720:
                print("%d, %d" % (noun, verb))
                return 100 * noun + verb
    return -1
