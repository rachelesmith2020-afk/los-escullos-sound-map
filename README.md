# Los Escullos sound map

Field recordings of Los Escullos, Cabo de Gata-Níjar Natural Park (Almería, Spain), by OOLITA (oolita.es).

Every sound is a real recording made at Los Escullos. No stand-ins from elsewhere.

## What is here

- `data/sound-log.csv` the master list: 19 slots with coordinates, best time, access notes, photo credit, recording details, licence and status
- `audio/` recordings, as published
- `photos/own/` photos taken by OOLITA for each slot
- `photos/reference/` reference photos from Wikimedia Commons, credited in `data/sound-log.csv` (column "Reference photo") under their own licences
- `map/` the sound map page (`template.html` plus `build.py` builds `los-escullos-sound-map.html`)

## Where it is published

- Freesound: https://freesound.org/people/oolita/ (pack "Los Escullos, Cabo de Gata")
- Large originals (video, raw recordings) are kept in Google Drive, not in this repo

## Licence

Sounds: Creative Commons Attribution NonCommercial 4.0 (CC BY-NC 4.0). Credit OOLITA. Not for commercial use.
Own photos: all rights reserved by OOLITA unless stated.
Reference photos: see the credit on each row of the log.

## Adding a sound

1. Record audio only, 60 to 120 seconds
2. Fill the slot's row in `data/sound-log.csv` (date, time, weather, file name, Freesound link, status)
3. Add the audio to `audio/` and the photo to `photos/own/` named `LE-xx_photo.jpg`
4. Rebuild the map: `cd map && python3 build.py audio`
