#  @classmethod
def request(url):
        fh = urllib2.urlopen(url)
        return cls.create(url=url, response=json.loads(fh.read()))