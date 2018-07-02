import builtins, os, uuid, json, time
Helper = projectRelativeImport('helpers', 'app/util', 'Helper')

class DataStorage:

    def __init__(self, base):
        # absolute path to project, storage directory, base_url + _time
        self.storagePath = os.path.join(builtins.absolute, 'storage', Helper.removeNonAlphaNumeric(base) + '_' + time.time())
        mkdir(self.storagePath)

    def saveItem(self, item, itemId):
        # naming for this item. title__h1__unique
        name = item.getId() + '__' + item.getTitle() + '__' + item.getHeaderOne() + '__' + uuid.uuid4().hex[:6].upper()
        metaPath = os.path.join(self.storagePath, name, '.meta')
        contentPath = os.path.join(self.storagePath, name, '.html')
        try:
            write(metaPath, json.dumps(item))
            write(contentPath, item.getContent())
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
