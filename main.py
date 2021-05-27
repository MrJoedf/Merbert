import os
import shutil
import fnmatch
import re
import glob

from os.path import expanduser
#USER DIRECTORY
home = expanduser("~")
source = home
#if nosource, then source = home

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def makeFile(target, location, src=source):
    location = location[1:-1]
    print("MAKE FILE")
    if src != source:
        src = src[1:-1]
        src = source + "/" + src
    location = source + "/" + location
    target = target[1:-1]

    newPath = location + '/' + target
    if os.path.exists(newPath):
        return
    else:
        os.mkdir(newPath)


def deleteFile(target, location, src=source):
    location = location[1:-1]
    print("DELETE FILE")
    if src!=source:
        src = src[1:-1]
        src = source + "/" + src
    location = source + "/" + location
    target = target[1:-1]



    if os.path.exists(target) and os.path.exists(location):
        print("EXISTS")
        os.remove(find(target, source))
    else:
        print("LOOK FOR FILE")
        # print(location)
        matches = findMatch(target, src)
        print(matches)
        for match in matches:
            os.remove(match)

def fileify(string):
    if string[0]!='*':
        return('*' + string)
    return string

def findMatch(pattern, path):
    print("FIND MATCH")
    result = []
   # pattern = pattern[1:-1]
    print("PATTERN: ", pattern)

    print(glob.glob(path))

    for root, dirs, files in os.walk(path):
        for name in files:
            if pattern in name:
                print(name)
                result.append(os.path.join(root, name))

    return result

def moveTo(target,  location, src=source):
    location = location[1:-1]
    location = source + "/" + location
    target = target[1:-1]

    if src!=source:
        src = src[1:-1]
        src = source + "/" + src

        #make sure regex can find any matching files
       # target = fileify(target)
        print("NEW SOURCE: ", target)
        if os.path.exists(location) == False:
            os.mkdir(location)

    if os.path.exists(target) and os.path.exists(location):
        print("EXISTS")
        shutil.move(find(target, source), location)
    else:
        print("LOOK FOR FILE")
       # print(location)
        matches = findMatch(target, src)
        print(matches)
        for match in matches:
            shutil.move(match, location)

print("MERBERT v0.1")
commands = ["move", "delete", "sizeof", "make", "rename", "show", "source", "nosource", "end"]

commandLine = ""
while commandLine != "end":
    commandLine = input("Enter command: ")

    print("CL: ", commandLine)
    comSplit = commandLine.split()
    command = comSplit[0]

    print(comSplit)

    if command in commands:
        print(command)
        if command == "move":
            #Keywords are included in quotation marks
            quoted = re.compile('"[^"]*"')
            spots = []
            for value in quoted.findall(commandLine):
                spots.append(value)

            if len(spots)>3 or len(spots)<2:
                print("Invalid input.")
            else:
                if len(spots)==2:
                    print(spots[0], spots[1])
                    moveTo(spots[0], spots[1])
                else:
                    print(spots[0], spots[2], spots[1])

                    moveTo(spots[0], spots[2], spots[1])

        elif command == "delete":
            quoted = re.compile('"[^"]*"')
            spots = []
            for value in quoted.findall(commandLine):
                spots.append(value)

            if len(spots) > 3 or len(spots) < 2:
                print("Invalid input.")
            else:
                print(spots)
                deleteFile(spots[0], spots[1])

        elif command == "make":
            quoted = re.compile('"[^"]*"')
            spots = []
            for value in quoted.findall(commandLine):
                spots.append(value)

            if len(spots) > 2 or len(spots) < 1:
                print("Invalid input.")
            else:
                print(spots)
                if len(spots)==2:
                    makeFile(spots[0], spots[1])

                if len(spots)==1:
                    makeFile(spots[0])


    else:
        print("Invalid input.")


