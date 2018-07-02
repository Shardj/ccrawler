# Launcher defines our changes to builtins then runs app/main.py
import subprocess, os, configparser, builtins, imp, sys
# Store project absolute path in global __builtins__
builtins.absolute = os.path.dirname(os.path.abspath(__file__)) # global variable for absolute path imports

def projectRelativeImport(fileName, projectRelativePath, moduleName = None):
    # if moduleName not set, set it to file name with first letter capatilised
    if moduleName is None:
        moduleName = fileName[:1].capitalize() + fileName[1:]

    # we shouldn't be passing fileName with an extension unless moduleName is set due to previous if. So in those cases we add .py
    if len(fileName) >= 3 and fileName[-3:] != '.py':
        fileName = fileName + '.py'

    dir = os.path.join(builtins.absolute, projectRelativePath)
    full = os.path.join(dir, fileName)

    sys.path.append(dir)
    submodule = imp.load_source(moduleName, full)
    sys.path.remove(dir)
    return submodule

builtins.projectRelativeImport = projectRelativeImport # new global function for importing using project relative path
