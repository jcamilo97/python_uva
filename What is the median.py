ray = []
try:
    while True:
        x = input()
        if x == '':
            break
        aray.append(int(x))
        aray.sort()
        if(len(aray)%2 != 0):
            print(aray[int(len(aray)/2)])
        else:
            a = aray[(int(len(aray)/2))-1]
            print(int((aray[int(len(aray)/2)]+a)/2))
except EOFError:
    pass