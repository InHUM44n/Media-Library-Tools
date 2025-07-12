import os
import sys
from pathlib import Path
import argparse

def organize(folderpath:Path, recursive:bool, compress_flac:bool, include_track_number:bool, retain_original:bool, add_release_type:bool):
    for filepath in Path(folderpath).glob('*'):
        # if the file is a directory and recursive mode is enabled, apply actions to the files in that directory recursively.
        if os.path.isdir(filepath) and recursive:
            organize(filepath, True, compress_flac=compress_flac, include_track_number=include_track_number, retain_original=retain_original, add_release_type=add_release_type)
        
def main():
    parser = argparse.ArgumentParser(description="Organize Audio files")

    parser.add_argument(
        "path",
        type=Path,
        help="Path to a file or folder"
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="apply recursively, if applied to a folder"
    )
    parser.add_argument(
        "--include-track-number",
        action="store_true",
        help="Include the track (and disc) number in the filename"
    )
    parser.add_argument(
        "--compress-flac",
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
        help="Add Release type information to metadata, such as"
    )

    args = parser.parse_args()
    
    # Example usage:
    print(f"Input path: {args.path}")
    print(f"Recursive: {args.recursive}")
    print(f"Include track: {args.include_track_number}")
    print(f"Compress FLAC: {args.compress_flac}")
    print(f"Retain original FLAC files: {args.retain_original_flac}")
    print(f"Add Release Type: {args.add_release_type}")
    
    directory = Path(os.getcwd())
    organize(directory, args.recursive, args.compress_flac, args.include_track_number, args.retain_original_flac, args.add_release_type)
    
    