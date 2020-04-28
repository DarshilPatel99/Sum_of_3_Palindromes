#importing needed finctions
from l_is_5_6 import len5,len6
from l_is_1_2_3_4 import len1,len2,len3,len4
from algos import algo1,algo2,algo3,algo4
from Initial_configuration import startingpoint
from functions import *

#input
s = input('Enter Number(digit must be seperated by space): ')
g = int(input('Enter Base( >= 5) : '))

#initialization
n = str_to_list(s)
l = len(n)
ans = []
p = []

if is_valid(n,g):#number is valid

    if l == 1:#length of number is 1(1 digit in number)
        ans = list(len1(n,g))

    elif l == 2:# length of number is 2(2 digit in number)
        ans = list(len2(n,g))

    elif l == 3:# length of number is 3(3 digit in number)
        ans = list(len3(n,g))

    elif l == 4:# length of number is 4(4 digit in number)
        ans = list(len4(n,g))

    elif l == 5:# length of number is 5(5 digit in number)
        ans = list(len5(n,g))

    elif l == 6:# length of number is 6(6 digit in number)
        ans = list(len6(n,g))

    else:# length of number is 7 or more

        # calculating initial configuration
        p = list(startingpoint(n, l, g))

        #from initial configuration identify appropriate algorithm
        #these conditions are written at page no 6
        if ((p[3] == 'A1' or p[3] == 'A2' or p[3] == 'A3' or p[3] == 'A4') and l % 2 == 1) or ((p[3] == 'A5' or p[3] == 'A6') and l % 2 == 0):#algorithm 1
            ans = list(algo1(n, p, g, l))
            # 3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6
            # 1 0 1 3 4 5 6 4 7 3 8 1

        elif (((p[3] == 'A1' or p[3] == 'A2' or p[3] == 'A3' or p[3] == 'A4') and l % 2 == 0) or ((p[3] == 'A5' or p[3] == 'A6') and l % 2 == 1)) and n[l // 2] != 0 and n[(l // 2) - 1] != 0:#algorithm 2
            ans = list(algo2(n, p, g, l))
            # 2 7 1 8 2 8 1 8 2 8 4 5 9 0 4 5 2 3 5 3 6 0
            # 1 4 5 6 7 3 4 5 6 9 3 4 6 7

        elif ((p[3] == 'B1' or p[3] == 'B2' or p[3] == 'B3' or p[3] == 'B4' or p[3] == 'B5' or p[3] == 'B6' or p[3] == 'B7') and l % 2 == 1):#algorithm 3
            ans = list(algo3(n, p, g, l))
            # 1 2 0 2 0 5 6 9 0 3 1 5 9 5 9 4 2 8 5 3 9

        elif ((p[3] == 'B1' or p[3] == 'B2' or p[3] == 'B3' or p[3] == 'B4' or p[3] == 'B5' or p[3] == 'B6' or p[3] == 'B7') and l % 2 == 0) and n[l // 2] != 0 and n[(l // 2) - 1] != 0:#algorithm 4
            ans = list(algo4(n, p, g, l))
            # 1 2 2 6 7 4 2 0 0 9 6 2 0 3 5 3 2 4 4 4

#page no 26
        else:#algorithm 5 for special numbers
            # 1 2 2 6 7 4 2 0 1 0 7 2 0 3 5 3 2 4 4 4
            # 1 0 3 0 0 0 0 0 1 3
            m = l//2
            count = 0
            n1 = n

            #s=g^m + g^m-1
            s = [0]*(m+1)
            s[m]=s[m-1]=1

            #n1 = n - count*s
            while n1[m]==0 or n1[m-1]==0:
                n1 = minus(n1,s,g)
                count += 1

            # calculating initial configuration
            p = list(startingpoint(n1, l, g))
#page no 27
            if len(p[0])==(2*m): #page no. 27 case (i)

                if (((p[3] == 'A1' or p[3] == 'A2' or p[3] == 'A3' or p[3] == 'A4') and l % 2 == 0) or ((p[3] == 'A5' or p[3] == 'A6') and l % 2 == 1)):
                    ans = list(algo2(n1, p, g, l))

                elif ((p[3] == 'B1' or p[3] == 'B2' or p[3] == 'B3' or p[3] == 'B4' or p[3] == 'B5' or p[3] == 'B6' or p[3] == 'B7') and l % 2 == 0):
                    ans = list(algo4(n1, p, g, l))

            if len(p[0])==(2*m)-1: #page no. 27 case (ii)
                z1 = D(n1[0] - n1[l - 3], g)
                p1 = [None] * l
                p2 = [None] * (l - 1)
                p3 = [None] * (l - 2)
                if z1 != 0:
                    p1[l - 1] = p1[0] = 1
                    p2[l - 2] = p3[l - 3] = 0
                    p1[l - 2] = p1[1] = n1[l - 2]
                    p2[l - 3] = p2[0] = n1[l - 3] - 1
                    p3[l - 4] = p3[0] = z1
                    type = 'B1'
                else:
                    p1[l - 1] = p1[0] = 1
                    p2[l - 2] = p3[l - 3] = 0
                    p1[l - 2] = p1[1] = n1[l - 2]
                    p2[l - 3] = p2[0] = n1[l - 3] - 2
                    p3[l - 4] = p3[0] = 1
                    type = 'B2'

                p = [p1,p2,p3,type]

                ans = list(algo4(n1, p, g, l))

            #add s into p1
            #p1 = p1 + count*s
            for i in range(0,count):
                ans[0] = add(ans[0],s,g)

    #printing the number
    print(n[::-1])

    #printing 3 palindrom numbers
    for i in ans:
        print(remove_0(i)[::-1])

else:#not valid number
    print("not valid number or Base")
