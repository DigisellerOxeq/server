import time
import hashlib
from email.policy import default

from app.core.config import settings
from app.lib.http_client import HTTPClient


class DigisellerAPI:

    def __init__(self, token: str, seller_id: int):
        self.token = token
        self.seller_id = seller_id

    def get_token(self):

        timestamp = int(time.time())

        data = self.token + str(timestamp)
        sign = hashlib.sha256(data.encode('utf-8')).hexdigest()

        json_ = {
            "seller_id": self.seller_id,
            "timestamp": timestamp,
            "sign": sign
        }

        http_client = HTTPClient(
            base_url=settings.digi.base_url,
            timeout=settings.digi.timeout,
            retries=settings.digi.retries,
            delay=settings.digi.delay,
            headers=
        )

        response = HTTPClient.post(
            self,
            endpoint='/api/apilogin',
            json=json_,
            headers=
        )


        if response.status_code != 200:
            return None

        if 'retval' not in data or 'token' not in data or data['retval'] != 0:
            return None

        return data['token']