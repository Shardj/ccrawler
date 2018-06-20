# Imports
import random
from bs4 import BeautifulSoup
projectRelativeImport('helpers', 'app/util/', 'Helper')
projectRelativeImport('scrapedItem', 'app/modules/', 'ScrapedItem')
projectRelativeImport('storageManager', 'app/modules/', 'StorageManager')

# Main class to hold our data
class Data:
    # Holds result
    collector = []
    # id of collector item currently being addressed
    currentId = -1
    # urls must contain base to be accepted, so 'bbc.com' would mean we only scrape urls from that page
    base = ''
    # the selector for getting the element which holds the content we want to save
    selector = 'body'
    # request params
    PAYLOAD = {
        timeout: 60,
        headers: {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
        }
    }


    # Initializer, adds our first collector item to our collector and sets the base url
    def __init__(selector, starter, baseUrl = ''):
        if baseUrl == '' or baseUrl is None:
            baseUrl = starter

        if selector != '' or selector is not None:
            self.selector = selector

        this.base = baseUrl
        self.addCollectorItem(self.createCollectorItem(starter))

    # Creates a brand new unedited collector item and returns it
    def createCollectorItem(url):
        parentId = self.currentId
        return ScrapedItem.CollectorItem(parentId, url)

    # Adds supplied item to the end of our collector
    def addCollectorItem(item):
        self.collector.append(item)

    # Returns content from url wrapped in BeautifulSoup object
    def fetchUrl(url):
        response = requests.get(url, params=self.PAYLOAD)
        return BeautifulSoup(response.content, 'html.parser')

    # Main Loop
    def start:
        # Loop while there are still items left ahead of our current id in self.collector
        # Alternative (more robust less efficient) condition `any(item.attempted == False for item in self.collector)`
        while (self.currentId+1 < self.collector.length):
            self.currentId++
            time.sleep(5+random.randint(0, 5)) #don't want to get caught and ipbanned
            try:
                currentItem = self.collector[self.currentId] # Does variable get set to loop scope or try scope? Testing will reveal
            except IndexError:
                raise IndexError('missing item from self.collector at position ' + str(self.currentId) + ' in Data start(),'
                r' while condition should have ended loop before any index errors occour')

            if currentItem.getAttempted() == True:
                raise ValueError('invalid value of attempted in currentItem in Data start(), item at new id should never have already been attempted')

            # Attempt to fetch content from url
            currentItemContent = self.fetchUrl(currentItem.getUrl())
            currentItem.setAttempted(True)
            # Save changes
            self.collector[self.currentId] = currentItem

            # Create new items from found links
            for link in currentItemContent.find_all('a'):
                url = link.get('href')

                # Validate url
                if Helper.url_validate(url) == False:
                    continue

                # Check url is an extension of our base url
                if self.base not in url:
                    continue

                # Check we haven't already stored this url
                if any(item.url == url for item in self.collector):
                    continue

                self.addCollectorItem(createCollectorItem(url))

            currentItem.setContent(currentItemContent.find_all(self.selector))
            currentItem.setTitle(currentItemContent.title.string)
            currentItem.setHeaderOne(currentItemContent.h1.string)

            # Save changes
            self.collector[self.currentId] = currentItem

        self.save()

    #We've crawled all possible urls and will now clean up. Consider implementing functionality to save while crawling (memory is important guys)
    def save:
        storage = StorageManager.DataStorage()
        for index in range(len(self.collector)):
            storage.saveItem(self.collector[index], index)
            index+= 1
