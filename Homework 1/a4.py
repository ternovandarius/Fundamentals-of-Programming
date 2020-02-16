while True:
    x = input("Insert an integer:")
    x = int(x)

    digit_list = []

    while x!=0:
        digit_list.append(x%10)
        x=x//10

    digit_list.sort(key=int)
    #digit_list[::-1]

    print(*digit_list, sep = '')

