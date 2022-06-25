import textwrap

import math
def wrap(string, max_width):
    str1 = ""
    for i in range(len(string)):
        if i == 0:
            str1 = string[:max_width]
        elif i % max_width == 0:
            str1 = str1 + '\n' + string[i:i + max_width]
    print (str1)

    return str1


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)