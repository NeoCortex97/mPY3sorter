# mPY3sorter
Ein script, das Mp3 dateien nach metainformationen sortiert.
Das script erwartet einen Ordner der nur mit mp3 dateien gefüllt ist, die mindestens die Metainformationen über Künstler und album enthalten.

## Installation
Installiere python3. [Hier](https://realpython.com/installing-python/) findest du eine Anleitung.  
Danach führe in einer Komandozeiel/einem Terminal folgenden befehl aus ```pip3 install -r `requirements.txt``

Danach kann das Script benutzt werden. Idealerweise erstellt man sich ein konsolenscript, das das script direkt startet.

## Benutzung
```bash
python3 pfad\zu\mPY3sorter.py pfad\zu\settings.json
```
Ein script, dass das tool firekt aufruft könnte ungefähr so aussehen:
```bash
@echo off
python3 pfad\zu\mPY3sorter.py \pfad\zu\settings.json
pause  
```
Ein Beispiel für eine config datei:
```json
{
  "sources": [
    "~/Musik/GoogleMusic_sync/",
    "~/Musik/Spotify_download/"
  ],
  "destination_base_path": "~/Musik/"
}
```
In den eckigen Klammern hinter ```sources``` muss mindestens ein, gerne auch mehrere Ordner angegeben werden aus denen die Dateien gesucht werden sollen.  
Hinter ```destinanation_base_path```  muss der Ordner angegeben werden, in dem die Sortierten Dateien abgelegt werden sollen.

## TODO
* [X] Titel aus metainformationen  
* [X] Mehrere Quellordner pro settings.json  
* [X] ignorieren von nicht unterstützten dateien  
* [ ] unterstützen von anderen Dateiformaten  
* [ ] komandozeilenparameter  
* [ ] hübscheres interface  
