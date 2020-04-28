from functions import *

#page no 7
#algorithm 1
def algo1(ni,p,g,l):

    #step 1
    m = (l-1)//2
    p1 = p[0]
    p2 = p[1]
    p3 = p[2]
    c = [None]*l
    c[0]=0
    c[1] = (p1[0]+p2[0]+p3[0])//g

    #step 2
    if p3[0] < ni[2*m-2]:
        p1[2*m-1]=p1[1]=D(ni[2*m-1]-p2[0],g)#x2
    else :
        p1[2*m-1]=p1[1]=D(ni[2*m-1]-p2[0]-1,g)#x2

    p2[2*m-2]=p2[1] = D(ni[2*m-2]-p3[0]-1,g)#y2
    p3[2*m-3]=p3[1] = D(ni[1] - (p1[1]+ p2[1] + c[1]),g)#z2
    c[2] = (p1[1]+p2[1]+p3[1]+c[1]-ni[1]) // g#c2

    #step 3 to m
    for i in range(3,m+1):
        if p3[i-2] < ni[2 * m - i]:
            p1[2*m-i+1] = p1[i-1] = 1#xi
        else:
            p1[2*m-i+1] = p1[i-1] = 0#xi

        p2[2*m-i] = p2[i-1] = D(ni[2*m-i]-p3[i-2]-1,g)#yi
        p3[2*m-(i+1)] = p3[i-1] = D(ni[i-1]-p1[i-1]-p2[i-1]-c[i-1],g)#zi
        c[i] = (p1[i-1]+p2[i-1]+p3[i-1]+c[i-1]-ni[i-1])//g#ci

# page no 11

    #adjustment steps
    if c[m] == 1:#I.1
        p1[m]=0
    elif c[m]==0:#I.2
        p1[m]=1
    else:#I.3
        p1[m]=1
        p2[m-1]=p2[m]=p2[m]-1
        p3[m-1]=0

    return p1,p2,p3

#page no 13
#algorithm 2
def algo2(ni,p,g,l) :

    #step 1
    m = l//2
    p1 = p[0]
    p2 = p[1]
    p3 = p[2]
    c = [None]*l
    c[0]=0
    c[1] = (p1[0]+p2[0]+p3[0])//g

    #step 2
    if p3[0] < ni[2*m-3]:
        p1[2*m-2]=p1[1]=D(ni[2*m-2]-p2[0],g) #x2
    else :
        p1[2*m-2]=p1[1]=D(ni[2*m-2]-p2[0]-1,g) #x2

    p2[2*m-3]=p2[1] = D(ni[2*m-3]-p3[0]-1,g) #y2
    p3[2*m-4]=p3[1] = D(ni[1] - (p1[1]+ p2[1] + c[1]),g) #z2
    c[2] = (p1[1]+p2[1]+p3[1]+c[1]-ni[1]) // g #c2

    #step 3 to m-1
    for i in range(3,m):
        if p3[i-2] < ni[2 * m - i-1]:
            p1[2*m-i] = p1[i-1] = 1 #xi
        else:
            p1[2*m-i] = p1[i-1] = 0 #xi

        p2[2*m-(i+1)] = p2[i-1] = D(ni[2*m-i-1]-p3[i-2]-1,g) #yi
        p3[2*m-(i+2)] = p3[i-1] = D(ni[i-1]-p1[i-1]-p2[i-1]-c[i-1],g) #zi
        c[i] = (p1[i-1]+p2[i-1]+p3[i-1]+c[i-1]-ni[i-1])//g #ci

#page no 14
    #step m
    p1[m] = p1[m-1] = 0 # xm
    p2[m-1] = D(ni[m-1]-p3[m-2]-c[m-1],g) #ym
    c[m] = (c[m-1]+p1[m-1]+p2[m-1]+p3[m-1])//g #cm

#page no 15
    # adjustment steps
    if c[m] == 0 : #II.2

        if p2[m-1]!=0:#II.2.i
            p1[m] = p1[m - 1] = 1
            p2[m - 1] = p2[m-1]-1

        else:#II.2.ii
            if p2[m-2]!=0:#II.2.ii.a
                p1[m] = p1[m - 1] = 1
                p2[m]=p2[m-2] = p2[m-2]-1
                p2[m-1]=g-2
                p3[m-1]=p3[m-2]=p3[m-2]+1
            else:
                if p3[m-2]!=0:#II.2.ii.b
                    p2[m] = p2[m-1] = p2[m-2] = 1
                    p3[m-1]=p3[m-2]=p3[m-2]-1
                else:#II.2.ii.c
