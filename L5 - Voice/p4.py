from playsound import playsound

try:
        num = int(input("Enter integer: "))
        if num % 2 == 0:
                print('even')
                playsound('even.mp3')
        else:
                print('odd')
                playsound('odd.mp3')

        playsound('s1.mp3')

except ValueError:
        print("Enter integers only. ")
        playsound('error_integer.mp3')
        