#fp = open(input("Enter friendslist filename: "),'r')
import pandas as pd
from sys import exit
from os import system

def checkBanned(friends):
    results = []
    url = r'https://cewl.a2hosted.com/lists.php?show=banned_members'
    tables = pd.read_html(url)
    cewl_banned = tables[0]['PSN']
    for friend in friends:
        if len(cewl_banned[cewl_banned==friend]):
            results.append(friend)
    return results
    

def getFriends(username="cnnet",size=250):
    print("Getting ",username,"'s PSN friends..\n")
    system("php getFriends.php " + username + " "+str(size)+" > friends_"+username)
    filename = "friends_"+username
    fp = open(filename,'r')
    if fp.readline().endswith("Exiting..\n"):
        return (filename,-1)
    fp.close()
    return (filename,0)

if __name__ == "__main__":
    username = input("Enter PSN username : ")
    filename,code = getFriends(username)
    if code == -1:
        fp = open(filename,'r')
        print(fp.readline())
        exit()  
    else:
        friends = []
        fp = open(filename,'r')
        for line in fp:
            friends.append(line.rstrip())
        print(checkBanned(friends))
        exit()