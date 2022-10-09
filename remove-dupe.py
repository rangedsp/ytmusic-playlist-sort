from ytmusicapi import YTMusic
import json
import os.path

# Uncomment next line to auth as per https://ytmusicapi.readthedocs.io/en/latest/usage.html#authenticated
# YTMusic.setup(filepath="headers_auth.json")

ytmusic = YTMusic('headers_auth.json')

with open('./playlist.txt', 'r') as playlistFile:
    playlistId = playlistFile.read()

dataFilePath = "./" + playlistId + ".json"
playlist = ytmusic.get_playlist(playlistId, limit=None)

# This is to make it easier in development, don't want to load my huge playlist every time
# if os.path.exists(dataFilePath):
#     with open(dataFilePath, 'r') as openfile:
#         playlist = json.load(openfile)

# else:
#     playlist = ytmusic.get_playlist(playlistId, limit=None)

#     playlistObj = json.dumps(playlist, indent=4)
#     with open(dataFilePath, "w") as outfile:
#         outfile.write(playlistObj)

trackDict = {}
dupes = []
unavailables = []

for track in playlist["tracks"]:
    if track["videoId"] in trackDict:
        dupes.append(track)
        continue

    if track["videoId"] in trackDict:
        dupes.append(track)
        continue
    if track["isAvailable"] is not True:
        unavailables.append(track)

    trackDict[track["videoId"]] = track

print('Found ' + str(len(dupes)) + " duplicates. \n")
if len(dupes) > 0:
    removeDupe = input('Do you want to remove them? Y/N \n')
    if removeDupe.lower() == "y":
        print(" Removing... \n")
        ytmusic.remove_playlist_items(playlistId, dupes)

print('Found ' + str(len(unavailables)) + " unavailable tracks. \n")
if len(unavailables) > 0:
    removeUnavailable = input('Do you want to remove them? Y/N \n')
    if removeUnavailable.lower() == "y":
        print(" Removing... \n")
        ytmusic.remove_playlist_items(playlistId, unavailables)
