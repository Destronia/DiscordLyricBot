import os

folder_path = '.\lyrics'

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if filename == 'THIS_IS_WHERE_YOUR_LYRICS_GO.txt':
        print(f"Skipping file: {filename}")
        continue  # Skip the specified file

    if os.path.isfile(file_path):
        print(f"Processing file: {filename}")

        # Change the file name to lowercase
        new_filename = filename.lower()
        new_file_path = os.path.join(folder_path, new_filename)

        os.rename(file_path, new_file_path)

        print(f"Renamed to lowercase: {new_filename}")


clear = lambda: os.system('cls')  
clear()

print("All Lyric files have been renamed to lowercase.")

