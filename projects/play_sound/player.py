import os
import sys
import playsound

def play_music(file_path, volume=0.5):
    """
    Plays the given music file or URL via the CLI.

    :param file_path: The path to the music file or the URL to play.
    :param volume: The volume level (default: 0.5).
    """
    if os.path.isfile(file_path):
        playsound.playsound(file_path, volume)
    elif "http" in file_path or "https" in file_path:
        playsound.playsound(file_path, volume)
    else:
        print(f"Error: '{file_path}' is not a valid file path or URL.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python play_music.py [file_path]")
        sys.exit(1)

    file_path = sys.argv[1]
    play_music(file_path) 