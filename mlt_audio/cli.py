import os
from pathlib import Path
import argparse
import subprocess

SUPPORTED_AUDIO_EXTENSIONS:tuple[str, ...] = (".mp3", ".flac")

def organize(folderpath:Path, recursive:bool, compress_flac:bool, retain_original:bool, rename_to_title:bool, include_track_number:bool, add_release_type:bool):
    # iterate over all files in the given directory
    for filepath in Path(folderpath).glob('*'):
        filepath_string = os.fsdecode(filepath)
        # if the file is a directory and recursive mode is enabled, apply actions to the files in that directory recursively.
        if os.path.isdir(filepath) and recursive:
            organize(
                folderpath=filepath,
                recursive=True,
                compress_flac=compress_flac,
                retain_original=retain_original,
                rename_to_title=rename_to_title,
                include_track_number=include_track_number,
                add_release_type=add_release_type)
        # if the file is an audio file
        elif os.path.isfile(filepath) and filepath_string.endswith(SUPPORTED_AUDIO_EXTENSIONS):
            print(f"Found audio file: {filepath_string}")
            output_folder = filepath.parent
            tracktitle = filepath.stem
            extension = filepath.suffix
            # file renaming section
            if rename_to_title:
                from .metadata_helper import fetch_title
                tracktitle = fetch_title(filepath)
                if include_track_number:
                    from .metadata_helper import fetch_track_number_string
                    track_disc_and_number = fetch_track_number_string(filepath)
                    tracktitle = f"{track_disc_and_number} {tracktitle}"
                renamed_path = f"{output_folder}/{tracktitle}{extension}"
                if not os.path.exists(renamed_path):
                    os.rename(filepath, renamed_path)
                    filepath = Path(renamed_path)
                else:
                    if filepath == renamed_path:
                        print("Skipped renaming, as it already named correctly")
                    else:
                        print("Skipped file renaming, as a file with that name already exists.")
            # FLAC compression section
            if extension==".flac" and compress_flac:
                output_path = f"{output_folder}/{tracktitle}.mp3"
                if not os.path.exists(output_path):
                    print("Compressing flac to mp3...")
                    subprocess.run(
                        [ "ffmpeg", "-i", filepath, "-ab", "192k", output_path ],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.PIPE
                    )
                    if not retain_original: os.remove(filepath)
                    filepath = Path(output_path)
                else:
                    print("Skipped compression, as mp3 file already exists.")
            # metadata modification section
            if add_release_type:
                # TODO: Add functionality for automatic addition of release type
                pass
        # skip all unsupported and non-audio files
        else:
            print(f"Skipped non-audio file: {filepath_string}")
def main():
    parser = argparse.ArgumentParser(description="Organize Audio files")

    parser.add_argument(
        "path",
        type=Path,
        help="Path to a file or folder"
    )
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="apply recursively, if applied to a folder"
    )
    parser.add_argument(
        "--rename-to-title",
        action="store_true",
        help="Fetch the track title from its Metadata and rename the file to it"
    )
    parser.add_argument(
        "--include-track-number",
        action="store_true",
        help="Include the track (and disc) number in the filename"
    )
    parser.add_argument(
        "-c", "--compress-flac",
        action="store_true",
        help="Compress FLAC files to MP3 files"
    )
    parser.add_argument(
        "--retain-original-flac",
        action="store_true",
        help="Do not delete the original files after conversion"
    )
    parser.add_argument(
        "--add-release-type",
        action="store_true",
        help="Automatically add release type information to metadata, like \"Album\", \"EP\" or \"Single\""
    )
    parser.add_argument(
        "--remove-non-ascii",
        action="store_true",
        help="Remove Non-ASCII Characters from the Filename."
    )
    parser.add_argument(
        "--strip-cover",
        action="store_true",
        help="Extract the cover art from the metadata and store it as cover.jpg."
    )

    args = parser.parse_args()
    
    organize(
        folderpath=args.path,
        recursive=args.recursive,
        compress_flac=args.compress_flac,
        rename_to_title=args.rename_to_title,
        include_track_number=args.include_track_number,
        retain_original=args.retain_original_flac,
        add_release_type=args.add_release_type)
    
    