from mutagen.flac import FLAC
from pathlib import Path
import os
import subprocess

def convert_recursive(folderpath:Path):
    for filepath in Path(folderpath).glob('*'):
        title, extension = os.path.splitext(filepath)
        # if the file is a directory, convert the files in that directory recursively.
        if (os.path.isdir(filepath)):
            convert_recursive(filepath)
        # if it's a flac file, convert it
        elif (os.path.isfile(filepath) and extension == ".flac"):
            output_path = title+".mp3"
            if not os.path.exists(output_path):
                subprocess.run([
                    "ffmpeg", "-i", filepath, "-ab", "192k", output_path
                ])
                os.remove(filepath)

directory = Path(os.getcwd())
convert_recursive(directory)