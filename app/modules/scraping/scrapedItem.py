# Individual items being held in scrape.py Data collector
class CollectorItem:
    # Initializer
    def __init__(self, parentId, url):
        if type(parentId) is not int:
            raise TypeError('invalid type of parentId in CollectorItem __init__(), should be int')
        elif type(url) is not str:
            raise TypeError('invalid type of url input in CollectorItem __init__(), should be str')
        elif parentId < -1:
            raise ValueError('invalid value of parentId in CollectorItem __init__(), must be greater than or equal to negative one')

        # Values
        self.content = None
        self.attempted = False
        self.title = ''
        self.headerOne = ''
        self.saved = False
        self.parents = [parentId]
        self.children = []
        self.url = url
        self.id = None

    def stringifyTags(self):
        self.content = str(self.content)
        self.title = str(self.title)
        self.headerOne = str(self.headerOne)
        return self
