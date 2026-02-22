#!/usr/bin/env python3
"""
MP3 File Organizer
Organizes MP3 files by album metadata.
"""

import os
import shutil
from pathlib import Path
import mutagen
from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError


def get_album_info(mp3_path):
    """Extract album information from MP3 file."""
    try:
        audio = MP3(mp3_path)
        # Try to get album from ID3 tags
        if 'TALB' in audio:
            return str(audio['TALB'])
        elif 'TPE1' in audio:  # Fallback to artist if no album
            return str(audio['TPE1'])
        else:
            return "Unknown_Album"
    except (ID3NoHeaderError, Exception):
        # If no ID3 tags, use filename as album name
        return Path(mp3_path).stem


def organize_mp3_files(base_dir="."):
    """
    Organize MP3 files by album.
    1. Find all MP3 files
    2. Move them to 'unsorted' folder
    3. Delete other folders
    4. Organize by album
    """
    base_path = Path(base_dir).resolve()
    unsorted_dir = base_path / "unsorted"
    
    print(f"Working in directory: {base_path}")
    
    # Step 1: Find all MP3 files
    print("Finding all MP3 files...")
    mp3_files = list(base_path.rglob("*.mp3"))
    print(f"Found {len(mp3_files)} MP3 files")
    
    if not mp3_files:
        print("No MP3 files found!")
        return
    
    # Step 2: Create unsorted directory and move all MP3 files there
    print("Creating unsorted directory...")
    unsorted_dir.mkdir(exist_ok=True)
    
    print("Moving all MP3 files to unsorted directory...")
    for mp3_file in mp3_files:
        if mp3_file.parent != unsorted_dir:
            dest = unsorted_dir / mp3_file.name
            # Handle duplicate filenames
            counter = 1
            while dest.exists():
                stem = mp3_file.stem
                suffix = mp3_file.suffix
                dest = unsorted_dir / f"{stem}_{counter}{suffix}"
                counter += 1
            
            print(f"Moving: {mp3_file.name} -> {dest.name}")
            shutil.move(str(mp3_file), str(dest))
    
    # Step 3: Delete other folders (excluding unsorted and hidden folders)
    print("Deleting other folders...")
    for item in base_path.iterdir():
        if item.is_dir() and item.name != "unsorted" and not item.name.startswith('.'):
            print(f"Deleting folder: {item.name}")
            shutil.rmtree(item)
    
    # Step 4: Organize files by album
    print("Organizing files by album...")
    mp3_files_in_unsorted = list(unsorted_dir.glob("*.mp3"))
    
    for mp3_file in mp3_files_in_unsorted:
        album_name = get_album_info(mp3_file)
        
        # Clean album name for filesystem
        album_name = "".join(c for c in album_name if c.isalnum() or c in (' ', '-', '_')).strip()
        if not album_name:
            album_name = "Unknown_Album"
        
        album_dir = base_path / album_name
        album_dir.mkdir(exist_ok=True)
        
        dest = album_dir / mp3_file.name
        # Handle duplicate filenames
        counter = 1
        while dest.exists():
            stem = mp3_file.stem
            suffix = mp3_file.suffix
            dest = album_dir / f"{stem}_{counter}{suffix}"
            counter += 1
        
        print(f"Organizing: {mp3_file.name} -> {album_name}/{dest.name}")
        shutil.move(str(mp3_file), str(dest))
    
    # Clean up unsorted directory if empty
    try:
        unsorted_dir.rmdir()
        print("Removed empty unsorted directory")
    except OSError:
        print("Unsorted directory not empty or contains files")
    
    print("MP3 organization complete!")


if __name__ == "__main__":
    import sys
    
    # Check if mutagen is installed
    try:
        import mutagen
    except ImportError:
        print("Installing required package: mutagen")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "mutagen"])
        import mutagen
    
    # Allow specifying directory as command line argument
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    organize_mp3_files(target_dir)
