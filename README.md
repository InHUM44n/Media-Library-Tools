# Media Library Tools

This is a collection of scripts I wrote to organize my media library. Maybe it's of use to someone out there.

## Installing

```
git clone https://github.com/InHUM44n/Media-Library-Tools
cd Media_Library_Tools
pip install .
```

Installing ffmpeg at the system-level is required for flac to mp3 compression.

## Functionality and Usage

### Audio Organizer

This converts all FLAC files in the current directory and all subdirectories into MP3. ffmpeg is required here.
```
mlt-audio path/to/folder-or-file <options>
```
Options:
```
--recursive:                apply recursively, if applied to a folder
--include-track-number:     Include the track (and disc) number in the filename
--compress-flac:            Compress FLAC files to MP3 files
--retain-original-flac:     Do not delete the original files after conversion
--add-release-type:         Add Release type information to metadata, such as
```