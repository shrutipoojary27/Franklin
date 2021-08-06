def personal_details(name,email,biostack,slack_username,twitter_username):
    print("name:{}\nemail:{}\nbiostack:{}\nslack_username:{}\ntwitter_username:{}\n".format(name, email, biostack,slack_username,twitter_username))
str1="@Mangaimicro3696"
str2="@MANGAIYARKARASI"
def personal(str1,str2):
    print(str1,str2)
def ham(str1, str2):
    i=0
    count=0
    while(i<len(str1)):
        if str1[i]!=str2[i]:
            count += 1
        i += 1
    return count
personal(str1,str2)
print("Hamming distance:{}".format(ham(str1,str2)))
name = "Mangaiyarkarasi S"
email = "mangaiyarkarasi39@gmail.com"
biostack ="genomics"
slack_username = "@MANGAIYARKARASI"
twitter_username = "@Mangaimicro3696"
personal_details(name,email,biostack,slack_username,twitter_username)




