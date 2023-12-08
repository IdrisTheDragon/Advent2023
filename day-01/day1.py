import time

start =time.time()

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

print('==P1==')
# P1
with open('input.txt',"r") as infile:
    sum = 0
    for l in infile:
        l = l.strip()
        #print(l)
        l = [c for c in l if c.isdigit()]
        sum += int(l[0] + l[-1])
    print(sum)
end = time.time()
print("P1",end-start)
start =time.time()
print('==P2==')
# P2
digits = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
with open('input.txt',"r") as infile:
    sum = 0
    for l in infile:
        l = l.strip()
        l1 = l
        #print(l)
        i=0
        while i <= len(l):
            for k,v in digits.items():
                if l[i:].startswith(k):
                    l = l.replace(k,str(v),1)
            i +=1
        #print(l)
        l = [c for c in l if c.isdigit()]
        v1 = l[0]
        
        l = l1
        i=len(l)
        while i >= 0:
            for k,v in digits.items():
                if l[i:].startswith(k):
                    l = rreplace(l,k,str(v),1)
            i -=1
        #print(l)
        l = [c for c in l if c.isdigit()]
        v2 = l[-1]
        v = int(v1 + v2)

        #print(v1,v2,v)
        sum += v
    print(sum)
end = time.time()
print("P2",end-start)
start =time.time()
print('==P2 ALT==')
# P2
digits = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
def finder_right(l):
    i=0
    while i <= len(l):
        if l[i].isdigit():
            return l[i]
        for k,v in digits.items():
            if l[i:].startswith(k):
                return str(v)
        i +=1
    raise Error("missing digit")

def finder_left(l):
    i=len(l)-1
    while i >= 0:
        if l[i].isdigit():
            return l[i]
        for k,v in digits.items():
            if l[i:].startswith(k):
                return str(v)
        i -=1
    raise Error("missing digit")

with open('input.txt',"r") as infile:
    sum = 0
    for l in infile:
        l = l.strip()
        
        v1 = finder_right(l)
        v2 = finder_left(l)
        v = int(v1 + v2)

        #print(v1,v2,v)
        sum += v
    print(sum)
end = time.time()
print("P2 ALT",end-start,"s")
