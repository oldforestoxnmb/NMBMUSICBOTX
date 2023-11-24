from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("29388736"))
API_HASH = getenv("0b6b89768857602f9236afab60cac78f")

BOT_TOKEN = getenv("6874503477:AAGh6tKlmocIs5awMEVSgbWSN1cmKnOwcQk", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("5371579102"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/7d201555feafaca3b18fe.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/de126268f8cef53390434.jpg")

SESSION = getenv("BQHAb8AAVjI_nXDy1KD94QTC4xolDP5t5xSDIF9Qy7Pnlkih8akIvt2pbqeCFdFuEAKalDwK65YGFYzB9QbOrGI8yqmTuseWNSJrl6VlLFwVzaSCTR2rfgcFBhqfTHH8SDWiadLM50DIoxTsl80vIMC121_o9pm8w2pQ2v75bAbt9y7wwChGqh8Kj5SEp7bTyuu4LQi3aTT412JVo28tTDYUz-J7lde2AkiICPY810f5uIY4GHNo6wfiJSanhBlxdX8G3LcYBJacG4IHJFaVG-xk2NX4TxPYMtliJCTHQRchJU6uEjKc9W0eFUTtPAt9tVO5Rno7lSpBE5sVG7lJ6GmIcpbvHAAAAAFAK8reAA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/nmb_xD")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NoMoreBins")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284002358").split()))


FAILED = "https://graph.org/file/51ac174f20b91e941b318.jpg"
