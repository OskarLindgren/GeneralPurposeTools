import os

def Calculator():
    os.system("title " + "GPT - Calculator")
    print("Press q to exit")
    print("[Uses python syntax]")
    while True:
        userinput = input("Equaction: ")
        if userinput.lower() == 'q':
            return
        else:
            try:
                print(eval(userinput))
            except Exception as e:
                print(e)
                input("Press enter to continue...")
                return

if __name__ == '__main__':
    Calculator()