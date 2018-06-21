# Launcher defines our changes to builtins then runs app/main.py
import subprocess, os, configparser, builtins, imp

# Store project absolute path in global __builtins__
builtins.absolute = os.path.dirname(os.path.abspath(__file__)) # global variable for absolute path imports

def projectRelativeImport(fileName, projectRelativePath, moduleName = None):
    if moduleName is None:
        moduleName = fileName.title()

    path = builtins.absolute + projectRelativePath
    if type(path) != 'list':
        path = [path]

    module = imp.find_module(fileName, path)
    imp.load_module(moduleName, module)

builtins.projectRelativeImport = projectRelativeImport # new global function for importing using project relative path

# Launch scraper/crawler. Unecisarrily use our previously defined projectRelativeImport function for consistancy
projectRelativeImport('main','/app')
