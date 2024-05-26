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
        print (f"{self.FG_RED}RICORDATEMI CHE MANCA L'ESERCIZIO A CHE ORA!!!!{self.RESET}")
        
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
                    "Per produrre con un solo comando l’elenco dei file presenti in una cartella ordinati "
                    "dal più recente al meno recente decidi di installare il seguente alias: ")
    
    def backup(self):
        self.filler('README.md', 'Backup', 
                    "Prima di effettuare una modifica all'interno della cartella ‘foo’"
                    "\ndecidi saggiamente di effettuare una copia di backup chiamata ‘foo.bck’\n")
        os.makedirs(os.path.join(self.playpath, 'Backup', 'foo'), exist_ok=True)
    
    def dove(self):
        self.filler('README.md', 'Dove', 
                    'Ti viene chiesto di verificare la posizione all’interno del' 
                    '\nfilesystem del comando tree e di scrivere il risultato nel file output.txt\n')
   
    def script(self):
        self.filler('README.md', 'Script', 
                    'Un collega ha creato uno script di backup per effettuare operazioni di'
                    '\nmanutenzione.l rendilo eseguibile solo per l’utente.\n')
        script_path = os.path.join(self.playpath, 'Script', 'script.sh')
        os.makedirs(os.path.dirname(script_path), exist_ok=True)
        with open(script_path, 'w') as script:
            script.write('#!/bin/bash\n echo "Hello, World!"')
        
    def lista(self):
        self.filler('README.md', 'Lista', 
                    "'per controllare gli eseguibili installati nel tuo sistema ti veine "
                    "\nchiesto di produrre una lista ordinata senza dettagli, no opzione -l" 
                    "\nalfabeticamente dei file contenuti nella cartella /bin e /usr/bin eliminando"
                    "\ni duplicati e scribere il risultato nel file output.txt'\n")

    def configRete(self):
        self.filler('README.md', 'ConfigRete', 
                    "\n'hai un problema sulla configurazione di rete. Il collega che si occupa di "
                    "\nnetworking ti cheide di produrre l’elelenco senza dettagli delle interfacce di "
                    "\nrete comfiguarae dulla tua macchina (opzione —brief) e di scrivere il risultato" 
                    "\nnel file interfaces.txt'\n")
        
    def fileTemp(self):
        self.filler('README.md', 'FileTemp',"Non ho il testo, ma:"
                    "\n - Cerca i file (nascosti in questo caso) "
                    "\nelimina tutti i file .temp con un comando'\n")
        for x in range(1, 11):
            path = os.path.join(self.playpath, 'FileTemp', f'.autosave_{x}.tmp')
            open(path, 'w').close()
            
    def tarball(self):
        self.filler('README.md', 'Tarball', "Hai scaricato una tarball dal web, decomprimila!")
        path = os.path.join(self.playpath, 'Tarball', 'Im_A_Tarball')
        open(path, 'w').close() 
        extension = '.tar.gz'
        subprocess.run(f'tar -czf {path}{extension} {path} 2>/dev/null',  shell=True )
        os.remove(path)
    
    def traslochi(self):
        self.filler('README.md', 'Traslochi', "per configurare correttamente il sistema è necessario muovere "
                    "\nun po’ di files. Sposta i file bar e biz dentro la cartella /etc/conf."
                    "\ncopia il file foo dentro la cartella /etc/conf\n")
        
        etc_conf_path = os.path.join(self.playpath, 'Traslochi', 'etc', 'conf')
        os.makedirs((etc_conf_path), exist_ok=True)
        files = ['bar', 'biz', 'foo']
        for file in files: 
            path = os.path.join(self.playpath, 'Traslochi', file)
            open(path, 'w').close()
    
    def link(self):
        self.filler('README.md', 'Link', "All’interno di quesat cartella, crea un link simbolico della cartella "
                    "foo e chiamalo bar\n" )
        os.makedirs(os.path.join(self.playpath, 'Link', 'foo'), exist_ok=True)
        
    def rinomina(self):
        self.filler('README.md', 'Rinomina','Rinomina il file foo.txt in foo.md' )        
        path = os.path.join(self.playpath, 'Rinomina', 'foo.txt')
        open(path, 'w').close()

    def user(self):
        self.filler('README.md', 'User', 'aggiungi un nuovo utente foo e ed inseriscilo nel gruppo di backup')
            
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
