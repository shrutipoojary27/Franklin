def ham(slack_username,twitter_username ):
    i=0
    count=0
    while(i<len(slack_username)):
        if slack_username[i]!=twitter_username[i]:
            count += 1
        i += 1
    return count

name = "Mangaiyarkarasi S"
email = "mangaiyarkarasi39@gmail.com"
biostack ="genomics"
slack_username = "@MANGAIYARKARASI"
twitter_username = "@Mangaimicro3696"
d =  ham(slack_username,twitter_username)

print("{},{},{},{},{},{}".format(name, email, slack_username, biostack, twitter_username, d))
