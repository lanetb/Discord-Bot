import discord
import random
import re

class Quotes_Chat:
    def __init__(self, quotes_chat, quote_of_the_day):
        self.quotes_chat = quotes_chat
        self.quotes_of_the_day = quote_of_the_day

    def set_quotes_chat(self, quotes_chat):
        self.quotes_chat = quotes_chat

    def get_quotes_chat(self):
        return self.quotes_chat
    
    def set_quotes_of_the_day(self, quotes_of_the_day):
        self.quotes_of_the_day = quotes_of_the_day

    def get_quotes_of_the_day(self):
        return self.quotes_of_the_day
    
quotes_chat = Quotes_Chat(None, None)

def handle_message(message) -> str:
    p_message = message.lower()

    if p_message == "hi":
        return "Hello, how are you?"
    
    if p_message == "quote" or p_message == "q":
        if quotes_chat.get_quotes_chat() == None:
            return "No quotes chat has been set."
        else:
            try:
                list_q = quotes_chat.get_quotes_chat().history()
                return get_random_quote(list_q)
            except quotes_chat.get_quotes_chat.history().Forbidden:
                return "I don't have permissions for that chat."
            except quotes_chat.get_quotes_chat.history().HTTPException:
                return "Could not get the chat history."
            
    if p_message == "setquoteschat" or p_message == "sqc":
        quotes_chat.set_quotes_chat(discord.TextChannel)
        return "This chat has been set as the quotes chat."
    
    if p_message == "$setquotesoftheday" or p_message == "$sqotd":
        quotes_chat.set_quotes_of_the_day(discord.TextChannel)
        

def get_random_quote(qoutes):
    regex = re.compile('"[A-Za-z0-9\s]+" - [A-Za-z0-9@\s]+')
    qoute = random.choice(qoutes)
    if re.match(regex, qoute):
        return qoute
    else:
        return get_random_quote(qoutes)
    
def parse_quote(quote):
    regex = re.compile('"[A-Za-z0-9\s]+"')
    q = re.split(regex, quote)
    regex = re.compile('@')


