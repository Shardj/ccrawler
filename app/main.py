# Imports
Scrape = projectRelativeImport('scrape', 'app/modules/scraping', 'Scrape')
SaveHandler = projectRelativeImport('inputSaveHandler', 'app/util', 'SaveHandler')
import sys, builtins

# User input and startup, using previously entered values handler provides QOL, at the end we save values entered in current runtime as new default values
handler = SaveHandler.ConfHandler()
starting = handler.takeInput('First url to pull from', 'InputCache', 'starting')
base = handler.takeInput('Will only crawl urls which contain', 'InputCache', 'base')
selector = handler.takeInput('Data css selector', 'InputCache', 'selector')
handler.save()

Scrape.Data(selector, starting, base).start()
