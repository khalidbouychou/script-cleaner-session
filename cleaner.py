import os
import shutil
from pathlib import Path
import time
def print_header():
    header = """
 _   _  _           _ _     _   ____                      _                
| | | |/ |__   __ _| (_) __| | | __ )  ___  _   _ _   _  | |__   ___  _   _ 
| |_| | '_ \ / _` | | |/ _` | |  _ \ / _ \| | | | | | | | '_ \ / _ \| | | |
|  _  | | | | (_| | | | (_| | | |_) | (_) | |_| | |_| | | | | | (_) | |_| |
|_| |_|_| |_|\__,_|_|_|\__,_| |____/ \___/ \__,_|\__, | |_| |_|\___/ \__,_|
                                                 |___/                     
    """
    print(header)
    print("iMac Cleanup Script")
    print("=" * 50)
    print("Social Media:")
    print("Instagram: @steph")
    print("LinkedIn : khalid bouychou")
    print("Intra    : khbouych")
    print("=" * 50)

def clear_user_caches():
    cache_path = Path.home() / "Library" / "Caches"
    for item in cache_path.iterdir():
        if item.is_dir():
            try:
                shutil.rmtree(item)
            except Exception as e:
                print(f"Error removing {item}: {e}")
        elif item.is_file():
            try:
                os.remove(item)
            except Exception as e:
                print(f"Error removing {item}: {e}")

def clear_downloads():
    downloads_path = Path.home() / "Downloads"
    for item in downloads_path.iterdir():
        if item.is_file():
            try:
                os.remove(item)
            except Exception as e:
                print(f"Error removing {item}: {e}")

def empty_trash():
    trash_path = Path.home() / ".Trash"
    for item in trash_path.iterdir():
        try:
            if item.is_dir():
                shutil.rmtree(item)
            else:
                os.remove(item)
        except Exception as e:
            print(f"Error removing {item} from Trash: {e}")

def main():
    print_header()
    print("\nStarting cleanup process...")
    time.sleep(2)
    print("\nClearing user caches...")
    clear_user_caches()

    print("\nClearing Downloads folder...")
    clear_downloads()
    time.sleep(2)

    print("\nEmptying Trash...")
    empty_trash()

    time.sleep(2)
    print("\nCleanup process completed.")
    print("\nThank you for using the iMac Cleanup Script, Khalid Bouychou!")
    print("Don't forget to follow on Instagram: @steph")

if __name__ == "__main__":
    main()