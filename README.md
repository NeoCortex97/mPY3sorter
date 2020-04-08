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
Wenn man mehrere settings dateien anlegt, kann man dateien aus unterschiedlichen ordnern zusammenführen.

## TODO
*[ ] Titel aus metainformationen  
*[ ] Mehrere Quellordner pro settings.json  
*[ ] ignorieren von nicht unterstützten dateien  
*[ ] komandozeilenparameter  
*[ ] unterstützen von anderen Dateiformaten  
*[ ] hübscheres interface  
