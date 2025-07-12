# Media Library Tools

This is a collection of scripts I wrote to organize my media library. Maybe it's of use to someone out there.

## Installing

```
git clone https://github.com/InHUM44n/Media-Library-Tools
cd Media-Library-Tools
pip install .
```

Installing ffmpeg at the system-level is required for flac to mp3 compression.

## Functionality and Usage

### Audio Organizer

This converts all FLAC files in the current directory and all subdirectories into MP3. ffmpeg is required here.
```
mlt-audio <options> path/to/folder-or-file
```
Options:
```
-r, --recursive:            apply recursively, if applied to a folder
--rename-to-title:          Fetch the Title from Metadata and rename the file accordingly.
--include-track-number:     Include the track (and disc) number in the filename.
                            Only works with --rename-to-title, since the name would otherwise endlessly expand with repeated use.
-c, --compress-flac:        Compress FLAC files to MP3 files.
--retain-original-flac:     Do not delete the original files after conversion. Only works with --compress-flac.
```
Future Functionality:
```
--add-release-type:         Automatically add release type information to metadata, either "Single", "EP" or "Album"
                            1-2 Tracks -> Single
                            3-5 Tracks -> EP
                            6+  Tracks -> Album
                            Yes, this is completely arbitrary and manual changes will be necessary if you plan to tag your entire library with this.
--remove-non-ascii:         Remove Non-ASCII Characters from the Filename.
--strip-cover:              Extract the cover art from the metadata and store it as cover.jpg to save on storage.
```