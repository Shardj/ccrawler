import builtins, os, uuid, json, time
Helper = projectRelativeImport('helpers', 'app/util', 'Helper')

class DataStorage:

    def __init__(self, base):
        # absolute path to project, storage directory, base_url + _time
        self.storagePath = os.path.join(builtins.absolute, 'storage', Helper.removeNonAlphaNumeric(base) + '_' + str(time.time()))
        self.mkdir(self.storagePath)

    def saveItem(self, item):
        # naming for this item. title__h1__unique
        name = str(item.id) + '__' + item.title + '__' + item.headerOne + '__' + uuid.uuid4().hex[:6].upper()
        metaPath = os.path.join(self.storagePath, name + '.meta')
        contentPath = os.path.join(self.storagePath, name + '.html')
        try:
            self.write(metaPath, json.dumps(item.stringifyTags().__dict__))
            self.write(contentPath, item.getContent())
        except Exception as e:
            print('failed to write files')
            print(e)
            return

        return True

    def write(self, fullpath,content):
        file = open(fullpath, 'w')
        file.write(content)
        file.close()

    def mkdir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
