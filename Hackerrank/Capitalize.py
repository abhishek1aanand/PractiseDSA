# Complete the solve function below.
import os
def solve(s):
    list1 = []
    str1 = ""
    if s.find(" ") != (-1):

        list1 = s.split(" ")

        list1 = [x[0].upper() + x[1:] for x in list1 if x!='']
        for i in range(len(list1)):
            if i == 0:
                str1 = list1[0]
            else:
                str1 = str1 + " " + list1[i]
        print(str1)



if __name__ == '__main__':


    s = input()

    solve(s)


