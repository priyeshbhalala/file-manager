import os      
import shutil

path_=input("Enter path_")    
list_=os.listdir(path_)   #then using listdir function  we are listing the file names of given path.

# logic of moving files.
for file_ in list_:
  name,ext = os.path.splittext(file_)  #now using splitext function we can split Extension and file name.
  ext = ext[1:]  #then extension name starting from index 1 because 0th index considering '.'that's why we starting from 1.
                  
  if ext =='':   #here we will check extension name is empty or not, if extension name is empty then skip the next code in for loop and goto next iteration.
      continue
  if os.path.exists(path_+'/'+ext):   # from here we are checking extension name of folder is already exist or not, if already exist then moving files otherwise goto for else.
      shutil.move(path_+'/'+file_,path_+'/'+ext+'/'+file_)  # then using shutil.move function we are moving files in seprate folder.
  else:
      os.makedirs(path_+'/'+ext)  #if folder dosen't exist it will create folder for storing sortded folder name.
      shutil.move(path_+'/'+file_,path_+'/'+ext+'/'+file_)   #then using shutil.move we are moving files in seprate folder.