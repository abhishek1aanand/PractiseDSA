n,m = [int(x) for x in (input().split(" "))]
list1 = [int(x) for x in (input().split(" "))]
A = set([int(x) for x in (input().split(" "))])
B = set([int(x) for x in (input().split(" "))])
happiness = 0
for i in list1:
    if i in A:
        happiness = happiness+1
    elif i in B:
        happiness = happiness - 1
print(happiness)
