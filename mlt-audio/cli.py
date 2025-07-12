import os
import sys
from pathlib import Path
import argparse

def apply(folderpath:Path, recursive:bool, compress_flac:bool, include_track_number:bool):
    for filepath in Path(folderpath).glob('*'):
        # if the file is a directory and recursive mode is enabled, apply actions to the files in that directory recursively.
        if os.path.isdir(filepath) and recursive:
            apply(filepath, True, compress_flac=compress_flac, include_track_number=include_track_number)
        

def main():
    parser = argparse.ArgumentParser(description="Organize Audio files")

    parser.add_argument(
        "path",
        type=Path,
        help="Path to a file or folder"
    )
    parser.add_argument(
        "--recursive",
        action="true_true",
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

    args = parser.parse_args()
    
    if sys.argv == 1:
        parser.error("No arguments provided. Use --help to see available options.")
    
    # Example usage:
    print(f"Input path: {args.path}")
    print(f"Recursive: {args.recursive}")
    print(f"Compress FLAC: {args.compress_flac}")
    print(f"Include track: {args.include_track_number}")
    
    directory = Path(os.getcwd())
    apply(directory, args.recursive, args.compress_flac, args.include_track_number)
    
    