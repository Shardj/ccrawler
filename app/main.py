# Imports
Scrape = projectRelativeImport('scrape', 'app/modules', 'Scrape')
SaveHandler = projectRelativeImport('inputSaveHandler', 'app/util', 'SaveHandler')
import sys, builtins

# User input and startup, using previously entered values handler provides QOL, at the end we save values entered in current runtime as new default values
handler = SaveHandler.ConfHandler()
starting = handler.takeInput('first url to pull from', 'InputCache', 'starting')
base = handler.takeInput('will only crawl url which contain the following, leave blank to use first url for this value', 'InputCache', 'base')
selector = handler.takeInput('if you want to pull from a specific page element enter selector here', 'InputCache', 'selector')
handler.save()

# Using imported Scrape file create an object from the Data class and call its start() method. Catch and log all errors collected and not handled from within scrape
try:
    Scrape.Data(selector, starting, base).start()
except Exception as e:
    print('Fatal error: ' + e)
    logError()
    sys.exit()

def logError(err):
    # Convert single errors to list of errors (len 1)
    errList = []
    if type(err) is not list:
        errList.append(err)
    else:
        errList = err

    # log collected list of errors
    logf = open("error.log", "w")
    for err in errList:
        logf.write(str(e))
