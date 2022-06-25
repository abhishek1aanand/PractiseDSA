def group(list1,Q1):
    new_string = ""
    for z in Q1:
        if z[0] == z[1]: print(list1[z[0]-1][z[2]-1])
        else:

            for w in range(z[0] - 1, z[1]):
                new_string = new_string + list1[w]

            print(new_string)
            print(z[2])
            print(new_string[z[2]-1])
            new_string=""

        #print(new_string[z[2]-1])

N = int(input())
list1 = []
Q1 = []
for i in range(N):
    list1.append(input())


Q = int(input())
for i in range(Q):
    if i == 0:
        Q1 = [[int(x) for x in input().split(" ") ]]
    else:
        Q1 = Q1 + [[int(x) for x in input().split(" ")]]
print(list1)
print(Q1)

group(list1,Q1)

