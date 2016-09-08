from urllib.request import urlopen, Request, urlretrieve # for opening URL's, and retrieving image
from bs4 import BeautifulSoup # optional... might be useless
import ast # for safe eval
import time # for delay

# open the page and get the html
url = "https://www.instagram.com/explore/tags/selfie/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode("utf-8")

# setting a json string to eventually save it to file

# I use beutiful soup, because I think it's faster than treating the html like a string
# so I 1st narrow down to the script I want, and only then convert it to a string
# Though I might be wrong, and then this is useless, and we can treat the whole thing as
# a string from beginning
soup = BeautifulSoup(html, "lxml")
json_string = '''script'''
temp = soup.find_all(json_string)
data = ''
for json in temp:
    temp2 = str(json.string)
    if temp2.startswith('window._sharedData'):
        data = temp2

# this gets only the json with the info from the main selfie page
delimiter = '''"nodes": '''
new_data = data.split(delimiter)[1].split("]},")[0] + "]"
new_data = new_data.replace("false", "\"\"")
x = ast.literal_eval(new_data)

# we unfortunately don't have the no. of followers
# to get it we must first go to the picture page, to get the username,
# and then go to the user page to get the no#.
# we have to add some delay time (time.sleep()) in order not to get kicked out

# x is now a list of dictionaries
for i in x:
    time.sleep(1)

    i = dict(i)
    pic_url = "https://www.instagram.com/p/" + str(i['code'])
    #i['code'] contains the unique picture post

    # open the picture/post page to get the user name
    pic_req = Request(pic_url, headers={'User-Agent': 'Mozilla/5.0'})
    pic_html = urlopen(pic_req).read().decode("utf-8")
    del1 = "photo by @"
    del2 = " "
    user_name = pic_html.split(del1)[1].split(del2)[0]

    # for some reason sometimes it has a " in the end that needs to be removed
    if user_name[-1] == '\"':
        user_name = user_name[:-1]

    # user_name = the user's name ...
    user_url = "https://www.instagram.com/" + user_name

    # just another precaution
    time.sleep(0.5)

    # saves the images
    savename = i['code'] + ".jpg"
    urlretrieve(i['display_src'], savename)

    # open the user page to get # of followers
    user_req = Request(user_url, headers={'User-Agent': 'Mozilla/5.0'})
    user_html = urlopen(user_req).read().decode("utf-8")
    del3 = "\"followed_by\": {\"count\": "
    del4 = "}"
    followers = user_html.split(del3)[1].split(del4)[0]


    # writing to file, file still needs slight modification to work as json
    # especially remove the " in the beginnning, and add a } at the end ...
    json_file = "\"" + i['code'] + "\": {" + "\"likes\": " + "\"" +str(i['likes']['count']) + "\"" + ", " + "\"comments\": " + "\"" + str(i['comments']['count']) + "\"" + ", " + "\"followers\": " + "\"" + followers + "\"" + ", " + "\"date\": " + "\"" + str(i['date']) + "\"" + " }, "

    # likes-count gives the count of likes, comments likewise, date gives unix time
    # display_src gives direct link to the image
    # image will be saved with the name of the code

    with open('data.json', 'a') as outfile:
        outfile.write(json_file)


