import googleTrans
import time

def main():
    text = open("texts/starwars.txt", "r").read() ## CAREFUL HERE. THIS CALL COMSUMES ABOUT 2 000 CHARACTERS
    time.clock()
    googleText = googleTrans.translate(q=text, source="en", target="fr")

    print("google: {}\n".format(time.clock()))
    print(googleText)

if __name__ == "__main__":
    main()