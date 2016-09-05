from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import ast

# open the page and get the html
url = "https://www.instagram.com/explore/tags/selfie/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode("utf-8")

# use beutiful soup, because I think it's faster than treating the html like a string
# we 1st narrow down to the script we want, and only then
soup = BeautifulSoup(html, "lxml")

json_string = '''script'''
temp = soup.find_all(json_string)

data = ''
for json in temp:
    temp2 = str(json.string)
    if temp2.startswith('window._sharedData'):
        data = temp2
    # print(temp2)

delimiter = '''"nodes": '''
new_data = data.split(delimiter)[1].split("]},")[0] + "]"
new_data = new_data.replace("false", "\"\"")
x = ast.literal_eval(new_data)

for i in x:
    i = dict(i)
    print(i['code'], i['likes']['count'], i['comments']['count'], i['display_src'].split('?')[0])
#     jd = json.loads(i)
#     print(jd)

# j_d = json.loads(new_data)
#
# result = []
# for item in json_data:
#     my_dict={}
#     my_dict['code'] = item.get('code')
#     my_dict['comments'] = item.get('comments').get('count')
#     my_dict['likes'] = item.get('likes').get('count')
#     my_dict['link'] = item.get('display_src')
#     print(my_dict)
#     result.append(my_dict)
