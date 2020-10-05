class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f"<{self.name} - {self.duration}>"

    def __eq__(self, other):
        if self.duration == other.duration:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.duration < other.duration:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.duration > other.duration:
            return True
        else:
            return False


class Album:
    def __init__(self, name, album):
        self.name = name
        self.album = album
        self.tracks_list = []

    def __str__(self):
        x = ""
        for tracks in self.tracks_list:
            x += f"{str(tracks)} "
        return f"Name group: {self.name}\nName album: {self.album}\n    Tracks:\n    {x}"

    def add_track(self, track):
        self.tracks_list.append(track)


track1 = Track("Серпантин", 3.07)
track2 = Track("Компас", 3.05)
track3 = Track("B.I.D", 3.13)
track4 = Track("Кино", 3.04)
track5 = Track("77", 2.03)
track6 = Track("Бенз", 2.13)

great_depression = Album("Markul", "Great depression")
great_depression.add_track(Track("Серпантин", 3.07))
great_depression.add_track(Track("Компас", 3.04))
great_depression.add_track(Track("B.I.D", 3.13))

moscowsky = Album("MACAN", "MoscowSKY")
moscowsky.add_track(Track("Кино", 3.05))
moscowsky.add_track(Track("77", 2.03))
moscowsky.add_track(Track("Бенз>", 3.13))