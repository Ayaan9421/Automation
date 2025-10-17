from playsound import playsound

while True:
        op = int(input("1) success, 2) alert, 3) Error  and 4) exit: "))
        if op == 1:
                playsound('s1.mp3')
        elif op == 2:
                playsound('a1.mp3')
        elif op == 3:
                playsound('e1.mp3')
        elif op == 4:
                break