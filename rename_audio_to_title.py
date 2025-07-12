from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from pathlib import Path
import os

def rename_file_to_title(filepath:Path):
    if os.fsdecode(filepath).endswith(".mp3"):
        audio = MP3(filepath, ID3=ID3)
        title = audio.get("TIT2")
        if (title):
            renamed_path = os.path.join(filepath.parent, title.text[0]+".mp3")
        else:
            print("Skipped file without title: " + os.fsdecode(filepath))
            return
    elif os.fsdecode(filepath).endswith(".flac"):
        audio = FLAC(filepath)
        title_list = audio.get("title")
        if title_list and len(title_list) > 0:
            title = title_list[0]
            renamed_path = os.path.join(filepath.parent, title+".flac")
        else:
            print("Skipped file without title: " + os.fsdecode(filepath))
            return
    if not os.path.exists(renamed_path):
        os.rename(filepath, renamed_path)
    else:
        print("Skipped file that is already renamed or already exists: "+renamed_path)

def rename_recursive(folderpath:Path):
    for filepath in Path(folderpath).glob('*'):
        filepathstr = os.fsdecode(filepath)
        supported_audio_extensions:tuple[str, ...] = ("mp3", ".flac")
        # if the file is a directory, rename the files in that directory recursively.
        if (os.path.isdir(filepath)):
            rename_recursive(filepath)
        # if it's an audio file, rename it
        elif os.path.isfile(filepath) and (filepathstr.endswith(supported_audio_extensions)):
            rename_file_to_title(filepath)

directory = Path(os.getcwd())
rename_recursive(directory)