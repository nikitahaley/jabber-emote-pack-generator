# jabber-emote-pack-generator
A tool to streamline the creation of emote packs for groups using Pidgin/Adium to communicate.

When executing the script you will be asked for a path; make sure the directory ends in / because this version doesn't check for it and WILL generate empty files with stupid names if given the chance.
When prompted for a pack logo icon, do not include the path. Pidgin will correctly read just a filename (eg: coolicon.png) assuming that file actually exists in the pack directory.

The current version of this script will generate a Pidgin theme file and Adium plist with the following behavior:

The resulting emotes will be called by their filename without the extension, surrounded by colons (:). For example, Pidgin will be able to call "coolicon.png" with :coolicon: and the theme file will contain this line:

! coolicon.png				:coolicon:

For filenames containing uppercase characters, the resulting emote can be called with sensitive casing or entirely lowercase. For example, Pidgin will be able to call "CoolIcon.png" with :CoolIcon: OR :coolicon: and the theme file will contain this line:

! CoolIcon.png				:CoolIcon: :coolicon:

To load your emote pack into Pidgin:

1. Locate your Pidgin user data folder (usually %appdata%/.purple/)
2. Copy the folder containing your emotes to smileys folder (correct directory structure should resemble /%appdata%/.purple/smileys/coolpack/coolicon.png)
3. Select from Tools > Preferences > Themes > Smileys in Pidgin

Restarting Pidgin is not required. If you make changes to your pack after Pidgin has already loaded it, simply select another emote pack from the Smileys menu's dropdown then switch back to yours. Changes will take effect immediately and the new version of the pack will be used for any new lines in conversations.

To load your emote pack into Adium, add .AdiumEmoticonSet to the end of the Pidgin folder name after creating the Emoticons.plist set, then put the file into the /Library/Application Support/Adium 2.0/Emoticons/ folder. Restart Adium and if it is done correctly Adium will add the emoticon pack to the list.

This is a very basic version of this script and it isn't really recommended to use it, or anything else I've ever touched. Please report bugs in this project's issue tracker.
