import os, sys,shutil

def desktop_files():
    extensions_to_ignore = [".lnk", ".url"]
    parent_folders = ["audio", "text", "images", "junk", "executables", "folders", "video"]
    images_folders = [".png", ".gif", ".jpeg"] #, ".jpg"
    audio_folders = [".wav", ".mp3"]
    text_folders = [".txt", ".docx", ".pdf"]
    executables_folders = ['.exe', ".bat", ".vbs"]
    videos_folders = [".mp4", ".mov"]

    organize_unordered_folders = False 
    desktop_path = os.environ['USERPROFILE'] + "\\Desktop\\"

    if not os.path.isdir(desktop_path + "Files") : os.mkdir(desktop_path + "Files")

    for pfolder in parent_folders:
        if not os.path.isdir(desktop_path + "Files\\" + pfolder) : os.mkdir(desktop_path + "Files\\" + pfolder)

        if pfolder == "audio":
            for afolders in audio_folders:
                if not os.path.isdir(desktop_path + "Files\\" + pfolder + "\\" + afolders) : os.mkdir(desktop_path + "Files\\" + pfolder + "\\" + afolders)

        elif pfolder == "text":
            for tfolders in text_folders:
                if not os.path.isdir(desktop_path + "Files\\" + pfolder + "\\" + tfolders) : os.mkdir(desktop_path + "Files\\" + pfolder + "\\" + tfolders)

        elif pfolder == "images":
            for ifolders in images_folders:
                if not os.path.isdir(desktop_path + "Files\\" + pfolder + "\\" + ifolders) : os.mkdir(desktop_path + "Files\\" + pfolder + "\\" + ifolders)

        elif pfolder == "executables":
            for efolders in executables_folders:
                if not os.path.isdir(desktop_path + "Files\\" + pfolder + "\\" + efolders) : os.mkdir(desktop_path + "Files\\" + pfolder + "\\" + efolders)

        elif pfolder == "video":
            for vfolders in videos_folders:
                if not os.path.isdir(desktop_path + "Files\\" + pfolder + "\\" + vfolders) : os.mkdir(desktop_path + "Files\\" + pfolder + "\\" + vfolders)


    for file in os.listdir(desktop_path):
        valid_file = True
        for extension in extensions_to_ignore:
            if extension in file:
                valid_file = False

        if not valid_file : continue
        if file.lower() == "files" : continue

        if ".jpeg" in file or ".jpg" in file:
            shutil.move(desktop_path+file, desktop_path+"Files\\"+"images\\"+".jpeg\\" + file)
            #print(desktop_path+file + " -> " + desktop_path+"Files\\"+"images\\"+".jpeg\\" + file)
        elif ".png" in file:
            shutil.move(desktop_path+file, desktop_path+"Files\\"+"images\\"+".png\\" + file)

        elif ".gif" in file:
            shutil.move(desktop_path+file, desktop_path+"Files\\"+"images\\"+".png\\" + file)

        elif ".wav" in file:
            shutil.move(desktop_path+file, desktop_path+"Files\\"+"audio\\"+".wav\\" + file)

        elif ".mp3" in file:
            shutil.move(desktop_path+file, desktop_path+"Files\\"+"audio\\"+".mp3\\" + file)

        elif ".txt" in file:
            shutil.move(desktop_path+file, desktop_path+"Files\\"+"text\\"+".txt\\" + file)

        elif ".docx" in file:
            shutil.move(desktop_path+file, desktop_path+"Files\\"+"text\\"+".docx\\" + file)

        elif ".pdf" in file:
            shutil.move(desktop_path+file, desktop_path+"Files\\"+"text\\"+".pdf\\" + file)

        elif ".exe" in file:
            shutil.move(desktop_path+file, desktop_path+"Files\\"+"executables\\"+".exe\\" + file)

        elif ".bat" in file:
            shutil.move(desktop_path+file, desktop_path+"Files\\"+"executables\\"+".bat\\" + file)

        elif ".vbs" in file:
            shutil.move(desktop_path+file, desktop_path+"Files\\"+"executables\\"+".vbs\\" + file)

        elif ".mp4" in file:
            shutil.move(desktop_path+file, desktop_path+"Files\\"+"video\\"+".mp4\\" + file)

        elif ".mov" in file:
            shutil.move(desktop_path+file, desktop_path+"Files\\"+"video\\"+".mov\\" + file)

        elif os.path.isdir(desktop_path+file):
            shutil.move(desktop_path+file, desktop_path+"Files\\"+"folders\\"+ file)
            
        else:
            shutil.move(desktop_path+file, desktop_path+"Files\\"+"junk\\"+ file)

        print(file) #moved files

if __name__ == "__main__":
    desktop_files()
