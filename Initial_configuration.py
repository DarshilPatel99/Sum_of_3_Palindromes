from functions import *

#page no. 3
#page no. 4
#page no. 5
#page no. 6

def startingpoint(ni,l,g):
    #initialization
    p1 = [None]*l
    p2 = [None]*(l-1)
    p3 = [None]*(l-2)
    type = ''
    if ni[l-2] >= 3 :
        z1 = D(ni[0] - ni[l - 1] - ni[l - 2] + 1,g)
        if (z1 != 0) :#a1
            p1[l-1]=p1[0]=ni[l-1]
            p2[l-2]=p2[0]=ni[l-2]-1
            p3[l-3]=p3[0]=z1
            type = 'A1'
        if (z1 == 0) :#a2
            p1[l-1]=p1[0]=ni[l-1]
            p2[l-2]=p2[0]=ni[l-2]-2
            p3[l-3]=p3[0]=1
            type = 'A2'
    if ni[l-2]<=2 :
        if ni[l-1]!=1:
            z1 = D(ni[0] - ni[l-1] + 2,g)
            if(z1 != 0):#a3
                p1[l-1] = p1[0] = ni[l-1]-1
                p2[l-2] = p2[0] = g-1
                p3[l-3] = p3[0] = z1
                type = 'A3'
            if z1 == 0 :#a4
                p1[l - 1] = p1[0] = ni[l - 1]-1
                p2[l - 2] = p2[0] = g - 2
                p3[l - 3] = p3[0] = 1
                type = 'A4'

        if ni[l-1]==1 :
            z1 = D(ni[0]-ni[l-3],g)
            if z1 != 0 :
                if ni[l-3]>=4:#b1
                    p1[l-1]=p1[0]=1
                    p2[l-2]=p3[l-3]=0
                    p1[l-2]=p1[1]=ni[l-2]
                    p2[l-3]=p2[0]=ni[l-3]-1
                    p3[l-4]=p3[0]=z1
                    type = 'B1'
                if ni[l-3]<=3 and ni[l-2]==0 :#a5
                    p1[l-1]=p2[l-2]=p3[l-3]=0
                    p1[l-2]=p1[0] = g-1
                    p2[l-3]=p2[0] = ni[l-3]+1
                    p3[l-4]=p3[0] = z1
                    type = 'A5'
            if z1==0:
                if ni[l-3]>=3:#b2
                    p1[l-1]=p1[0]= 1
                    p2[l-2]=p3[l-3]= 0
                    p1[l-2]=p1[1]=ni[l-2]
                    p2[l-3]=p2[0]=ni[l-3]-2
                    p3[l-4]=p3[0]=1
                    type = 'B2'
                if ni[l-3]<=2 and ni[l-2]==0 :#a6
                    p1[l-1]=p2[l-2]=p3[l-3]=0
                    p1[l-2]=p1[0] = g-1
                    p2[l-3]=p2[0] = ni[l-3]+2
                    p3[l-4]=p3[0] = g-1
                    type = 'A6'

            if ni[l-2]!=0 :
                if ni[0]==0:
                    if ni[l-3]<=1:#b3
                        p1[l - 1] = p1[0] = 1
                        p2[l - 2] = p3[l - 3] = 0
                        p1[l - 2] = p1[1] = str(ni[l-2]-1)
                        p2[l - 3] = p2[0] = str(g-2)
                        p3[l - 4] = p3[0] = 1
                        type = 'B3'
                    if ni[l-3]<=3:#b4
                        p1[l - 1] = p1[0] = 1
                        p2[l - 2] = p3[l - 3] = 0
                        p1[l - 2] = p1[1] = ni[l - 2]
                        p2[l - 3] = p2[0] = 1
                        p3[l - 4] = p3[0] = g-2
                        type = 'B4'

                if ni[l-3]<=2 and ni[0] != 0 : #b5
                    p1[l - 1] = p1[0] = 1
                    p2[l - 2] = p3[l - 3] = 0
                    p1[l - 2] = p1[1] = ni[l - 2] - 1
                    p2[l - 3] = p2[0] = g - 1
                    p3[l - 4] = p3[0] = ni[0]
                    type = 'B5'

                if ni[l-3]==3 :
                    if ni[0] != 3 :#b6
                        p1[l - 1] = p1[0] = 1
                        p2[l - 2] = p3[l - 3] = 0
                        p1[l - 2] = p1[1] = ni[l-2]
                        p2[l - 3] = p2[0] = 2
                        p3[l - 4] = p3[0] = D(ni[0]-3,g)
                        type = 'B6'
                    if ni[0] == 3:#b7
                        p1[l - 1] = p1[0] = 1
                        p2[l - 2] = p3[l - 3] = 0
                        p1[l - 2] = p1[1] = ni[l-2]
                        p2[l - 3] = p2[0] = 1
                        p3[l - 4] = p3[0] = 1
                        type = 'B7'

    #remove leading zeros
    p1 = remove_0(p1)
    p2 = remove_0(p2)
    p3 = remove_0(p3)

    return p1,p2,p3,type
