import re

# I think you can guess what this does
def url_validate(url):
    if url is None or url is '':
        return False

    regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(re.match(regex, url))

# rindex for lists (reverse index)
def rindex(mylist, myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1

def removeNonAlphaNumeric(text):
    return re.sub(r'\W+', '', text)

def xstr(s):
    if s is None:
        return ''
    return str(s)

def purgeWhitespace(text):
    return re.sub('\s', '', text) # remove all whitespace
