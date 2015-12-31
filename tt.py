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

    def timediff(self, t2, t1):
        return time(t2.hour - t1.hour, t2.minute - t1.minute)


    ### OBJECT INIT STUFF ###

    def __init__(self):
        a = self.activity.copy()
        a["name"] = "Operating Systems"
        t1 = time(10, 0)
        t2 = time(11, 0)
        self.insert_activity(a, "1", t1, t2)
        self.insert_activity(a, "6", time(8, 30), time(9, 30))

        print self.timediff(t2, t1)



        pprint(self.thetable)


if __name__ == "__main__":
    t = TimeTable()
