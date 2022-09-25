class TimeFormatter:
    def __init__(self, current_time):
        """
        current time: extracted with time.gmtime()
        """
        self.time=current_time
    def __repr__(self):
        date = f"{self.time[0]}-{self.time[1]}-{self.time[1]}"
        time = f"{self.time[3]}:{self.time[4]}"
        return f"{date} {time}"