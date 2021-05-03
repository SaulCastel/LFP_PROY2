from os import write


def report(msg):
    file = open("./log.txt","a")
    file.write("> "+msg+"\n")
    file.close()