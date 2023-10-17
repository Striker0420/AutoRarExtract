import os
import sys
import subprocess
import time

def process(folder_path):
    """
    Process the downloaded folder and extract all RAR files in it.
    """
    for root, _, files in os.walk(folder_path):
        for file in files:
            _, file_extension = os.path.splitext(file)

            if file_extension.lower() == ".rar":
                file_path = os.path.join(root, file)
                try:
                    # Delay before extraction (in seconds)
                    delay = 15
                    time.sleep(delay)

                    subprocess.run(['7z', 'x', file_path, f'-o{root}'])
                    print(f"Extracted: {file_path}")
                except Exception as e:
                    print(f"Error extracting {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python qbt_auto_unrar.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    process(folder_path)
