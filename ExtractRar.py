import os
import sys
import subprocess
import time

def process(folder_path):
    """
    Process the downloaded folder and extract all RAR files in it.
    """
    # Specify the full path to the 7-Zip executable
    seven_zip_path = r'C:\Program Files\7-Zip\7z.exe'

    for root, _, files in os.walk(folder_path):
        for file in files:
            _, file_extension = os.path.splitext(file)

            if file_extension.lower() == ".rar":
                file_path = os.path.join(root, file)
                try:
                    # Delay before extraction (in seconds)
                    delay = 10
                    time.sleep(delay)

                    print(f"Extracting: {file_path}")
                    
                    # Use the full path to 7-Zip executable
                    subprocess.run([seven_zip_path, 'x', file_path, f'-o{root}'])
                    
                    print(f"Extracted: {file_path}")
                except Exception as e:
                    print(f"Error extracting {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python qbt_auto_unrar.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    process(folder_path)
