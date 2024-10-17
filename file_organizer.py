import os
import pathlib
import shutil

'''
Different type of file formats
'''

fileFormat = {
"Web": [".html5", ".html", ".htm", ".xhtml",".csv",".webp",".acsm"],

"Picture": [".jpeg", ".jpg", ".tiff", ".gif",".heic",".HEIC"
             ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],

"Video": [".avi", ".mkv", ".flv", ".wmv",
          ".mov", ".mp4", "..webm", ". vob",
          ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],

"Document": [".oxps", ".epub", ".pages", ".docx",
              ".txt", ".pdf", ".doc", ".fdf",
              ".ods", ".odt", ".pwi", ". xsn",
              ". xps" , ".dotx", ".docm", ".dox",
              ".rvg", ".rtf", ".rtfd", ".wpd",
              ".xls", ".xlsx", ".ppt", "pptx" , ".md"],
"PPT" : [".pptx"],

"Compressed": [".a", ".ar", ".cpio", ".iso",
                ".tar", ".gz", ".rz", ".7z",
                ".dmg", ".rar", ".xar", ".zip",
                ".msi",".msix"],

"Audio": [".aac", ".aa", ".aac", ".dvf",
          ".m4a", ".m4b", ".m4p", ".mp3",
           ".msv", "ogg", "oga", ".raw", 
          ".vox", ".wav", ".wma", "aiff"],

"Torrent":[".srt",".torrent"],

"Installable":[".exe"],

"apk":[".apk"],

"c_cpp":[".c",".cpp"],

"python":[".py",".ipynb"],

"JSON":[".json"],

"font_style":[".otf"],

"CSV_XL" : [".csv",".xlsx",".xlsm","xlsb"]

}

fileTypes = list(fileFormat.keys())
fileFormats= list(fileFormat.values())

def organizer(directory):
    
    files_of_the_folder = os.listdir(directory)
    directory += '/'
    
    for file in files_of_the_folder:
        fileName = pathlib.Path(file)
        fileFormatType = fileName.suffix.lower()
        
        if (fileName != "file_organizer" and fileFormatType != ".py"): #to exclude file_organizer.py file
            src = directory + str(fileName)
            destination = directory + "Other"
            
            if fileFormatType == "":
                print(f"{src} has no file Format")
            else:
                for formats in fileFormats:
                    
                    if fileFormatType in formats:
                        folder = fileTypes[fileFormats.index(formats)]
                        
                        if os.path.isdir(directory + folder) == False:
                            os.mkdir(directory + folder)
                        destination = directory + folder 
                        
                else:
                    if os.path.isdir("Other") == False:
                        os.mkdir(destination + "Other")
                print(src, "  ----------moved to-------->  ", destination, ",")
                try:
                    shutil.move(src, destination)
                except:
                    continue
        else:
            pass
        
    print("Files are organized.... files with uncommon extensions might be store in 'Others' folder. Please Check....")


while(True):
    choices = input("Would you like to organize: \n1. Current file directory?(type 1/Y) \n2. Different directory?(type 2/N) \n3. Type '3/exit' to exit \nYOUR CHOICE : ")
    print()
    if choices.upper() == 'Y' or choices == '1' :
        organizer(os.getcwd())
        break

    elif choices.upper() == 'N' or choices == '2':
        path = input("Specify the path of the Directory(Folder) you want to organize : ")
        if os.path.exists(path):
            print(" The path exists.\n")
            organizer(path)
            break
        
        else:
            print("The path does not exist.\n")
            continue
        
    elif choices.upper() == 'EXIT' or choices == '3':
        print("Exiting...")
        break
    else:
        continue

