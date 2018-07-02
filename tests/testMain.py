SaveHandler = projectRelativeImport('inputSaveHandler', 'app/util', 'SaveHandler')
import sys, builtins

# User input and startup, using previously entered values handler provides QOL, at the end we save values entered in current runtime as new default values
handler = SaveHandler.ConfHandler()
testName = handler.takeInput('Name of unit test file', 'Test', 'name')
handler.save()

test = projectRelativeImport(testName, 'tests/unit', 'test')
test.Main().run() #create the test and then run it
