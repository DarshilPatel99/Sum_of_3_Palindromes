from l_is_1_2_3_4 import *
from algos import *
from Initial_configuration import *
from functions import *

#for length of number is 5(5 digit in number)
def len5(n,g):
    p1 = []
    p2 = []
    p3 = []

#page no 30
    if n[4] != 1:#use algorithm 1
        p = list(startingpoint(n, 5, g))
        ans = list(algo1(n, p, g, 5))
        return ans

    else:#first digit(n[4]) is 1
        m = [1,n[3],0,n[3],1]
        if gt_eq(n,m):
            sub = minus(n,m,g)

            #length of sub is 3
            if len(sub)==3 and sub != [1,0,2]:#page no. 30 lemma 4.5 case (i)
                p1 = m
                p2,p3 = len3(sub,g)
                return p1,p2,p3
            if sub == [1,0,2]:#page no. 30 lemma 4.5 case (ii)
                p1 = [1,n[3],1,n[3],1]
                p2 = [1,0,1]
                return p1,p2

            # length of sub is 2
            if len(sub)==2 and sub[1]!=sub[0]+1:#page no. 30 lemma 4.5 case (i)
                p1 = m
                p2,p3 = len2(sub,g)
                return p1,p2,p3
            if len(sub) == 2 and sub[1] == sub[0] + 1:
                if n[3]!=0:#page no. 30 lemma 4.5 case (iii)
                    if sub[0]+1+n[3]<= g-1:#a
                        p1 = [1,n[3]-1,1,n[3]-1,1]
                        p2 = [g-1,sub[1],g-1]
                        p3 = [sub[1]]
                        return p1,p2,p3
#page no 31
                    if n[3]+1+sub[0]==g + n[1]:#b
                        p1 = [1,n[3]-1,1,n[3]-1,1]
                        p2 = [g-1,sub[1],g-1]
                        p3 = [sub[1]]
                        return p1,p2,p3
                if n[3]==0:#page no. 30 lemma 4.5 case (iv)
                    p1 = [g-1,g-1,g-1,g-1]
                    p2 = [sub[1],sub[1]]
                    p3 = [1]
                    return p1,p2,p3

            # length of sub is 1
            if len(sub)==1:
                p1 = m
                p2 = sub
                return p1,p2

        else:
            if n[3]==0:#page no. 30 lemma 4.5 case (v)
                p1 = [g-1,g-1,g-1,g-1]
                p2 = [1]
                return p1,p2

            m = [1,n[3]-1,g-1,n[3]-1,1]
            sub = minus(n,m,g)
            if n[3]!=0 and n[3] + sub[0] == g + n[1]:#page no. 30 lemma 4.5 case (vii)
                p1 = [1,n[3]-1,g-2,n[3]-1,1]
                p2 = [1,sub[1],1]
                p3 = [sub[0]-1]
                return p1,p2,p3

def len6(n,g):
    p1 = []
    p2 = []
    p3 = []
    p = []
    c = [0,0,0,0,0,0]

#page no 31-32
    if n[5]!=1:#algorithm 2
        #exctra adjustment as shown in page no 32 is implemented in algorithm 2
        p = list(startingpoint(n, 6, g))
        ans = list(algo2(n,p,g,6))
        return ans
#page no 33
    else:#first digit(n[5]) is 1
        p1 = [0]*5
        p2 = [0]*5
        p3 = [0]*3
        z1 = D(n[0]-n[4]+1,g)
        t = D(n[0]-n[4]+2,g)

        if z1!=0 and t !=0:#page no.33 case (i)
            p1[0] = p1[4]= g-1
            p2[0] = p2[4] = n[4]
            while (p2[0] <= 0):
                p1[0] = p1[4] = p1[0]-1
                p2[0] = p2[4] = p2[0]+1
            p3[0] = p3[2] = z1
            c[1] = (p1[0]+p2[0]+p3[0]-n[0])//g
            p1[1] = p1[3] = g-1
            p2[1] = p2[3] = n[3]
            while (p2[1] < 0):
                p1[1] = p1[3] = p1[1] - 1
                p2[1] = p2[3] = p2[3] + 1
            p3[1] = D(n[1]-p1[1]-p2[1]-c[1],g)
            c[2] = (c[1]+p1[1]+p2[1]+p3[1]-n[1])//g
            p1[2] = g - c[2] - z1
            p2[2] = n[2]
            while(p1[2]<0):
                p1[2]+=1
                p2[2]-=1
            return p1, p2, p3

        if t == 0 and n[2]!=0: #page no.33 case (ii)
            p1[0] = p1[4] = g - 1
            p2[0] = p2[4] = n[4]
            while (p2[0] <= 0):
                p1[0] = p1[4] = p1[0]-1
                p2[0] = p2[4] = p2[0]+1
            p3[0] = p3[2] = g-1
            c[1] = (p1[0]+p2[0]+p3[0]-n[0])//g
            p1[1] = p1[3] = g - 1
            p2[1] = p2[3] = n[3]
            while (p2[1] < 0):
                p1[1] = p1[3] = p1[1] - 1
                p2[1] = p2[3] = p2[3] + 1
            p3[1] = D(n[1] - p1[1] - p2[1] - c[1],g)
            c[2] = (c[1] + p1[1] + p2[1] + p3[1] - n[1]) // g
            p1[2] = g - c[2] - p3[0]
            p2[2] = n[2]
            while (p1[2] < 0):
                p1[2] += 1
                p2[2] -= 1
            return p1, p2, p3

