from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "2334"))
API_HASH = getenv("API_HASH", "2e0ea05fda51f54f36baf7")

BOT_TOKEN = getenv("BOT_TOKEN", "6606:AAS516KV6FR-fNOmNgZCPXnehlOU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

OWNER_ID = int(getenv("OWNER_ID", "5866649827"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BAGGCcgAQMIcH60z0iO3dweux4RPsmtMdR6PJ8ZtpA9tTq5X4U5C_etqWH1BoOKxEwRlp9LKk0woXh3J4rS-kTTnVkHlmo_95WN0qHCemrc3WEN0X_1pLwZgECULQXSU9YJAJ3K97_mDsnL21sUyTsSBTcU4Y-Ew99iU8ZHuZTw4ccV-A9smhHK5qlV1he-mGtJg0zzFr4YOqUXCv71bOkvQ3zrHJ74GZyhLECt5Zyy3FbF8KP42Gch_EiLPziVlOE3y4GavTtmbYyL_koUFVvDMQRiRdRVF6DC81zapC0t06pSr-4lhmMVdUwAAAAGCEwTqAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/cczza")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/cczza")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5866649827").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
