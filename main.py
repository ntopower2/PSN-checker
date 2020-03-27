#fp = open(input("Enter friendslist filename: "),'r')
import pandas as pd
friends = []
fp = open("friendslist.txt",'r')
lines = fp.readlines()
for line in lines:
    pos=line.find("/profile")
    if pos!=-1:
        pos += len("/profile/")
        friends.append(line[pos:pos+line[pos:].find("\"")])

url = r'https://cewl.a2hosted.com/lists.php?show=banned_members'
tables = pd.read_html(url) # Returns list of all tables on page
cewl_banned = tables[0]['PSN']
for friend in friends:
    if len(cewl_banned[cewl_banned==friend]):
        print(friend)
