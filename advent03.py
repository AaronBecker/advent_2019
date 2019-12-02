
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

def advent03(input):
    intcode = [int(x) for x in input.strip().split(',')]
    intcode[1] = 12
    intcode[2] = 2
    op = 0
    while apply_op(op, intcode):
        op += 4
    return intcode[0]
