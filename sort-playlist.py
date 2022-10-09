from ytmusicapi import YTMusic
import json
import os.path

# Uncomment next line to auth as per https://ytmusicapi.readthedocs.io/en/latest/usage.html#authenticated
# YTMusic.setup(filepath="headers_auth.json")

ytmusic = YTMusic('headers_auth.json')

with open('./playlist.txt', 'r') as playlistFile:
    playlistId = playlistFile.read()

dataFilePath = "./" + playlistId + ".json"

columnStr = input(
    "Which column to sort on? 1: Title (default) | 2: Album | 3: Artist. \n")

if (columnStr == "1"):
    column = 'title'
elif (columnStr == "2"):
    column = 'albumName'
elif (columnStr == "3"):
    column = 'artist'
else:
    column = 'title'

ascStr = input(
    "Ascending or Descending? 1: Ascending (default) | 2: Descending\n")
isDec = ascStr == '2'

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

for track in playlist["tracks"]:
    track['artist'] = track['artists'][0]['name']

    if track['album']:
        track['albumName'] = track['album']['name']
    else:
        track['albumName'] = ''

sortedIds = []

sortedTracks = sorted(playlist["tracks"], key=lambda d: (
    d[column] or '').lower(), reverse=isDec)
for track in sortedTracks:
    sortedIds.append(track['videoId'])

backupName = 'backup-sort-' + playlistId + '.json'

shouldBackup = True

if os.path.exists(backupName):
    confirmBackupOverwrite = input(
        "There's already a backup called "+backupName + ", overwrite? Y/N\n")

    shouldBackup = confirmBackupOverwrite.lower() == 'y'

if shouldBackup:
    with open(backupName, "w") as outfile:
        outfile.write(json.dumps(
            sortedTracks, indent=4))
        print("I've made a backup in "+backupName+"\n")

confirm = input(
    "The script will now remove all playlist items and add them again (sorted).\nAre you ready? Y/N \n")
if confirm.lower() == 'y':
    ytmusic.remove_playlist_items(playlistId, videos=sortedTracks)

    ytmusic.add_playlist_items(playlistId, videoIds=sortedIds)
