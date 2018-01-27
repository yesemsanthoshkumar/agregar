"""Swen chatbot"""

BOT_MSG = "Hi! I'm Swen. How may I help you?"
HMN_MSG = None

while HMN_MSG != 'exit':
    print(BOT_MSG)
    HMN_MSG = input()
    print("Message received: ", HMN_MSG)
