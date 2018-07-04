import copy
Helper = projectRelativeImport('helpers', 'app/util', 'Helper')

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
        self.content = [] # array normally with only one value, but selector could return multiple values
        self.attempted = False
        self.title = ''
        self.headerOne = []
        self.saved = False
        self.parents = [parentId]
        self.children = []
        self.url = url
        self.id = None

    # returns a stringified clone, doesn't effect original
    def stringifyTags(self):
        clone = copy.copy(self)
        temp = ''
        for contentPart in clone.content:
            temp = temp + self.__cleanMe(contentPart)

        clone.content = temp
        clone.title = Helper.xstr(clone.title)

        temp = ''
        for tag in clone.headerOne:
            if tag is not None and tag != '':
                temp = temp + ' - ' + tag.get_text().strip()

        clone.headerOne = temp
        return clone

    # private tag to clean string for content
    def __cleanMe(self, soup):
        for script in soup(["script", "style"]): # remove all javascript and stylesheet code
            script.extract()
        # get text
        text = soup.get_text()
        # break into lines and remove leading and trailing white space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text
