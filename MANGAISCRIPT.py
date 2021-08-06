def personal_details(name,email,biostack,slack_username,twitter_username):
    print("name:{}\nemail:{}\nbiostack:{}\nslack_username:{}\ntwitter_username:{}\n".format(name, email, biostack,slack_username,twitter_username))
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
personal_details(name,email,biostack,slack_username,twitter_username)
print("Hamming distance:{}".format(ham(slack_username,twitter_username)))