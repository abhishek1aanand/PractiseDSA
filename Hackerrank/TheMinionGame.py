def minion_game(string):
    string = string.lower()
    list1 = []
    list2 = []
    for i in range(len(string)):
        if string[i] in "aeiou":
            string1 = string[i:]
            list1.append(string1[i])
            list1.append([string1[i] + string1[x] for x in range(i + 1, len(string1))])

    print(list1)
if __name__ == '__main__':
    s = input()
    minion_game(s)