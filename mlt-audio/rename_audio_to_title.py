from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from pathlib import Path
import os
import argparse

def rename_file_to_title(filepath:Path):
    if os.fsdecode(filepath).endswith(".mp3"):
        audio = MP3(filepath, ID3=ID3)
        title = audio.get("TIT2")
        if (args.include_track_number):
            track_number = audio.get("TRCK")
            disc_number = audio.get("TPOS")
            if (track_number):
                if (disc_number):
                    track_disc_and_number = disc_number.text[0]+"."+track_number.text[0]
                else:
                    track_disc_and_number = track_number.text[0]
        if (title):
            title_str = title.text[0]
            if (track_disc_and_number):
                title_str = track_disc_and_number+" "+title_str
            renamed_path = os.path.join(filepath.parent, title_str+".mp3")
        else:
            print("Skipped file without title: " + os.fsdecode(filepath))
            return
    elif os.fsdecode(filepath).endswith(".flac"):
        audio = FLAC(filepath)
        title_list = audio.get("title")
        if (args.include_track_number):
            tracknumber_list = audio.get("tracknumber")
            discnumber_list = audio.get("discnumber")
            track_number = tracknumber_list[0] if tracknumber_list else None
            disc_number = discnumber_list[0] if discnumber_list else None
            if (track_number):
                if (disc_number):
                    track_disc_and_number = disc_number+"."+track_number
                else:
                    track_disc_and_number = track_number
        if title_list and len(title_list) > 0:
            title = title_list[0]
            if (track_disc_and_number):
                title = track_disc_and_number+" "+title
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

parser = argparse.ArgumentParser(description="Rename files with additional metadata")

parser.add_argument(
    "--include-track-number",
    action="store_true",
    help="Include the track number in the filename"
)

args = parser.parse_args()

directory = Path(os.getcwd())
rename_recursive(directory)