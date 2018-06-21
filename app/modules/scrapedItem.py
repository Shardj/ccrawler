# Individual items being held in scrape.py Data collector
class CollectorItem:
    # Values
    url: ''
    content: None
    parent: -1
    attempted: False
    title: ''
    headerOne: ''
    saved: False

    # Initializer
    def __init__(parentId, url):
        if type(parentId) is not int:
            raise TypeError('invalid type of parentId in CollectorItem __init__(), should be int')
        elif type(url) is not str:
            raise TypeError('invalid type of url input in CollectorItem __init__(), should be str')
        elif parentId <= 0:
            raise ValueError('invalid value of parentId in CollectorItem __init__(), must be greater than zero')
        else:
            self.parent = parentId
            self.url = url
