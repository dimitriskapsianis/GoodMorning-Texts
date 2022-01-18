import pywhatkit
import datetime
import random



current_time = datetime.datetime.now()
hour = current_time.hour
min = current_time.minute

print(hour)
print(min)


number_of_msgs = 0

cute_messages = ["Love you so much Kitty",
                 "Hope you have a great day", 
                 "You are a little sleeping miawer",
                 "miaw miaw <3",
                 "where is little kitty?",
                 "I am thinking of you all morning",
                 "love you <3 <3",
                 "I miss our huggies"]

min +=1
pywhatkit.sendwhatmsg("+15085308226","Good morning my love <3",hour,min)


while number_of_msgs <3:

    if min <58:
        min += random.randint(1,3)
    else:
        hour +=1
        min =0

    message = random.choice(cute_messages)
    cute_messages.remove(message)
    pywhatkit.sendwhatmsg("+15085308226",message,hour,min)

    number_of_msgs +=1

    print(number_of_msgs)
    print(min)
    print (cute_messages)




