#!/usr/bin/env python3
"""
Script to help translate places from Polish to English.
This script will read Polish content and help generate English translations.
"""

import os
import glob
import json
from pathlib import Path

def find_places_missing_english():
    """Find all places that are missing English translations."""
    places_missing_en = []
    
    # Find all content directories
    content_dirs = glob.glob("sections/*/places/*/content")
    
    for content_dir in content_dirs:
        pl_dir = os.path.join(content_dir, "pl")
        en_dir = os.path.join(content_dir, "en")
        
        if os.path.exists(pl_dir) and not os.path.exists(en_dir):
            place_name = content_dir.split("/")[-2]
            places_missing_en.append((place_name, content_dir))
    
    return places_missing_en

def read_polish_content(content_dir):
    """Read all Polish content files for a place."""
    pl_dir = os.path.join(content_dir, "pl")
    content = {}
    
    if not os.path.exists(pl_dir):
        return content
    
    # Read all .txt files
    txt_files = glob.glob(os.path.join(pl_dir, "*.txt"))
    
    for txt_file in txt_files:
        filename = os.path.basename(txt_file)
        try:
            with open(txt_file, 'r', encoding='utf-8') as f:
                content[filename] = f.read().strip()
        except Exception as e:
            print(f"Error reading {txt_file}: {e}")
    
    return content

def create_english_translation(place_name, content_dir, polish_content):
    """Create English translation directory and files."""
    en_dir = os.path.join(content_dir, "en")
    
    # Create English directory
    os.makedirs(en_dir, exist_ok=True)
    
    print(f"\n=== Translating {place_name} ===")
    print(f"Creating English translation in: {en_dir}")
    
    # Process each file
    for filename, polish_text in polish_content.items():
        print(f"\n--- {filename} ---")
        print(f"Polish: {polish_text}")
        
        # For now, just create placeholder files
        # In a real scenario, you would use a translation service or manual translation
        english_text = f"[ENGLISH TRANSLATION NEEDED: {polish_text}]"
        
        en_file = os.path.join(en_dir, filename)
        with open(en_file, 'w', encoding='utf-8') as f:
            f.write(english_text)
        
        print(f"Created: {en_file}")

def main():
    """Main function to process all places missing English translations."""
    print("Finding places missing English translations...")
    
    places_missing_en = find_places_missing_english()
    
    print(f"Found {len(places_missing_en)} places missing English translations:")
    for place_name, content_dir in places_missing_en:
        print(f"  - {place_name}")
    
    # Process first 5 places as an example
    print(f"\nProcessing first 5 places as an example...")
    
    for i, (place_name, content_dir) in enumerate(places_missing_en[:5]):
        print(f"\n{i+1}/5: Processing {place_name}")
        
        polish_content = read_polish_content(content_dir)
        if polish_content:
            create_english_translation(place_name, content_dir, polish_content)
        else:
            print(f"No Polish content found for {place_name}")

if __name__ == "__main__":
    main() 