#page no 34
        if t == 0 and n[2]==0: #page no.34 case (iii)
            p3 = [0]*4
            if n[4]==0 and n[0]==g-2:#a
                p1[0]=p1[4]=g-2
                p2[0]=p2[4]=1
                p3[0]=p3[3]=g-1
                c[1]=(p1[0]+p2[0]+p3[0]-n[0])//g
                p1[1]=p1[3]=0
                p2[1]=p2[3]=n[3]
                p3[1]=p3[2]=D(n[1]-p1[1]-p2[1]-c[1],g)
                c[2] = (p1[1]+p2[1]+p3[1]+c[1]-n[1])//g
                p1[2]=0
                p2[2]=g-c[2]-p3[2]
                return p1, p2, p3

            if n[4] == 1 and n[0] == g-1:#b
                p1[0] = p1[4] = g - 1
                p2[0] = p2[4] = 1
                p3[0] = p3[3] = g - 1
                c[1] = (p1[0] + p2[0] + p3[0] - n[0]) // g
                p1[1] = p1[3] = 0
                p2[1] = p2[3] = n[3]
                p3[1] = p3[2] = D(n[1] - p1[1] - p2[1] - c[1],g)
                c[2] = (p1[1] + p2[1] + p3[1] + c[1] - n[1]) // g
                p1[2] = 0
                p2[2] = g - c[2] - p3[2]
                return p1, p2, p3

            if n[4] == 2 and n[0] == 0:#c
                p1[0] = p1[4] = g - 1
                p2[0] = p2[4] = 2
                p3[0] = p3[3] = g - 1
                c[1] = (p1[0] + p2[0] + p3[0] - n[0]) // g
                p1[1] = p1[3] = 0
                p2[1] = p2[3] = n[3]
                p3[1] = p3[2] = D(n[1] - p1[1] - p2[1] - c[1],g)
                c[2] = (p1[1] + p2[1] + p3[1] + c[1] - n[1]) // g
                if c[2]!=2 :
                    p1[2] = 0
                    p2[2] = g - c[2] - p3[2]
                else:
                    P1 = [1,2,g-2,g-2,2,1]
                    p2 = [1,g-3,1]
                    p3 = [g-2]
                return p1, p2, p3

#page no 35
            if n[4]>=3:#d
                c[4]=(D(n[3]-1,g)+1-n[3])//g
                z = D(n[1]-n[3]-1+c[4],g)
                c[2] = (2-c[4]+D(n[3]-1,g)+z-n[1])//g
                p1 = [1,1-c[4],0,0,1-c[4],1]
                p2 = [n[4]-1,D(n[3]-1,g),2-c[2],D(n[3]-1,g),n[4]-1]
                p3 = [g-2,z,g-2]
                return p1, p2, p3

        if z1 == 0 and n[3]!=0:#page no.35 case (iv)
            if n[4]!=g-1:#a
                p1[0]=p1[4]=g-1
                p2[0]=p2[4]=n[4]+1
                p3[0]=p3[2]=g-1
                c[1] = (p1[0]+p2[0]+p3[0]-n[0])//g
                p1[1]=p1[3]=0
                p2[1]=p2[3]=n[3]-1
                p3[1] = D(n[1] - p1[1] - p2[1] - c[1],g)
                c[2] = (p1[1]+p2[1]+p3[1]+c[1]-n[1])//g
                p1[2]=0
                p2[2]=1+n[2]-c[2]
                while p2[2]>=g:
                    p2[2] -=1
                    p1[2] +=1
                return p1, p2, p3

            if n[4]==g-1:#b
                y=1
                m=0
                x = D(n[3]-y,g)
                c1 = (3+y+D(n[1]-3-y,g)-n[1])//g
                if c1==1 and x == g-1 and n[2]==0:
                    m = 1
                c2 = (x+D(n[2]-x-1-c1+m,g)+c1+1-n[2])//g
                c3 = (x+(y-c2)+c2-n[3])//g
                p1 = [1,3-c3,x-m,x-m,3-c3,1]
                p2 = [g-4,y-c2+m,D(n[2]-x-1-c1+m,g),y-c2+m,g-4]
                p3 = [1,D(n[1]-3-y,g)+(c2-m)+c3,1]
                return p1, p2, p3

