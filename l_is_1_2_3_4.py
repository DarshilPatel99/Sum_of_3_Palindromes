from functions import *

#page no 28
#for length of number is 1(1 digit in number)
def len1(n,g):
    p1=[]
    p1 = n
    return p1

#for length of number is 2(2 digit in number)
def len2(n,g):
    p1 = []
    p2 = []
    p3 = []
    if n[1] <= n[0]:
        p1 = [n[1],n[1]]
        p2 = [n[0]-n[1]]
        return p1,p2

    if n[1] > n[0] + 1:
        p1 = [n[1]-1, n[1]-1]
        p2 = [g + 1 + n[0] - n[1]]
        return p1, p2

    if n[1] == n[0] + 1 and n[0] >= 1:
        p1 = [n[0],n[0]]
        p2 = [g-1]
        p3 = [1]
        return p1, p2, p3

    if n[1] == 1 and n[0] == 0:
        p1 = [g-1]
        p2 = [1]
        return p1, p2

#page no. 29
#for length of number is 3(3 digit in number)
def len3(n,g):
    p1 = []
    p2 = []
    p3 = []
    if n[2] <= n[0]:
        p1 = [n[2],n[1],n[2]]
        p2 = [n[0]-n[2]]
        return p1, p2

    if n[2] >= n[0] + 1 and n[1] != 0:
        p1 = [n[2], n[1]-1, n[2]]
        p2 = [g + n[0] - n[2]]
        return p1, p2

    if n[2] >= n[0] + 1 and n[1] == 0 and D(n[2]-n[0]-1,g) != 0:
        p1 = [n[2]-1, g - 1, n[2]-1]
        p2 = [g + 1 + n[0] - n[2]]
        return p1, p2

    if n[2]>=3 and n[1]==0 and n[0] == n[2]-1:
        p1 = [n[2] - 2, g - 2, n[2] - 2]
        p2 = [1,1,1]
        return p1, p2

    if n[2]==2 and n[1]==0 and n[0] == 1:
        p1 = [1,0,1]
        p2 = [g-1,g-1]
        p3 = [1]
        return p1, p2, p3

    if n[2]==1 and n[1] == 0 and n[0] == 0:
        p1 = [g-1,g-1]
        p2 = [1]
        return p1, p2

#for length of number is 4(4 digit in number)
def len4(n,g):
    p1 = []
    p2 = []
    p3 = []
    m = [n[3],0,0,n[3]]
    if gt_eq(n,m) :

        #sub = n - m
        sub = minus(n, m, g)

        #sub is length of 3
        if len(sub)==3 and sub != [1,0,2]: #page no. 29 lemma 4.4 case (i)
            p1 = m
            p2,p3 = len3(sub,g)
            return p1,p2,p3
        if sub == [1, 0, 2]:#page no. 29 lemma 4.4 case (ii)
            if n[3]!=1 and n[3]!=g-1:
                p1 = [n[3]-1,g-1,g-1,n[3]-1]
                p2 = [2,1,2]
                return p1,p2
            if n[3]==1:
                p1 = [1,1,1,1]
                p2 = [g-2,g-2]
                p3 = [3]
                return p1,p2,p3
            if n[3]==g-1:
                p1 = [g-1,1,1,g-1]
                p2 = [g-2,g-2]
                p3 = [3]
                return p1,p2,p3

        # sub is length of 2
        if len(sub) == 2 and sub[1]!=sub[0]+1:#page no. 29 lemma 4.4 case (i)
            p1 = m
            p2, p3 = len2(sub, g)
            return p1, p2, p3
        if len(sub) == 2 and sub[1]==sub[0]+1:#page no. 29 lemma 4.4 case (iii)
            if n[3]+sub[0]==n[0]:#a
                if n[3]!=1:
                    p1 = [n[3]-1,g-2,g-2,n[3]-1]
                    p2 = [1,3,1]
                    p3 = [sub[0],sub[0]]
                    return p1,p2,p3
                if n[3]==1:
                    p1 = [g-1,g-1,g-1]
                    p2 = [sub[1],sub[1]]
                    p3 = [1]
                    return p1, p2, p3
            if n[3]+sub[0] == g + n[0]:#b
                p1 = [n[3]-1,g-2,g-2,n[3]-1]
                p2 = [1,3,1]
                p3 = [n[0],n[0]]
                return p1, p2, p3

        # sub is length of 1
        if len(sub)==1:
            p1 = m
            p2 = sub
            return p1, p2

    if n[1]==0 and n[2]==0 and n[0]<=n[3]-1 and n[3]!=1:#page no. 30 lemma 4.4 case (iv)
        p1 = [n[3]-1,g-1,g-1,n[3]-1]
        p2 = [g + n[0]-n[3]]
        p3 = [1]
        return p1, p2, p3

    if n == [0,0,0,1]:#page no. 30 lemma 4.4 case (v)
        p1 = [g-1,g-1,g-1]
        p2 = [1]
        return p1, p2