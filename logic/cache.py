from urllib.request import urlretrieve
import hashlib
import os.path
import re


def url_fetch(url):
    """
    Read URL from local cache file. If local cache file does
    not exist, perform urlretrieve() to read URL to cache file.
    """
    # Generate a hash of the URL without the trailing API Key
    # API Key MUST be placed at the end of the URL!
    url_no_key = re.sub('&key=.+', '', url)
    m = hashlib.md5()
    m.update(str(url_no_key).encode('utf-8'))
    url_hash = m.hexdigest()
    cache_filename = 'cache/' + url_hash + '.html'

    if not os.path.isdir('cache/'):
        os.mkdir('cache/')

    if not os.path.isfile(cache_filename):
        urlretrieve(url, cache_filename)

    page_cache = open(cache_filename, "r")
    page_content = page_cache.read()

    return page_content


if __name__ == '__main__':
    url = 'https://www.logicforte.com/'
    page = url_fetch(url)
    print(page)
