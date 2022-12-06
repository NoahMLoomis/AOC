def check_0(str):
    if str[0] in str[1:4]:
        return True
    return False


def check_1(str):
    if str[1] == str[0] or str[1] in str[2:4]:
        return True
    return False


def check_2(str):
    if str[2] == str[0] or str[2] == str[1] or str[2] == str[3]:
        return True
    return False


def check_3(str):
    if str[3] in str[0:3]:
        return True
    return False


def check_unique(str, index):
    string_without_index =  str[:index] + str[index + 1:]
    if str[index] in string_without_index:
        return False
    return True


def get_first_packet():
    with open("./data/day6.txt") as f:
        file = f.readline()
        for i in range(len(file)):
            searchStr = file[i:i+14]
            uniqueCount = 0
            for k in range(len(searchStr)):
                if uniqueCount == 13:
                    return i + 14
                if check_unique(searchStr, k):
                    uniqueCount += 1


print(get_first_packet())
