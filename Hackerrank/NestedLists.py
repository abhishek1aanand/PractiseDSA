import sys

if __name__ == '__main__':
    list1 = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        list1.extend([[name, score]])
    a = [x[1] for x in list1]
    second_min = a[1]
    minimum = a[0]
    if second_min == minimum: second_min = minimum
    for i in range(2, len(a)):
        if a[i] < minimum and a[i] <second_min:
            minimum =a[i]


