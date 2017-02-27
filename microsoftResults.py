import microsoftTrans
import time

def main():
    text = open("texts/starwars.txt", "r").read() #THIS WILL CONSUME 2 000 / 2 000 000 FREE MONTHLY CHARACTERS
    time.clock()
    microsoftText = microsoftTrans.translate(text=text, to="fr")

    print("microsoft: {}\n".format(time.clock()))
    print(microsoftText)

if __name__ == "__main__":
    main()