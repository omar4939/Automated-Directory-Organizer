import os


current_path= os.getcwd()
all_files = os.listdir()

image_files= os.path.join(current_path, "Images")
documents_files= os.path.join(current_path, "Documment")
programing = os.path.join(current_path, "Programing")
vidos_files= os.path.join(current_path, "Vidos")
othors_files= os.path.join(current_path, "Othors")
audio_path= os.path.join(current_path, "Audio")
compressed_path= os.path.join(current_path, "Compressed")

IMAGE_EXTENSIONS = ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp"
DOC_EXTENSIONS = ".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".csv"
ARCHIVE_EXTENSIONS = ".zip", ".rar", ".7z", ".tar", ".gz"
VIDEO_EXTENSIONS = ".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"
AUDIO_EXTENSIONS = ".mp3", ".wav", ".aac", ".flac", ".ogg"

def orginaze_file(current_path, image_files, documents_files, programing, vidos_files, othors_files, audio_path, compressed_path):


    if len(all_files) == 0:
        print("Empty file")
        return
    
    for rename_files in all_files:

        if rename_files == "test01.py":
            continue

        if rename_files.endswith(IMAGE_EXTENSIONS):

            if not os.path.exists(image_files):
                os.mkdir("Images")
            
            old_path= os.path.join(current_path, rename_files)
            now_path= os.path.join(image_files, rename_files)
            os.rename(old_path, now_path)
            print(f"Success: Moved {rename_files} to {image_files}")

        elif rename_files.endswith(DOC_EXTENSIONS):

            if not os.path.exists(documents_files):
                os.mkdir("Documment")

            old_path= os.path.join(current_path, rename_files)
            now_path= os.path.join(documents_files, rename_files)
            os.rename(old_path, now_path)
            print(f"Success: Moved {rename_files} to {documents_files}")

        elif rename_files.endswith(".py"):

            if not os.path.exists(programing):
                os.mkdir("Programing")

            old_path= os.path.join(current_path, rename_files)
            now_path= os.path.join(programing, rename_files)
            os.rename(old_path, now_path)
            print(f"Success: Moved {rename_files} to {programing}")

        elif rename_files.endswith(VIDEO_EXTENSIONS):

            if not os.path.exists(vidos_files):
                os.mkdir("Vidos")

            old_path= os.path.join(current_path, rename_files)
            now_path= os.path.join(vidos_files, rename_files)
            os.rename(old_path, now_path)
            print(f"Success: Moved {rename_files} to {vidos_files}")
        
        elif rename_files.endswith(AUDIO_EXTENSIONS):

            if not os.path.exists(audio_path):
                os.mkdir("Audio")

            old_path= os.path.join(current_path, rename_files)
            now_path= os.path.join(audio_path, rename_files)
            os.rename(old_path, now_path)
            print(f"Success: Moved {rename_files} to {audio_path}")

        elif rename_files.endswith(ARCHIVE_EXTENSIONS):

            if not os.path.exists(compressed_path):
                os.mkdir("Compressed")

            old_path= os.path.join(current_path, rename_files)
            now_path= os.path.join(compressed_path, rename_files)
            os.rename(old_path, now_path)
            print(f"Success: Moved {rename_files} to {compressed_path}")

        else:
            if not os.path.exists(othors_files):
                os.mkdir("Othors")

            old_path= os.path.join(current_path, rename_files)
            now_path= os.path.join(othors_files, rename_files)
            os.rename(old_path, now_path)
            print(f"Success: Moved {rename_files} to {othors_files}")


orginaze_file(current_path, image_files, documents_files, programing, vidos_files, othors_files, audio_path, compressed_path)

print("Successful All Files")