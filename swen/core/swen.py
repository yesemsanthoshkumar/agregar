"""Swen chatbot"""

from sentiment.sentiment_analysis import sentiment_over_time

BOT_MSG = "Hi! I'm Swen. How may I help you?"
HMN_MSG = None

while HMN_MSG != 'exit':
    print(BOT_MSG)
    HMN_MSG = input()
    if HMN_MSG.startswith("s?"):
        sentiment_over_time(HMN_MSG.strip("s?").strip())
    # print("Message received: ", HMN_MSG)
