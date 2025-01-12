### FILE EXTENSIONS
# https://cs50.harvard.edu/python/2022/psets/1/extensions/

# Implement a program that prompts the user for the name of a file and then outputs the file’s media type based on its extension.
# For example, if the input is "cat.jpg", the output should be "image/jpeg".

# Be sure to handle different file extensions and their corresponding media types.

def main():
    while True:
        file = input("Enter the name of a file: ")
        if not input_validity(file):
            print("Invalid file name.")
        else:
            print(extension(file))
            break

def input_validity(file):
    if "." not in file or file.startswith(".") or file.endswith("."):
        return False
    return True

def extension(file):
    file_ext = file.rsplit(".", 1)[-1]
    media_types = {
        "jpg": "image/jpeg",
        "pdf": "application/pdf",
        "mp3": "audio/mpeg",
        "mp4": "video/mp4"
    }

    return media_types.get(file_ext, "application/octet-stream")

if __name__ == "__main__":
    main()