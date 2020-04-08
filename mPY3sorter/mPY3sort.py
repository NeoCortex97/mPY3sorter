#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pathlib
import shutil
import eyed3
import json
import sys


def print_help():
    print("Benutzug: {} path/to/config.json".format(sys.argv[0]))
    print("Dieses Tool sortiert mp3 Dateien aus einem Ordner nach folgenden Kriterien in Ordner:")
    print("1. Künstler (album_artist tag)")
    print("2. Album (album tag)")
    print("3. Songtitel als dateiname.[*]")
    print("\n    * Wird in der nächsten version geändet, dass der title tag benutzt wird.")
    print("\n\nDas Tool ist gedacht um die arbeit mit dem chrome plugin für google Music zu erleichtern. \nGoogle Music platziert die downloads in einem frei wählbaren Ordner mit folgender Namenskovention:")
    print("<Künstler> - <Songname>.mp3")
    print("Das Tool verschiebt die dateien und benennt sie um. Das Tool legt ausßerdem eine Verknüpfung in den download ordner von google music an.")


def main(**kwargs):
    if not len(sys.argv) > 1:
        print_help()
    else:
        conf = json.load(pathlib.Path(sys.argv[1]).expanduser().absolute().open())
        destination_base = pathlib.Path(conf["destination_base_path"]).expanduser()
        sources = conf["sources"]
        for source_dir in sources:
            source = pathlib.Path(source_dir).expanduser()
            print("Betrete Quellordner: {}".format(source))
            artists = dict()
            for item in source.iterdir():
                audiofile = eyed3.load(item)
                if audiofile.tag.album_artist not in artists.keys():
                    artists[audiofile.tag.album_artist] = dict()
                if audiofile.tag.album not in artists[audiofile.tag.album_artist]:
                    artists[audiofile.tag.album_artist][audiofile.tag.album] = list()
                if item not in artists[audiofile.tag.album_artist][audiofile.tag.album]:
                    artists[audiofile.tag.album_artist][audiofile.tag.album].append((item, audiofile.tag.title))

            for künstler in artists.keys():
                print("Verarbeite Künstler \"{}\".".format(künstler))
                for album in artists[künstler].keys():
                    print("Verarbeite Album \"{}\" von \"{}\"".format(album, künstler))
                    dst_path = destination_base.joinpath(künstler).joinpath(album)
                    dst_path.mkdir(parents=True, exist_ok=True)
                    for title in artists[künstler][album]:
                        print("Verschiebe Titel \"{}\" aus \"{}\" von \"{}\"".format(title[1], album, künstler))
                        if not title[0].is_symlink():
                            tmp_path = dst_path.joinpath(title[1])
                            shutil.move(title[0], tmp_path)
                            title[0].symlink_to(tmp_path)


if __name__ == "__main__":
    main()