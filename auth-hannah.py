from discord_webhook import DiscordWebhook
import requests
import time
import random
import string
import os

class NitroGen:
    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""AUTHENTICATOR""")
        time.sleep(1)
        self.slowType("\nUniqueID: ", .02, newline = True)
        num = int(input(''))
        with open('uniqueid.txt') as file:
            unique_ids = file.readlines()

        def func1():
            print()
        def func2():
            print()

        switch = {
            unique_ids[0]: func1,
            unique_ids[1]: func2
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
                start = time.time()
    if __name__ == '__main__':
        Gen = NitroGen()
        Gen.main()
