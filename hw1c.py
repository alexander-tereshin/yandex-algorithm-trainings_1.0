def formatting(string):
    for i in (['-', '(', ')', '+']):
        string = string.replace(i, "")
    if len(string) == 7:
        string = "8495" + string
    else:
        if string[0] == '7':
            string = '8' + string[1:]
    return string


num = formatting(input())
ls = map(formatting, [input(), input(), input()])

for i in ls:
    if num == i:
        print('YES')
    else:
        print('NO')
