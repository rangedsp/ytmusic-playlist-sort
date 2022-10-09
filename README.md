# **Work in progress - please make sure to make backups, I'd recommend making a copy of the playlist and use that to test**

# Using ytmusicapi to remove duplicates in playlists

Youtube Music annoyed the crap out of me the other day, I can't for the life of me figure out how to sort my songs by title alphabetically, nor sort it by album, actually there's no way to sort other than newest first / last.

So I found this library:

https://ytmusicapi.readthedocs.io/en/latest/index.html

Maybe there are equivalents in node.js, but wanted to brush up on my python so here we are.

To get it to work, the rough steps are:

0. `pip install ytmusicapi` (using Python 3)
1. Grab the cookies from your browser session as [per instruction](https://ytmusicapi.readthedocs.io/en/latest/setup.html#authenticated-requests)
2. Run the setup call to store auth in a local json file
3. Change the playlist ID in `playlist.txt` to your playlist. It will be in the URL when you visit the playlist in a web browser. E.g. *https://music.youtube.com/playlist?list=PLUKStexm-HN_oXN2zUwnCgmiWzM9BVGoG* , in this case the ID is `PLUKStexm-HN_oXN2zUwnCgmiWzM9BVGoG`
4. Run either `python remove-dupe.py` or `python sort-playlist.py` 

## sort-playlist.py
This will allow you to sort by artist / title / album name, either ascending or descending. 

The easiest way to run sort was to remove all the tracks and add the sorted tracks back. This is rather risky so I made the script output the sorted tracks into a json file 

## remove-dupe.py
This will find duplicate songs or songs that are no longer available and remove them.

## restore-backup.py
This will load up the backup tracks and add them back to the playlist.