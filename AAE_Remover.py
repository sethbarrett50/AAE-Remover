'''
Created by Seth Barrett




This project is designed to remove all files with the extension .AAE. 
These are founnd whenever I back up my iPhone's photos and are annoying lol.

-----------------------------------------------------------------------
Import Statements to Import Used Modules
-----------------------------------------------------------------------
'''
import os
'''
-----------------------------------------------------------------------
Opening Message
-----------------------------------------------------------------------
'''
print(f'\n{"":-^60}\n{"AAE File Remover":-^60}\n{"For iPhone Photo Backup Cleanup":-^60}\n{"Created by Seth Barrett":-^60}\n{"King":-^60}\n{"":-^60}')
'''
-----------------------------------------------------------------------
Show Current Working Directory, Ask for Input and Open Input file, Delete files
-----------------------------------------------------------------------
'''
print(f'Current Working Directory:{os.getcwd()}')
dirs = [ f for f in os.listdir( os.curdir ) if os.path.isdir(f) ]
for dir in dirs:
    print(f'{"-"*5}{dir}')
#Add UIV here
ufolder = str(input('''Please choose the directory wish that contains all the .AAE files:'''))
delfiles = []
for root, dirpath, files in os.walk(ufolder):
    for file in files:
        if (file.lower()).endswith('.aae'):
            delfiles.append(file)
            os.remove(os.path.join(root, file))
'''
-----------------------------------------------------------------------
Exit Message
-----------------------------------------------------------------------
'''
print(f'{"":-^60}\nThe files that were deleted were: {delfiles}\n{"":-^60}\n{"End of AAE Remover":-^60}\n{"":-^60}')

