## HTML
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out = ''
    
    # Override start and end tag handler
    def handle_starttag(self, tag, attrs):
        self.out=self.out+''+tag

    def handle_endtag(self, tag):
        self.out=self.out+'/'+tag

## Windows and bit array
from bitarray import bitarray
def windows(s, l):
  res=[]
  for i in range(len(s)-l):
    sub=s[i:i+l]
    res.append(sub)
  return res

def to_bit_array(data, wl, bit_len):
  parser = MyHTMLParser()
  parser.feed(data)
    
  ws = windows(parser.out, wl)
  ba = bitarray(bit_len)
  ba.setall(0)
  
  for w in ws:
    ba[hash(w) % bit_len] = 1
    
  return ba