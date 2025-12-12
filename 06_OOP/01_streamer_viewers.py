class Viewer:
    total_viewers = 0  # атрибут на класа (споделен)

    def __init__(self, username, watch_time=0, is_subscribe=False):
        self.username = username
        self.watch_time = watch_time
        self.is_subscribe = is_subscribe

        Viewer.total_viewers += 1

    @classmethod
    def get_total_viewers(cls):
        return cls.total_viewers

    def add_watch_time(self, minutes):
        if minutes > 0:
            self.watch_time += minutes

    def subscribe(self):
        self.is_subscribe = True

    def get_rank(self):
        if self.watch_time < 60:
            return "Newbie"

        elif self.watch_time < 300:
            return "Regular"

        return "Super Fan" if self.is_subscribe else "Fan"

    def __repr__(self):
        return (f"Viewer(username={self.username}, watch_time={self.watch_time}, "
                f"subscriber={self.is_subscribe}, rank={self.get_rank()})")