import subprocess, pathlib, configparser, builtins, imp

# Store project absolute path in global __builtins__
projectDir = pathlib.Path(__file__).parent

builtins.setAbsolute(projectDir) # global variable for absolute path imports
builtins.projectRelativeImport = projectRelativeImport # new global function for importing using project relative path
def projectRelativeImport(fileName, projectRelativePath, moduleName = None):
    if moduleName is None:
        moduleName = fileName.title()

    module = imp.find_module(fileName, self.absolute + projectRelativePath)
    imp.load_module(moduleName, module)

# Launch scraper/crawler
cmd = 'python ./app/main.py'

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
out, err = p.communicate()
result = out.split('\n')
for lin in result:
    if not lin.startswith('#'):
        print(lin)
