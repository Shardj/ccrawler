import builtins, os, uuid, json

class DataStorage:
    storagePath = os.path.join(builtins.absolute, 'storage')

    def __init__(self):
        self.map = [] # list of {id,childPath}

    def saveItem(self, item, itemId):
        parentPath = self.getChildPath(item.getParentId())

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

    def getMapItem(self, id):
        for item in self.map:
            if item.id == id:
                return item
            else:
                return False
