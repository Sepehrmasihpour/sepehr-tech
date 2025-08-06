import httpx
from config import settings
import time
from models import *

BASE_URL = settings.payping_base_url
HEADER = {"Authorization": f"Token {settings.payping_api_token}"}
