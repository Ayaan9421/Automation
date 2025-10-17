from playsound import playsound

try:
        num = int(input("Enter integer: "))
        if num % 2 == 0:
                print('even')
        else:
                print('odd')

        playsound('s1.mp3')

except ValueError:
        print("Enter integers only. ")
        playsound('e1.mp3')