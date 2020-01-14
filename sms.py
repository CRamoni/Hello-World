#An SMS Simulation

class SMSMessage():
    def _init_ (self, hasBeenRead, messageText, fromNumber):
        self.hasBeenRead = False
        self.messageText = messageText
        self.fromNumber = fromNumber # The constructor should initialise the senders number

# method changing hasBeenRead to True 
    def MarkAsRead(self):
        self.hasBeenRead = True
        return self.hasBeenRead 
        
 
# a list to be used as an inbox
SMSStore = []

# takes text and number 
def add_sms(self,messageText,fromNumber):
        return (self.messageText, self.fromNumber)
     
# returns number of messages in the store
def get_count(self):
        counter = 0
        if counter in SMSStore:
            counter = counter + 1
            return counter
        
#get_message
def get_message(self):
        
        i = 0
        while 1:
            i=+1
            Getmessage = (input("Enter Message or press Enter:"))
            if Getmessage =="":
                break
            SMSStore.append(Getmessage)
        return SMSStore
    
# get unread messages, returns all unread messages in the list
def unread_messages(self):
        return SMSStore
    
#   removes sms in the smsstore
def remove (self):
      del SMSStore[2]
        

userChoice = ""

while userChoice != "quit":
    userChoice = input("What would you like to do - read/send/quit?:")
    if userChoice == "read":
        print(unread_messages(SMSStore))
    elif userChoice == "send":
        print(get_message(SMSStore))
    elif userChoice == "quit":
        print ("Goodbye")
    else:
        print ("Oops - incorrect input")
