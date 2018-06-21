import configparser

class ConfHandler:
    confPath = r'.\settings\local.ini'
    conf = None

    def __init__(self):
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(self.confPath)

    def save():
        with open(self.confPath, 'w') as configfile:
            self.conf.write(configfile)

    def takeInput(inputStr, settingType, settingName):
        inputResult = input(inputStr + ' (' + self.conf[settingType][settingName] + '): ')

        if inputResult == '' or inputResult is None:
            inputResult = self.conf[settingType][settingName]
        else:
            self.conf[settingType][settingName] = inputResult

        return inputResult
