import os
import time
import inspect
from dotenv import load_dotenv
from twilio.rest import Client as Twilio

from helper import *

if __name__ == '__main__':
    load_dotenv()

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Twilio(account_sid, auth_token)

    while True:
        try:
            data = get_weather(
                os.environ['LAT'],
                os.environ['LONG'],
            )
            temp_C = round(
                (data['current']['temp'] - 273.15) * 100
            ) / 100
            temp_F = round(
                (1.8 * (data['current']['temp'] - 273.15) + 32) * 100
            ) / 100
            message = client \
                .messages \
                .create(
                    body=inspect.cleandoc(
                        f"""
                        Weather Update: {temp_C}C ({temp_F}F) Src: OpenWeatherMap
                        """
                    ),
                    from_=os.environ['TWILIO_NUMBER'],
                    to=os.environ['TO_NUMBER']
                )
            print('sent:', message.sid)
        except Exception as e:
            print('error:', e)
        finally:
            time.sleep(12 * 60 * 60)