#page no 32
                    if l==6 and p3[2]==0 and p3[2]==0:#for len6 as per page no 32-33
                        p1 = p[0]
                        p2 = p[1]
                        p3 = p[2]
                        p1[2] = p1[3] = p2[1] = p2[2] = p2[3] = p3[1] = p3[2] = 0
                        if p3[0] < ni[3]:
                            p1[4] = p1[1] = D(ni[4] - p2[0], g)  #x2
                        else:
                            p1[4] = p1[1] = D(ni[4] - p2[0] - 1, g) #x2

                        if p1[1] != 0:#1st IF
                            p1[4] = p1[1] = p1[1] - 1
                            p1[2] = p1[3] = g - 1
                            p2[1] = p2[2] = p2[3] = 1
                            return p1, p2, p3

                        else:#2nd IF
                            if p1[0] == 1:# case (i)
                                p1 = [2, 0, 0, 0, 0, 2]
                                p2 = [1, 1]
                                p3 = [g - 4]
                                return p1, p2, p3

                            if p1[0] != 1 and p2[0] != g - 1:# case (ii)
                                p1[0] = p1[5] = p1[0] - 1
                                p1[1] = p1[4] = g - 1
                                p2[0] = p2[4] = p2[0] + 1
                                p2[2] = g - 2
                                p3[1] = p3[2] = 1
                                return p1, p2, p3

                            if p1[0] != g - 1 and p2[0] == g - 1 and p3[0] == g - 1:# case (iii)
                                p1[0] = p1[5] = p1[0] + 1
                                p2 = [1, 1]
                                p3 = [g - 4]
                                return p1, p2, p3
#page no 15
                    else:##II.2.ii.c as per page no 15
                        p1[m+1]=p1[m-2]=p1[m-2]-1
                        p1[m]=p1[m-1]=1
                        p2[m-2]=p2[m]=g-1
                        p2[m-1]=g-4
                        p3[m-1]=p3[m-2]=2
                        p3[m+1]=0

    elif c[m]==2:#II.3
        p1[m] = p1[m - 1] = 1
        p2[m] = p2[m - 2] = p2[m - 2] - 1
        p2[m - 1] = g - 2
        p3[m - 1] = p3[m - 2] = 0
    return p1, p2, p3

#page no 17
#algorithm 3
def algo3(ni,p,g,l):

    #step 1
    m = l//2
    p1 = p[0]
    p2 = p[1]
    p3 = p[2]
    c = [None]*l
    c[0]=0
    c[1] = (p1[0]+p2[0]+p3[0])//g

    #step 2
    if p3[0] < ni[2*m-3]:
        p1[2*m-2]=p1[2] = D(ni[2*m-2]-p2[0],g) #x2
    else :
        p1[2*m-2]=p1[2] = D(ni[2*m-2] - p2[0] - 1, g) #x2
    p2[2*m-3] = p2[1] = D(ni[2*m-3]-p3[0]-1,g) #y2
    p3[2*m-4] = p3[1] = D(ni[1]-p1[1]-p2[1]-c[1],g) #z2
    c[2]  = (p1[1]+p2[1]+p3[1]+c[1]-ni[1])//g #c2

    #step 3 to m-1
    for i in range(3,m):
        if(p3[i-2] < ni[2*m-i-1]):
            p1[2*m - i] = p1[i] = 1 #xi
        else:
            p1[2*m - i] = p1[i] = 0 #xi
        p2[2*m-2-(i-1)] = p2[i-1] = D(ni[2*m-(i+1)]-p3[i-2]-1,g) #yi
        p3[2*m-3-(i-1)] = p3[i-1] = D(ni[i-1] - p1[i-1] - p2[i-1] - c[i-1],g) #zi
        c[i] = (p1[i-1]+p2[i-1]+p3[i-1]+c[i-1]-ni[i-1])//g #ci

    #step m
    p1[m] = 0
    p2[m-1] = D(ni[m-1]-p3[m-2]-p1[m-1]-c[m-1],g)
    c[m] = (c[m - 1] + p1[m - 1] + p2[m - 1] + p3[m - 1]) // g

