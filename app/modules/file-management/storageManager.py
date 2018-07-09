import builtins, os, uuid, json, time
Helper = projectRelativeImport('helpers', 'app/util', 'Helper')

class DataStorage:

    def __init__(self, base):
        # absolute path to project, storage directory, base_url + _time
        self.storagePath = os.path.join(builtins.absolute, 'storage', Helper.removeNonAlphaNumeric(base) + '_' + str(int(time.time())) )
        self.mkdir(self.storagePath)

    def saveItem(self, item):
        try:
            clonedItem = item.stringifyTags()
            # naming for this item. title__h1__unique
            name = str(clonedItem.id) + '__' + Helper.removeNonAlphaNumeric(clonedItem.title) + '__' + Helper.removeNonAlphaNumeric(clonedItem.headerOne)
            metaPath = Helper.purgeWhitespace(os.path.join(self.storagePath, name + '.meta'))
            contentPath = Helper.purgeWhitespace(os.path.join(self.storagePath, name + '.txt'))
            self.write(contentPath, clonedItem.content)
            del clonedItem.content # we don't want content in our meta files
            self.write(metaPath, json.dumps(clonedItem.__dict__))
            # our cloned item loses scope here and is thrown away
        except Exception as e:
            print('failed to write files')
            print(e)
            return

        return True

    def write(self, fullpath, content):
        file = open(fullpath, 'w')
        file.write(content)
        file.close()

    def mkdir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
