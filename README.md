# Getting the word position from the app name. (itunes api) 

## Task: 

Suppose we are interested in the positions of our mobile app or competitor’s app. Most often, apps are searched by words in their name (not necessarily in the first place). To find out the specific position for specific words, we can use the iTunes API. Let id be the appleid of the app we want to research (for example, 860011430). This app has a name of N words (in this case “Ghost Lens AR Fun Movie Maker”). Need to write a python script that takes id as input and inserts N rows into the sqlite3 database itunes.db in the itunes table (id, word, pos, date); each row contains the id of the app, the requested word from the name, the position of the app id in the output for this word and the date of running the script.


### Project status: completed