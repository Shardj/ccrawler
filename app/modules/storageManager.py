import builtins, os

class DataStorage:
    storagePath = builtins.getAbsolute()+'storage/'
    map = [] # list of {id,childPath}

    def saveItem(item, itemId):
        parentPath = getChildPath(item.getParentId())

        if parentPath == False:
            path = storagePath
        else:
            path = parentPath

        title = item.getTitle()
        childDir = path + title + '/'
        metaPath = path + title + '.meta'
        contentPath = path + title + '.html'
        try:
            mkdir(childDir)
            write(metaPath, pprint(item))
            write(contentPath, item.getContent())
        except(e):
            print('failed touch or mkdir')
            print(e)
            return

        self.map.append({id: itemId, childPath: childDir})

    def getChildPath(id):
        if any(item.id == id for item in self.map):
            item = self.getMapItem(id)
            if item == False:
                return False

            return item.childPath

    def write(fullpath,content):
        file = open(fullpath, 'w')
        file.write(content)
        file.close()

    def mkdir(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def getMapItem(id):
        for item in self.map:
            if item.id == id:
                return item
            else:
                return False
