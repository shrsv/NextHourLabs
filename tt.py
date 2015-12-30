from pprint import pprint


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


    ### OBJECT INIT STUFF ###

    def __init__(self):
        a = self.activity.copy()
        a["name"] = "Operating Systems"
        self.insert_activity(a, "1", "10:00", "11:00")
        self.insert_activity(a, "6", "8:30", "9:30")

        pprint(self.thetable)


if __name__ == "__main__":
    t = TimeTable()
