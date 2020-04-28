#reamove leading zeros of a number
def remove_0(n):
    l = len(n)
    for i in range(l-1,-1,-1):
        if n[i]==0:
            n.pop(i)
        else:
            return n
    return [0]

#convert user input string into list
def str_to_list(s):

    nw=s.split()
    nw = nw[::-1]
    ni = []
    for i in nw:
        ni.append(int(i))
    return ni

#check for valid number
def is_valid(n,g):
    if g<5:
        return False
    for i in n:
        if(i>=g):
            return False
    return True

def D(a,g):
    return (a%g)

#substraction of two numbers in list form
def minus(n,m,g):
    ln = len(n)
    lm = len(m)
    m += [0]*(ln-lm)
    ans = [0]*ln
    for i in range(0,ln):
        ans[i]=n[i]-m[i]
    for i in range(0,ln):
        if(ans[i]<0):
            ans[i]+=g
            ans[i+1]-=1
    ans = remove_0(ans)
    return ans

#check first inmber is >= second number or not, in list form.
def gt_eq(n,m):
    if len(n)>len(m):
        return True
    elif len(n)<len(m):
        return False
    else:
        l = len(n)
        for i in range(l-1,-1,-1):
            if(n[i]>m[i]):
                return True
            elif n[i]<m[i]:
                return False
        return True

#Addition of two numbers in list form
def add(n,m,g):
    ln = len(n)
    lm = len(m)
    m += [0] * (ln - lm)
    ans = [0] * (ln+1)
    for i in range(0, ln):
        ans[i] = n[i] + m[i]
    for i in range(0, ln):
        if (ans[i] >= g):
            ans[i] -= g
            ans[i + 1] += 1
    ans = remove_0(ans)
    return ans

