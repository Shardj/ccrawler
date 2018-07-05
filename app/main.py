# Imports
Scrape = projectRelativeImport('scrape', 'app/modules/scraping', 'Scrape')
SaveHandler = projectRelativeImport('inputSaveHandler', 'app/util', 'SaveHandler')
import sys, builtins, re

# User input and startup, using previously entered values handler provides QOL, at the end we save values entered in current runtime as new default values
handler = SaveHandler.ConfHandler()
starting = handler.takeInput('First url to pull from', 'InputCache', 'starting')
regex = handler.takeInput('Do you wish to use a regex or plaintext filter', 'InputCache', 'regex', ['plaintext' , 'regex'])
# if answer was plaintext then 'contain plaintext:' else 'match regex:'
base = handler.takeInput('Will only crawl urls which ' + ('contain ' if regex == 'plaintext' else 'match ') + regex, 'InputCache', 'base')
selector = handler.takeInput('Data css selector', 'InputCache', 'selector')
handler.save()

# checks further on are expecting 'base' as regex, if plaintext is entered we must escape special characters
Scrape.Data(selector, starting, re.escape(base) if regex == 'plaintext' else base).start()