#page no 18
    #adjustment step
    if c[m]==0:#III.2
        p1[m]=1

    elif c[m] == 2:#III.3
        if(p2[m]!=0 and p3[m-1]!= g-1):#III.3.i
            p2[m] = p2[m-2] = p2[m]-1
            p2[m-1] = p2[m-1] - 1
            p3[m-1] = p3[m-2] = p3[m-2]+1
        elif (p2[m] != 0 and p3[m - 1] == g-1):#III.3.ii
            p1[m]=1
            p2[m] = p2[m - 2] = p2[m] - 1
            p3[m - 1] = p3[m - 2] = 0
        elif (p2[m] == 0 and p3[m - 1] != g-1):#III.3.iii
            p1[m+1]=p1[m-1]=p1[m-1]-1
            p2[m] = p2[m - 2] = g - 1
            p2[m - 1] = p2[m - 1] - 1
            p3[m-1] = p3[m-2] = p3[m-1] + 1
        elif (p2[m] == 0 and p3[m - 1] == g-1):#III.3.iv
            p1[m + 1] = p1[m - 1] = p1[m - 1] - 1
            p1[m]=1
            p2[m] = p2[m - 2] = g - 1
            p3[m - 1] = p3[m - 2] = 0

    return p1,p2,p3

#page no.19
#algorithm 4
def algo4(ni,p,g,l):

    #step 1
    m = l//2
    p1 = p[0]
    p2 = p[1]
    p3 = p[2]
    c = [None]*l
    c[0]=0
    c[1] = (p1[0]+p2[0]+p3[0])//g

    #step 2
    if(p3[0]<ni[2*m-4]):
        p1[2*m-3]=p1[2] = D(ni[2*m-3]-p2[0],g)#x2
    else :
        p1[2*m-3]=p1[2] = D(ni[2*m-3]-p2[0]-1, g) #x2
    p2[2*m-4]=p2[1] = D(ni[2*m-4]-p3[0]-1,g) # y2
    p3[2*m-5]=p3[1] = D(ni[1]-p1[1]-p2[1]-c[1],g) #z2
    c[2] = (p1[1]+p2[1]+p3[1]+c[1]-ni[1])//g #c2

    #step 3 to m-2
    for i in range(3,m-1):
        if p3[i-2] < ni[2*m-i-2]:
            p1[2*m-1-i]=p1[i]=1 #xi
        else:
            p1[2*m-1-i]=p1[i]=0#xi
        p2[2*m-3-(i-1)]=p2[i-1]=D(ni[2*m-i-2]-p3[i-2]-1,g) #yi
        p3[2*m-4-(i-1)]=p3[i-1]=D(ni[i-1]-p1[i-1]-p2[i-1]-c[i-1],g) #zi
        c[i]=(p1[i-1]+p2[i-1]+p3[i-1]+c[i-1]-ni[i-1])//g #ci

#page no 20
    #step m-1
    if p3[m-3]<ni[m-1]:
        p1[m]=p1[m-1]=1 #Xm-1
    else:
        p1[m] = p1[m-1] = 0#Xm-1
    p2[m-1]=p2[m-2] = D(ni[m-1]-p3[m-3]-1,g) #Ym-1
    p3[m-2]=D(ni[m-2]-p1[m-2]-p2[m-2]-c[m-2],g) #Zm-1

    c[m-1]=(p1[m-2]+p2[m-2]+p3[m-2]+c[m-2])//g #Cm-1

#page no 21
    #adjustment steps
    if p1[m-1] + c[m-1] ==1: #IV.1
        pass

    elif p1[m-1] + c[m-1] ==0 and p2[m-2]!=g-1: #IV.2
        if p3[m-2]!=0: #IV.2.i
            p2[m-1]=p2[m-2]=p2[m-2]+1
            p3[m-2]=p3[m-2]-1

        elif p3[m-2]==0 and p2[m-3]!=0: #IV.2.ii
            if p2[m-2]!=1 and p3[m-3]!=g-1: #IV.2.ii.a
                p1[m]=p1[m-1]=1
                p2[m]=p2[m-3]=p2[m]-1
                p2[m-1]=p2[m-2]=p2[m-1]-1
                p3[m-1]=p3[m-3]=p3[m-1]+1
                p3[m-2]=1

            elif p2[m - 2] != 1 and p3[m - 3] == g - 1: #IV.2.ii.b
                p1[m] = p1[m - 1] = 2
                p2[m] = p2[m - 3] = p2[m] - 1
                p2[m - 1] = p2[m - 2] = p2[m - 1] - 2
                p3[m - 1] = p3[m - 3] = 0
                p3[m - 2] = 3

            elif p2[m-2] == 1: #IV.2.ii.c
                p1[m] = p1[m - 1] = 1
                p2[m] = p2[m - 3] = p2[m] - 1
                p2[m - 1] = p2[m - 2] = g - 1
                p3[m - 1] = p3[m - 3] = 0
                p3[m - 2] = 3

        elif p3[m-2]==0 and p2[m-3]==0: #IV.2.iii
