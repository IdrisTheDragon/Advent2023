from functools import lru_cache


@lru_cache(maxsize = 128)
def place_sequence(pattern:str,sequence:str):
    # END cases
    if len(sequence) == 0 and len(pattern) == 0:
        # both empty is valid
        return 1
    if len(sequence) == 0:
        # if sequence empty remaining pattern can't contain any '#'
        return 1 if all( p in ['.','?'] for p in pattern) else 0
    if len(pattern) == 0:
        # empty pattern but sequence left is invalid
        return 0

    sum = 0
    if pattern[0] in ['.','?']:
        # go next level down
        sum += place_sequence(pattern[1:],sequence)
    if pattern[0] in ['#','?']:
        # parse next sequence count
        if ',' in sequence:
            (s,sequence) = sequence.split(',',1)
            s = int(s)
        else:
            s = int(sequence)
            sequence = ''
        # iterate until run out of s or more '#'
        while s > 0 and len(pattern) > 0 and pattern[0] in ['#','?']:
            pattern = pattern[1:]
            s-=1
        if s == 0:
            if len(pattern) == 0:
                sum += place_sequence(pattern,sequence)
            elif len(pattern) > 0 and pattern[0] in ['.','?']:
                pattern = pattern[1:]
                sum += place_sequence(pattern,sequence)
        # discard if s is not zero or more '#' with no space
    return sum

with open("input.txt","r") as infile:
    sum = 0
    for l in infile:
        (pattern,sequence) = l.strip().split(' ')
        s = place_sequence(pattern,sequence)
        #print(s)
        sum += s
print("==P1==")
print(sum)


with open("input.txt","r") as infile:
    sum = 0
    for l in infile:
        (pattern,sequence) = l.strip().split(' ')
        sequence = ','.join([sequence,sequence,sequence,sequence,sequence])
        pattern = '?'.join([pattern, pattern, pattern, pattern, pattern])
        s = place_sequence(pattern,sequence)
        #print(s)
        sum += s

print("==P2==")
print(sum)
