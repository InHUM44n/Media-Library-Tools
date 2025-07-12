# Media Library Tools

This is a collection of scripts I wrote to organize my media library. Maybe it's of use to someone out there.

## Installing the requirements

```
pip install -r requirements.txt
```

Installing ffmpeg at the system-level is required for flac to mp3 conversion.

## Functionality and Usage

### Recursive conversion of FLAC to MP3

This converts all FLAC files in the current directory and all subdirectories into MP3. ffmpeg is required here.
```
python path/to/convert_all_flac_to_mp3.py
```

### Renaming all audio files to their Title

This script fetches the track title from the metadata and renames the file to it.
```
python path/to/rename_audio_to_title.py
```