#page no. 36
        if z1==0 and n[3]==0:#page no.36 case (v)

            if n[4]==0:#a
                if n[2]!=0:#1st IF
                    p1 = [1,0,0,0,0,1]
                    n1 = [g-2,n[1],n[2]]
                    p2,p3 = list(len3(n1,g))
                    return p1, p2, p3
                if n[2]==0 and n[1]!=0 and n[1]!=g-1:#2nd IF
                    p1 = [1,0,0,0,0,1]
                    if(n[1]==1):
                        n1 = [g-1]
                        p2 = list(len1(n1,g))
                        return p1, p2
                    else:
                        n1 = [g-1,n[1]-1]
                        p2,p3 = list(len2(n1,g))
                        return p1, p2, p3
                if n[2]==0 and n[1]==0:#3rd IF
                    p1 = [1,0,0,0,0,1]
                    p2 = [g-2]
                    return p1, p2
                if n[2]==0 and n[1]==g-1:#4th IF
                    p1 = [g-1,0,1,0,g-1]
                    p2 = [g-1,g-2,g-2,g-1]
                    p3 = [1,0,1]
                    return p1, p2, p3

            if n[4]==1:#b
                if n[2]>=2 or (n[2]==1 and n[1]!=0 and n[1]!=1):#1st IF
                    p1 = [1,1,0,0,1,1]
                    n1 = minus(n,p1,g)
                    p2,p3 = list(len3(n1,g))
                    return p1, p2, p3
                if n[2]==1 and n[1]==0:#2nd IF
                    p1 = [1,0,g-1,g-1,0,1]
                    p2 = [1,g-1,1]
                    p3 = [g-2]
                    return p1, p2, p3
#page no. 37
                if n[2]==1 and n[1]==1:#3rd IF
                    p1 = [1,1,0,0,1,1]
                    p2 = [g-1,g-1]
                    return p1, p2
                if n[2]==0 and n[1]>=2:#4th IF
                    p1 = [1,1,0,0,1,1]
                    p2 = [n[1]-2,n[1]-2]
                    p3 = [g-n[1]+1]
                    return p1, p2, p3
                if n[2]==0 and n[1]==1:#5th IF
                    p1 = [1,0,0,0,0,1]
                    p2 = [1,0,0,0,1]
                    p3 = [g-2]
                    return p1, p2, p3
                if n[2]==0 and n[1]==0:#6th IF
                    p1 = [1,0,0,0,0,1]
                    p2 = [g-1,g-1,g-1,g-1]
                    return p1, p2

            if n[4] == 2:#c
                if n[2]>=2 or (n[2]==1 and n[1]!=0 and n[1]!=1):#1st IF
                    p1 = [1, 2, 0, 0, 2, 1]
                    n1 = minus(n, p1, g)
                    p2, p3 = list(len3(n1, g))
                    return p1, p2, p3
                if n[2]==1 and n[1]==0:#2nd IF
                    p1 = [1,1,g-1,g-1,1,1]
                    p2 = [1,g-2,1]
                    p3 = [g-1]
                    return p1, p2, p3
                if n[2]==1 and n[1]==1:#3rd IF
                    p1 = [1, 1, g - 1, g - 1, 1, 1]
                    p2 = [1, g - 1, 1]
                    p3 = [g - 1]
                    return p1, p2, p3
#page no. 38
                if n[2]==0 and n[1]>=4:#4th IF but n[1]!=3
                    p1 = [1,2,0,0,2,1]
                    p2 = [n[1]-3,n[1]-3]
                    p3 = [g-n[1]+3]
                    return p1, p2, p3
                if n[2]==0 and n[1]==3:#4th IF but n[1]==3
                    p1 = [1,2,0,0,2,1]
                    p2 = [1]
                    p3 = [g-1]
                    return p1, p2, p3
                if n[2]==0 and n[1]==2:#5th IF
                    p1 = [1,1,g-1,g-1,1,1]
                    p2 = [1,0,1]
                    p3 = [g-1]
                    return p1, p2, p3
                if n[2]==0 and n[1]==1:#6th IF
                    p1 = [1,0,0,0,0,1]
                    p2 = [2,0,0,0,2]
                    p3 = [g-2]
                    return p1, p2, p3
                if n[2]==0 and n[1]==0:#7th IF
                    p1 = [1,1,g-1,g-1,1,1]
                    p2 = [g-2,g-2]
                    p3 =[2]
                    return p1, p2, p3
            if n[4]==3 and n[0]==2:#d
                y = 1
                c1 = (2+y+D(n[1]-1-y,g)-n[1])//g
                c2 = (g-y-1+D(n[2]+y+2,g)+g-1-n[2])//g
                p1 = [1,0,g-y-1-c1,g-y-1-c1,0,1]
                p2 = [2,y-c2+1+c1,D(n[2]+y+2,g),y-c2+1+c1,2]
                p3 = [g-1,D(n[1]-1-y,g)+(c2-1)-c1,g-1]
                return p1, p2, p3
#page no. 39
            if n[4]>=4:#e
                y=1
                c1 = (1+y+D(n[1]-1-y,g)-n[1])//g
                c2 = (g-y+1+D(n[2]+y-1,g)-n[2])//g
                p1 = [1,2,g-y-c1,g-y-c1,2,1]
                p2 = [n[4]-3,y-c2+c1,D(n[2]+y-1,g),y-c2+c1,n[4]-3]
                p3 = [1,D(n[1]-2-y,g)+c2-c1,1]
                return p1,p2,p3