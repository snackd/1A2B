import time
import datetime

class Timer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.start_time = time.time()
        self.time_list = []

    def start(self):
        self.start_time = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))

    def record(self):
        if not self.start_time:
            print("請先使用 start() 方法開始")
        else:
            self.end_time = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
            self._calculate()

    def _calculate(self):
        self.time_list.append(self.end_time - self.start_time)

    def get_time(self):
        return self.time_list

if __name__ == "__main__":
    t = Timer()
    t.start()
    time.sleep(1)
    t.record()
    temp = t.get_time()
    print(temp[0].seconds)