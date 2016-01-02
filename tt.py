from pprint import pprint
from datetime import time


class TimeTable:

    ### BASIC DATASTRUCTURES ###

    day_ids = (0, 1, 2, 3, 4, 5, 6)
    day_names = ("Sunday", "Monday", "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday")

    activity = {
        "name": "",
        "short_name": "",
        "lecturer": ""
    }

    activity_segment = (None, None, None) # activity, start, end

    thetable = {
            "0": [],  # a list of activity_segment tuples
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": []
    }

    ### TABLE BUILDERS ###

    def insert_activity(self, activity, day_id, start, end):
        self.thetable[day_id].append((activity, start, end))


    ### DAY ID, DAY NAME RELATED STUFF ###

    def get_day_id(self, day_name):
        return self.day_ids[self.day_names.index(day_name.title())]


    def get_day_name(self, day_id):
        return self.day_names[day_id]


    def get_short_day_name(self, day_id):
        return self.get_day_name(day_id)[:3]

    def time_diff(self, t1, t2):
        return time(abs(t2.hour - t1.hour), abs(t2.minute - t1.minute), abs(t2.second - t2.second))

    def time_total_secs(self, t):
        return t.hour * 3600 + t.minute * 60 + t.second

    def time_compare(self, t1, t2):
        t1_secs = self.time_total_secs(t1)
        t2_secs = self.time_total_secs(t2)

        if t1_secs == t2_secs:
            return 0
        elif t1_secs > t2_secs:
            return 1
        else:
            return -1



    ### OBJECT INIT STUFF ###

    def __init__(self):
        a = self.activity.copy()
        a["name"] = "Operating Systems"
        t1 = time(12, 0)
        t2 = time(12, 30)
        self.insert_activity(a, "1", t1, t2)
        self.insert_activity(a, "6", time(8, 30), time(9, 30))

        print self.time_compare(time(12, 00), time(12, 00))

        pprint(self.thetable)


if __name__ == "__main__":
    t = TimeTable()
