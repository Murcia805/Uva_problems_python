from sys import stdin

def recursion_ciclo(Base1, Base2,rest,q):
    resul = ""
    while True :
        D = [Base1[0] + Base2[0], Base1[1] + Base2[1]]
        #M = D[0] / D[1]
        if D == q:
            break
        elif D[1]*q[0] > q[1]*D[0]:
            resul = resul + "R"
            Base1 = D
        elif D[1]*q[0] < q[1]*D[0]:
            resul = resul + "L"
            Base2 = D
        else:
            break

    return resul

def recursion(Base1, Base2,rest,q):
    D = [Base1[0]+Base2[0],Base1[1]+Base2[1]]
    M = D[0]/D[1]
    if D == q :
        return ''
    elif M < rest :
        return 'R' + recursion(D,Base2,rest,q)
    elif M > rest:
        return 'L' + recursion(Base1,D,rest,q)
    else:
        return ''

def solve(target):
    ans = ""
    rest = target[0]/target[1]
    q = target
    ans = recursion_ciclo([0,1], [1,0],rest,q)
    return ans

def main():
    target = [int(x) for x in stdin.readline().strip().split()]
    #print(lcm(target[0],target[1]))
    while target[0]!=1 or target[1]!=1:
        print(solve(target))
        target = [int(x) for x in stdin.readline().strip().split()]

main()