#page no 22
            if p3[m-3]!=g-1: #IV.2.iii.a
                p1[m]=p1[m-1]=1
                p1[m+1]=p1[m-2]=p1[m+1]-1
                p2[m]=p2[m-3]=g-1
                p2[m-1]=p2[m-2]=p2[m-2]-1
                p3[m-2]=1
                p3[m-1]=p3[m-3]=p3[m-1]+1

            elif p3[m-3] == g-1 and p2[m-2] !=1:#IV.2.iii.b
                p1[m] = p1[m - 1] = 2
                p1[m + 1] = p1[m - 2] = p1[m + 1] - 1
                p2[m] = p2[m - 3] = g - 1
                p2[m - 1] = p2[m - 2] = p2[m - 2] - 2
                p3[m - 2] = 3
                p3[m - 1] = p3[m - 3] = 0

            elif p3[m-3] == g-1 and p2[m-2] ==1 : #IV.2.iii.c
                p1[m] = p1[m - 1] = 1
                p1[m + 1] = p1[m - 2] = p1[m + 1] - 1
                p2[m] = p2[m - 3] = g - 1
                p2[m - 1] = p2[m - 2] = g - 1
                p3[m - 2] = 3
                p3[m - 1] = p3[m - 3] = 0

    elif p1[m-1] + c[m-1] ==0 and p2[m-2]==g-1: #IV.3
        p1[m]=p1[m-1]=1
        p2[m-1]=p2[m-2]=g-2
        p2[m]=p2[m-3]=p2[m]-1
        p3[m-2]=1
        p3[m-1]=p3[m-3]=p3[m-1]+1

    elif p1[m-1] == 0 and c[m-1]==2: #IV.4
        if p3[m-2] != g-1: #IV.4.i
            p2[m-1]=p2[m-2]=p2[m-1]-1
            p3[m-2]=p3[m-2]+1

#page no 23
        elif p3[m-2] == g-1 and p3[m-3]!= g-1: #IV.4.ii

            if p2[m-3]!=0: #IV.4.ii.a
                p1[m]=p1[m-1]=1
                p2[m-1]=p2[m-2]=p2[m-2]-2
                p2[m]=p2[m-3]=p2[m]-1
                p3[m-2]=1
                p3[m-1]=p3[m-3]=p3[m-1]+1

            elif p2[m-3]==0:#IV.4.ii.b
                p1[m] = p1[m - 1] = 1
                p1[m+1]=p1[m-2]=p1[m+1]-1
                p2[m - 1] = p2[m - 2] = p2[m - 1] - 2
                p2[m] = p2[m - 3] = g - 1
                p3[m - 2] = 1
                p3[m - 1] = p3[m - 3] = p3[m - 1] + 1

        elif p3[m-2]==g-1 and p3[m-3]==g-1: #IV.4.iii
            if p2[m-2]!=g-1 and p2[m-2]!=g-2: #IV.4.iii.a
                if p2[m-3]!=g-1: #1st IF
                    p1[m]=p1[m-1]=g-2
                    p1[m+1]=p1[m-2]=p1[m+1]-1
                    p2[m-1]=p2[m-2]=p2[m-2]+2
                    p2[m]=p2[m-3]=p2[m]+1
                    p3[m-1]=p3[m-2]=p3[m-3]=g-2

                elif p2[m-3]==g-1: #2nd IF
                    p1[m] = p1[m - 1] = g - 2
                    p2[m - 1] = p2[m - 2] = p2[m - 2] + 2
                    p2[m] = p2[m - 3] = 0
                    p3[m - 1] = p3[m - 2] = p3[m - 3] = g - 2

            elif p2[m-2]==g-1 or p2[m-2]==g-2: #IV.4.iii.b
                if p2[m-3]>=1: #1st IF
                    p1[m] = p1[m - 1] = 2
                    p2[m - 1] = p2[m - 2] = p2[m - 2] - 3
                    p2[m] = p2[m - 3] = p2[m] - 1
                    p3[m-2] = 3
                    p3[m-1]=p3[m-3]=0

