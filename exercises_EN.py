
import os
import subprocess

class Exam():
    def __init__(self):
        self.start = None
        self.result = subprocess.run("pwd", capture_output=True, text=True)
        self.root = self.result.stdout.strip()  
        self.playpath = os.path.join(self.root, 'playground')

        self.FG_BLACK = '\033[30m'
        self.FG_RED = '\033[31m'
        self.FG_GREEN = '\033[92m'
        self.FG_YELLOW = '\033[33m'
        self.FG_BLUE = '\033[34m'
        self.FG_MAGENTA = '\033[35m'
        self.FG_CYAN = '\033[36m'
        self.FG_WHITE = '\033[37m'
        self.RESET = '\033[0m'
        
    def banner(self):
        print("""
 █████ █████       █████ █████          ███  ████████ 
░░███ ░░███       ░░███ ░░███         ███░  ███░░░░███
 ░███  ░███        ░░███ ███        ███░   ░░░    ░███
 ░███  ░███         ░░█████       ███░        ██████░ 
 ░███  ░███          ░░███       ░░░███      ░░░░░░███
 ░███  ░███      █    ░███         ░░░███   ███   ░███
 █████ ███████████    █████          ░░░███░░████████ 
░░░░░ ░░░░░░░░░░░    ░░░░░             ░░░  ░░░░░░░░  
""")
        
    def dirCheck(self):
        print("\nChecking if PLAYGROUND already exists...")
        result = subprocess.run("pwd", capture_output=True, text=True)
        root = result.stdout.strip()  
        playground_path = os.path.join(root, 'playground')

        playground_found = False

        for dirpath, dirnames, filenames in os.walk(root):
            if 'playground' in dirnames:
                playground_found = True
                print(f"{self.FG_RED}\nFOUND OLD PLAYGROUND{self.RESET}")
                print('\nRemoving old playground')
                print(f'\n{self.FG_GREEN}CREATING NEW PLAYGROUND{self.RESET}')

                subprocess.run(['rm', '-rf', playground_path], check=True)
                break
            
        if not playground_found:
            print(f'{self.FG_GREEN}No playground found, creating one....{self.RESET}')
            os.makedirs(playground_path)        

    def filler(self, filename, subdirName, readmefill):
        subdir = os.path.join(self.playpath, subdirName)
        os.makedirs(subdir, exist_ok=True)  # Ensure directory is created if it doesn't exist
        file_path = os.path.join(subdir, filename)

        with open(file_path, 'w') as file:
            file.write(readmefill)

    def alias(self):
        self.filler('README.md', 'Alias', 
                    "To produce a list of files in a folder ordered "
                    "from most recent to least recent with a single command, you decide to install the following alias: ")
    
    def backup(self):
        self.filler('README.md', 'Backup', 
                    "Before making any changes inside the 'foo' folder,"
                    "\nwisely decide to create a backup copy called 'foo.bck'\n")
        os.makedirs(os.path.join(self.playpath, 'Backup', 'foo'), exist_ok=True)
    
    def dove(self):
        self.filler('README.md', 'Dove', 
                    'You are asked to verify the location within the' 
                    '\nfilesystem of the tree command and to write the result in the output.txt file\n')
   
    def script(self):
        self.filler('README.md', 'Script', 
                    'A colleague has created a backup script for performing maintenance operations.'
                    '\nMake it executable only for the user.\n')
        script_path = os.path.join(self.playpath, 'Script', 'script.sh')
        os.makedirs(os.path.dirname(script_path), exist_ok=True)
        with open(script_path, 'w') as script:
            script.write('#!/bin/bash\n echo "Hello, World!"')
        
    def lista(self):
        self.filler('README.md', 'Lista', 
                    "'To check the executables installed on your system, you are asked to produce a list"
                    "\nordered without details, no -l option, alphabetically of the files contained in the /bin and /usr/bin directories,"
                    "\neliminating duplicates and writing the result in the output.txt file'\n")

    def configRete(self):
        self.filler('README.md', 'ConfigRete', 
                    "\n'You have a network configuration problem. The colleague who handles networking asks you to produce a list"
                    "\nwithout details of the network interfaces configured on your machine (option --brief) and to write the result"
                    "\nin the interfaces.txt file'\n")
        
    def fileTemp(self):
        self.filler('README.md', 'FileTemp',"I don't have the text, but:"
                    "\n - Search for hidden files (in this case) "
                    "\nand delete all .temp files with a command'\n")
        for x in range(1, 11):
            path = os.path.join(self.playpath, 'FileTemp', f'.autosave_{x}.tmp')
            open(path, 'w').close()
            
    def tarball(self):
        self.filler('README.md', 'Tarball', "You downloaded a tarball from the web, decompress it!")
        path = os.path.join(self.playpath, 'Tarball', 'Im_A_Tarball')
        open(path, 'w').close() 
        extension = '.tar.gz'
        subprocess.run(f'tar -czf {path}{extension} {path} 2>/dev/null',  shell=True )
        os.remove(path)
    
    def traslochi(self):
        self.filler('README.md', 'Traslochi', "To configure the system correctly, you need to move "
                    "\na few files. Move the files bar and biz into the /etc/conf directory."
                    "\nCopy the file foo into the /etc/conf directory\n")
        
        etc_conf_path = os.path.join(self.playpath, 'Traslochi', 'etc', 'conf')
        os.makedirs((etc_conf_path), exist_ok=True)
        files = ['bar', 'biz', 'foo']
        for file in files: 
            path = os.path.join(self.playpath, 'Traslochi', file)
            open(path, 'w').close()
    
    def link(self):
        self.filler('README.md', 'Link', "Within this folder, create a symbolic link to the folder "
                    "foo and name it bar\n" )
        os.makedirs(os.path.join(self.playpath, 'Link', 'foo'), exist_ok=True)
        
    def rinomina(self):
        self.filler('README.md', 'Rinomina','Rename the file foo.txt to foo.md' )        
        path = os.path.join(self.playpath, 'Rinomina', 'foo.txt')
        open(path, 'w').close()

    def user(self):
        self.filler('README.md', 'User', 'Add a new user foo and add them to the backup group')
            
    def starter(self):
        self.alias()   
        self.backup()
        self.dove()
        self.script()
        self.lista()
        self.configRete()
        self.fileTemp()
        self.tarball()
        self.traslochi()
        self.link()
        self.rinomina() 
        self.user()
        
def main():
    e = Exam()
    e.banner()
    e.dirCheck()
    e.starter()
    
if __name__ == '__main__':
    main()
