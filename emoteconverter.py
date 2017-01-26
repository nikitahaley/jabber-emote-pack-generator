#!/usr/bin/env python3
import os
import sys

DIR_EMOTES = str(input("Enter directory to generate theme list for: "))
INFO_NAME = str(input("Enter name of emote pack: "))
INFO_DESC = str(input("Enter description of emote pack: "))
INFO_ICON = str(input("Enter filename of logo icon: "))
INFO_AUTH = str(input("Enter author name: "))
DIR_EMOTES_LIST = os.listdir(DIR_EMOTES) # get list of files in dir provided by user
print("Generating theme list for " + str(len(DIR_EMOTES_LIST)) + " emotes in " + DIR_EMOTES) # print the number of emotes in the directory

f = open(DIR_EMOTES + 'theme', 'w')

f.write("Name=" + INFO_NAME + "\nDescription=" + INFO_DESC + "\nIcon=" + INFO_ICON + "\nAuthor=" + INFO_AUTH + "\n\n[default]\n\n") # tell pidgin about our emote pack

for line in DIR_EMOTES_LIST:
    EMOTE_LINE = line
    EMOTE_LINE_NOEXT = EMOTE_LINE.split(".",1)[0] # remove the extension from the current emote file
    if EMOTE_LINE_NOEXT.islower():  # check for emotes with no uppercase letters so we don't write them twice
        f.write("! " + EMOTE_LINE + "\t\t\t\t:" + EMOTE_LINE_NOEXT + ":\n")
    else:
        f.write("! " + EMOTE_LINE + "\t\t\t\t:" + EMOTE_LINE_NOEXT + ": :" + str(EMOTE_LINE_NOEXT.lower()) + ":\n")


f.close()

with open(DIR_EMOTES + 'theme') as f:
    lines = f.readlines()
    f.close()
	
ff = open(DIR_EMOTES + 'Emoticons.plist', 'w')

ff.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
ff.write("<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">\n")
ff.write("<plist version=\"1.0\">\n")
ff.write("<dict>\n")
ff.write("<key>Emoticons</key>\n")
ff.write("<dict>\n")

for line in lines:
    if not (("=" in line) or line.startswith("#") or line.isspace() or line.startswith("[")): # ignore anything that's not an emote definition
        words = line.split()
        if (words[0] == "!"):
            words.pop(0) # pop off the exclamation point if there is one
        ff.write("<key>")
        ff.write(words.pop(0)) # pop off the emote file
        ff.write("</key>\n<dict>\n<key>Equivalents</key>\n<array>\n")
        for word in words:
            ff.write("<string>")
            ff.write(word) # write the emote triggers
            ff.write("</string>\n")
        ff.write("</array>\n<key>Name</key>\n<string>")
        ff.write(words.pop(0)) # pop off the first emote trigger string as name
        ff.write("</string>\n</dict>\n")

ff.write("</dict>\n<key>AdiumSetVersion</key>\n<integer>1</integer>\n</dict>\n</plist>")
ff.close()
print('Created theme and Emoticons.plist in target directory.')
