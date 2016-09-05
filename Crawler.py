# import urllib.request
# import http.cookiejar
# import re
#
# page_url = "https://www.instagram.com/explore/tags/selfie/"
#
# cj = http.cookiejar.CookieJar()
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# response = opener.open(page_url)
# response.addheaders = [('User-agent', 'Mozilla/5.0')]
# if 'text/html' in response.getheader('Content-Type'):
#     html_bytes = response.read()
#     html_string = html_bytes.decode("utf-8")
#
# finder = LinkFinder(Spider.base_url, page_url)
# finder.feed(html_string)
#
#
# except Exception as e:
# print(str(e))
# return set()

#converting the html to string, and then extracting the json part...

from urllib.request import urlopen, Request
import re

url = "https://www.instagram.com/explore/tags/selfie/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode("utf-8")

string = "\"nodes\": ["
regulars = html.split(sep=string)
nodes = regulars[1].split(sep="]},")
print(nodes[0])

# regulars = regulars.split("]},")
