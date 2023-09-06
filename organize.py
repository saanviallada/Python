import os
import shutil

From = "/Users/saanviallada/Desktop/Python/FROM"
To = "/Users/saanviallada/Desktop/Python/TO"

list = os.listdir(From)
print(list)

for file in list :
    name, extension = os.path.splitext(file)
    print(name,extension)
    if(extension==""):
        continue
    elif(extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']):
        print(1)
        path1 = From+"/"+file
        path2 = To+"/"+"images"
        path3 = To+"/"+"images"+"/"+file
        if(os.path.exists(path2)):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
    elif(extension in ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],):
        print(1)
        path4 = From+"/"+file
        path5 = To+"/"+"videos"
        path6 = To+"/"+"videos"+"/"+file
        if(os.path.exists(path5)):
            shutil.move(path4,path6)
        else:
            os.makedirs(path5)
            shutil.move(path4,path6)
    elif(extension in ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],):
        print(1)
        path7 = From+"/"+file
        path8 = To+"/"+"document"
        path9 = To+"/"+"document"+"/"+file
        if(os.path.exists(path8)):
            shutil.move(path7,path9)
        else:
            os.makedirs(path8)
            shutil.move(path7,path9)
    elif(extension in ['.exe', '.bin', '.cmd', '.msi', '.dmg'],):
        print(1)
        path10 = From+"/"+file
        path11 = To+"/"+"setup"
        path12 = To+"/"+"setup"+"/"+file
        if(os.path.exists(path11)):
            shutil.move(path10,path12)
        else:
            os.makedirs(path11)
            shutil.move(path10,path12)
            