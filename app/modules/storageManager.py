import builtins, os, uuid

class DataStorage:
    storagePath = os.path.join(builtins.absolute, 'storage')
    map = [] # list of {id,childPath}

    def saveItem(self, item, itemId):
        parentPath = self.getChildPath(item.getParentId())

        if parentPath == False:
            path = storagePath
        else:
            path = parentPath

        # naming for this item. title__h1__unique
        name = item.getTitle() + '__' + item.getHeaderOne() + '__' + uuid.uuid4().hex[:6].upper()
        childDir = os.path.join(path, name)
        metaPath = os.path.join(path, name, '.meta')
        contentPath = os.path.join(path, name, '.html')
        try:
            mkdir(childDir)
            write(metaPath, pprint(item))
            write(contentPath, item.getContent())
        except Exception as e:
            print('failed touch or mkdir')
            print(e)
            return

        self.map.append({id: itemId, childPath: childDir})
        return True

    def getChildPath(self, id):
        if any(item.id == id for item in self.map):
            item = self.getMapItem(id)
            if item == False:
                return False

            return item.childPath

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
