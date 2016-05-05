import tweepy, csv, re
from config import *

# Set vars
listhandle = ''
listslug = ''
listurl = raw_input("Paste list URL here (Example: https://twitter.com/user/lists/list-slug/): ")
match = re.search( 'twitter.com/(.*)/lists/([\w-]+)/?' , listurl)
if match:
    listhandle = match.group(1)
    # print listhandle
    listslug = match.group(2)
    # print listslug
else: 
    print ' -- Error: No username or list slug found in URL'
    print ' -- Please provide a URL structured like this:'
    print ' -- https://twitter.com/username/lists/list-slug/'
    # See: http://stackoverflow.com/a/19747562
    raise SystemExit

# Credentials stored in config file, see example-config.py for example
# More: http://tweepy.readthedocs.io/en/v3.5.0/getting_started.html
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Set up CSV
c = csv.writer(open(listslug+'.csv', 'wb'))
c.writerow(['id','name','handle','desc','link','img'])

# See: https://twitter.com/carldavaz/lists/rgstaff
# See: https://dev.twitter.com/rest/reference/get/lists/members
# Note: Twitter lists can't be larger than 5,000 members
list = api.list_members(listhandle, listslug, count='5000')
for i, member in enumerate(list):
    # Set member vars
    name = member.name.encode("utf-8")
    sname = member.screen_name.encode("utf-8")
    desc = member.description.encode("utf-8")
    link = 'http://twitter.com/' + sname
    img = member.profile_image_url
    # Write row for each
    c.writerow([i,name,sname,desc,link,img])

print 'Successfully created a CSV of your list in this directory with the name ' + listslug + '.csv'
