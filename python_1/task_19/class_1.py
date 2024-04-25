import time
from datetime import datetime, timedelta


class Timer:

    def fired(self, seconds=5):
        current_time = datetime.now() + timedelta(seconds=seconds)
        while current_time >= datetime.now():
            print("vienas")
            time.sleep(1)
