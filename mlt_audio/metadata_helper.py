from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from pathlib import Path

def fetch_title(filepath:Path):
    match filepath.suffix:
        case ".mp3":
            audio = MP3(filepath, ID3=ID3)
            title_list = audio.get("TIT2")
            return title_list[0] if title_list else None
        case ".flac":
            audio = FLAC(filepath)
            title_list = audio.get("title")
            return title_list[0] if (title_list and len(title_list) > 0) else None

def fetch_track_number_string(filepath:Path):
    match filepath.suffix:
        case ".mp3":
            audio = MP3(filepath, ID3=ID3)
            track_number_list = audio.get("TRCK")
            disc_number_list = audio.get("TPOS")
            if track_number_list:
                if disc_number_list:
                    return f"{disc_number_list.text[0].split("/")[0]}-{track_number_list.text[0].split("/")[0]}"
                else:
                    return track_number_list.text[0]
            else:
                return None
        case ".flac":
            audio = FLAC(filepath)
            track_number_list = audio.get("tracknumber")
            disc_number_list = audio.get("discnumber")
            track_number = track_number_list[0].split("/")[0] if track_number_list else None
            disc_number = disc_number_list[0].split("/")[0] if disc_number_list else None
            if track_number:
                if disc_number:
                    return f"{disc_number}-{track_number}"
                else:
                    return track_number
            else:
                return None
