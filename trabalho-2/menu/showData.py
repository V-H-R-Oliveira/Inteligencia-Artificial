def showData(data: list):
    print("|---------------------------------------|")
    for index, element in enumerate(data):
        print("\t\x1b[1m\x1b[1m", index, "|" ,element[0], "\x1b[0m")
        print("|---------------------------------------|")