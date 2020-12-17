input = list(int(line.strip()) for line in open('../input.txt'))

def joltage():
    input.append(0)
    input.sort()
    joltageJumps = {1:0,2:0,3:0}
    for jolt, nextJolt in zip(input,input[1:]):
        jump = nextJolt-jolt
        if jump <=3:
            joltageJumps[jump] +=1
    return joltageJumps[1] * (joltageJumps[3]+1)

print(joltage())