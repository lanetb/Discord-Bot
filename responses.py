import discord

class Quotes_Chat:
    def __init__(self, quotes_chat, quote_of_the_day):
        self.quotes_chat = quotes_chat
        self.quotes = []
        self.quotes_of_the_day = quote_of_the_day

    def set_quotes_chat(self, quotes_chat):
        self.quotes_chat = quotes_chat

    def get_quotes_chat(self):
        return self.quotes_chat
    
    def set_quotes(self, quotes):
        self.quotes = quotes
    
    def get_quotes(self):
        return self.quotes
    
    def set_quotes_of_the_day(self, quotes_of_the_day):
        self.quotes_of_the_day = quotes_of_the_day

    def get_quotes_of_the_day(self):
        return self.quotes_of_the_day
    
quotes_chat = Quotes_Chat(None)

def handle_message(message) -> str:
    p_message = message.lower()

    if p_message == "$hi":
        return "Hello, how are you?"
    
    if p_message == "$quote" or p_message == "$q":
        return "place holder"
    
    if p_message == "$setquoteschat" or p_message == "$sqc":
        quotes_chat.set_quotes_chat(discord.TextChannel)
        return "This chat has been set as the quotes chat."
    
def quote_of_the_day() -> str:
    return "place holder"

