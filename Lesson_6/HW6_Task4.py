import json
from datetime import timedelta
dur_of_track = 0
with open('acdc.json', 'r+') as file:
    d = json.load(file)
    track = d['album']['tracks']['track']
for i in track:
    dur_of_track += int(i['duration'])
print(timedelta(seconds=dur_of_track))
