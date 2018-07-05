import configparser, os, builtins, sys

class ConfHandler:
    confPath = os.path.join(builtins.absolute, 'settings/local.ini')
    conf = None

    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(self.confPath)

    def save(self):
        with open(self.confPath, 'w') as configfile:
            self.conf.write(configfile)

    def takeInput(self, inputStr, settingType, settingName, validation = []):
        inputResult = input(inputStr + ' (' + self.conf[settingType][settingName] + '): ')

        if inputResult == '' or inputResult is None:
            inputResult = self.conf[settingType][settingName]
        else:
            self.conf[settingType][settingName] = inputResult

        if validation != [] and inputResult not in validation:
            print('Invalid response, please respond with one of the following in the future: ' + str(validation))
            sys.exit()

        return inputResult
