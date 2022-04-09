def fact(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        return x * fact(x-1)

# print(fact(int(input()))) this works
for e in range(int(input("please input a number: "))):
    print(e, fact(e))
    # print(e)

# print(list(range(int(input("gimmie number: "))))) range function print