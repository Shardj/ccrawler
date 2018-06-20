import subprocess, os, configparser, builtins, imp

# Store project absolute path
parse = configparser.ConfigParser()
path = './settings/main.ini'
parse.read(path)
parse['project']['path'] = os.path.abspath("./")
with open(path, 'w') as configfile:
    parse.write(configfile)

builtins.absolute = parse['project']['path'] # global variables for absolute path imports
builtins.projectRelativeImport = projectRelativeImport # new global function for importing using project relative path
def projectRelativeImport(fileName, projectRelativePath, moduleName = None):
    if moduleName is None:
        moduleName = fileName.title()

    module = imp.find_module(fileName, builtins.absolute + projectRelativePath)
    imp.load_module(moduleName, module)

# Launch scraper/crawler
cmd = 'python ./app/main.py'

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
out, err = p.communicate()
result = out.split('\n')
for lin in result:
    if not lin.startswith('#'):
        print(lin)
