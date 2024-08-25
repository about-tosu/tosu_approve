from os import path, getenv

SUDO = "5171347305"

class Config:
    API_ID = int(getenv("API_ID", "14055090"))
    API_HASH = getenv("API_HASH", "a46f7b439d0afa45b7a69fc450f754e9")
    BOT_TOKEN = getenv("BOT_TOKEN", "7043502393:AAEdH1AegBbo9KIA91jWcie7KRE9gXXG5kw")
    FSUB = getenv("FSUB", "about_tosuu")
    CHID = int(getenv("CHID", "-1002023182491"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://botmaker9675208:botmaker9675208@cluster0.sc9mq8b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
