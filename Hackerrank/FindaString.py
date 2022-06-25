def count_substring(string, sub_string):
    print(string)
    print(sub_string)
    count = 0
    # string = string.lower()
    # sub_string = sub_string.lower()
    for i in range(0, len(string)):
        print(string[i:i + len(sub_string)])
        if string[i:i + len(sub_string)] == sub_string: count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)