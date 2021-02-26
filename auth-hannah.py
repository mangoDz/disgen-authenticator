#from discord_webhook import DiscordWebhook
import requests
import time
import random
import string
import os

class NitroGen:

    def __init__(self):
        self.num = 1

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""AUTHENTICATOR""")
        time.sleep(1)
        self.slowType("\nUniqueID: ", .02, newLine = True)
        num = int(input(''))
        unique_ids = []
        with open('uniqueid.txt') as file:
            for line in file:
                unique_ids.append(int(line))
        print('successfully read file')
        print(len(unique_ids))
        print(unique_ids[19])

        def func1():
            print()
        def func2():
            print()

        switch = {
            unique_ids[0]: func1,
            unique_ids[1]: func2,
            unique_ids[2]: func2,
            unique_ids[3]: func2,
            unique_ids[4]: func2,
            unique_ids[5]: func2,
            unique_ids[6]: func2,
            unique_ids[7]: func2,
            unique_ids[8]: func2,
            unique_ids[9]: func2,
            unique_ids[10]: func2,
            unique_ids[11]: func2,
            unique_ids[12]: func2,
            unique_ids[13]: func2,
            unique_ids[14]: func2,
            unique_ids[15]: func2,
            unique_ids[16]: func2,
            unique_ids[17]: func2,
            unique_ids[18]: func2,
            unique_ids[19]: func2,
        }

        switch[num]()
        os.startfile('run.bat')
        print("wow!")

        input("\nYou can now close this program.")
        [input(i) for i in range(4, 0, -1)]

    def slowType(self, text, speed, newLine = True):
        for i in text:
            print(i, end = "", flush = True)
            time.sleep(speed)
        if newLine:
            print()

if __name__ == '__main__':
    print("name is main")
    Gen = NitroGen()
    Gen.main()
