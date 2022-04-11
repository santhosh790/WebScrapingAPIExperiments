'''
Print numbers in chart as below::
Given sequence 3 2 5 2 print
        /\
       /  \
  /\  /
 /  \/
/
'''

def printChart(vals):
    print(vals)
    cols = sum(vals)
    cnt = 0
    rows = 0
    min = 0
    for idx, each in enumerate(vals):
        if idx % 2 == 0:
            cnt += each
        else:
            cnt -= each
        if rows < cnt:
            rows = cnt
        if min > cnt:
            min = cnt
    rows += 1 + abs(min)
    cols += 1
    a = [[" "]*cols for i in range(rows)]
    i = 0
    j = rows-1-abs(min)
    print(j)
    for idx, each in enumerate(vals):
        for k in range(1, each+1):
            if idx % 2 == 0:
                a[j][i] = "/"
                op = -1

            else:

                a[j][i] = "\\"
                op = 1
            if k != each:
                if j == 1:
                    a[j][i+2] = "\\"
                    a[j][i] = ""
                    a[j-1][i] = "o"
                    i = i+1
                j = j+op
            i = i+1

    for each in range(rows):
        v = "".join(val for val in a[each])
        print(v)
    #print("".join(val for val in (a[each] for each in range(rows))))

printChart([5,4,3,2,1])
printChart([1,2,3,4,5])
printChart([1,2,3,4,21])
printChart([1,36,2,8,7])
printChart([3,7,21,16])
printChart([43,42,41,39])
printChart([1,10,3,16,5,74])
printChart([3,1,2,3,6,2,3,6,3,2,3,6,2])
printChart([10,7,12,2,4,7,2,4,1,2,6,6,3,2,1,4,7,2,7,3,1,3,11,4,2,1,5,2,3,3,3,6,1,3,9,5,2,1,2,11,9,2,3,8,2,5,1,2,7,2,4,11,2,12])