#page no 24
                elif p2[m-3] == 0 and p1[m-2]>=1: #2nd IF
                    p1[m] = p1[m - 1] = 2
                    p1[m+1] = p1[m - 2] = p[m+1]-1
                    p2[m - 1] = p2[m - 2] = p2[m - 2] - 3
                    p2[m] = p2[m - 3] = g - 1
                    p3[m - 2] = 3
                    p3[m - 1] = p3[m - 3] = 0

    elif p1[m-1] == 1 and c[m-1]==1 : #IV.5
        if p3[m-2]!=g-1 and p2[m-2]!=0: #IV.5.i
            p2[m-1]=p2[m-2]=p2[m-2]-1
            p3[m-2]=p3[m-2]+1

        elif p3[m-2]!=g-1 and p2[m-2] == 0: #IV.5.ii
            p1[m]=p1[m-1]=0
            p2[m-1]=p2[m-2]==g-1
            p3[m-2]=p3[m-2]+1

        elif p3[m-2] == g-1 and p3[m-3] != 0: #IV.5.iii
            if p2[m-3]!=g-1: #IV.5.iii.a
                p1[m]=p1[m-1]=0
                p2[m-1]=p2[m-2]=p2[m-1]+1
                p2[m]=p2[m-3]=p2[m]+1
                p3[m-2]=g-2
                p3[m-1]=p3[m-3]=p3[m-1]-1

#page no 25
            elif p2[m-3] == g-1 and p2[m-2] > 1 : #IV.5.iii.b
                p1[m]=p1[m-1]=2
                p2[m-1]=p2[m-2]=p2[m-1]-2
                p2[m]=p2[m-3]=g-2
                p3[m-2]=1
                p3[m-1]=p3[m-3]=p3[m-1]+1

            elif p2[m-3] == g-1 and p2[m-2] == 0 : #IV.5.iii.c
                p2[m]=p2[m-1]=p2[m-2]=p3[m-3]=g-2
                p3[m-2] = 1
                p3[m-1]=p2[m-3]=p3[m-1]+1

            elif p2[m - 3] == g - 1 and p2[m - 2] == 1: #IV.5.iii.d
                p2[m] = p3[m - 3] = g - 2
                p2[m - 1] = p2[m - 2] =g-1
                p3[m - 2] = 1
                p3[m - 1] = p2[m - 3] = p3[m - 1] + 1

        elif p3[m-2] == g-1 and p3[m-3]==0 and p2[m-3]!=0: #IV.5.iv
            if p2[m-2]>1: #IV.5.iv.a
                p1[m]=p1[m-1]=2
                p2[m-1]=p2[m-2]=p2[m-1]-2
                p2[m]=p2[m-3]=p2[m]-1
                p3[m-1]=p3[m-2]=p3[m-3]=1

            elif p2[m-2]==0: #IV.5.iv.b
                p2[m - 1] = p1[m - 2] = g - 2
                p2[m] = p2[m - 3] = p2[m] - 1
                p3[m - 1] = p3[m - 2] = p3[m - 3] = 1

            elif p2[m-2]==1: #IV.5.iv.c
                p2[m - 1] = p1[m - 2] = g - 1
                p2[m] = p2[m - 3] = p2[m] - 1
                p3[m - 1] = p3[m - 2] = p3[m - 3] = 1

        elif p3[m-2]==g-1 and p3[m-3] == 0 and p2[m-3]==0: #IV.5.v
#page no 26
            if p2[m-2]>1:#IV.5.v.a
                p1[m]=p1[m-1]=2
                p1[m+1]=p1[m-2]=p1[m+1]-1
                p2[m-1]=p2[m-2]=p2[m-1]-2
                p2[m]=p2[m-3]=g-1
                p3[m-1]=p3[m-2]=p3[m-2]=1

            elif p2[m-2]==0:#IV.5.v.b
                p1[m+1]=p1[m-2]=p1[m+1]-1
                p2[m - 1] = p2[m - 2] = g - 2
                p2[m] = p2[m - 3] = g - 1
                p3[m - 1] = p3[m - 2] = p3[m - 2] = 1

            elif p2[m-2] == 1:#IV.5.v.c
                p1[m + 1] = p1[m - 2] = p1[m + 1] - 1
                p2[m - 1] = p2[m - 2] = g - 1
                p2[m] = p2[m - 3] = g - 1
                p3[m - 1] = p3[m - 2] = p3[m - 2] = 1

    elif p1[m-1]+c[m-1] == 3: #IV.6
        p2[m-1]=p2[m-2]=p2[m-1]-1
        p3[m-2]=0

    return p1,p2,p3


