class MinToDaysHoursMinutes:

    def __init__(self):
        self.mins = int(input("How many minutes do you wish to convert: "))
        self.min = 0
        self.hours = 0
        self.days = 0

    def MinToDay(self):
        self.days = self.mins // 1440
        return self.days

    def MinToHours(self):
        self.hours = (self.mins-(self.days * 1440)) // 60
        return self.hours

    def MinToMins(self):
        self.min = self.mins % 60
        return self.min

    def toString(self):
        if self.mins == 1:
            return print("\nThere are", self.MinToDay(), "days", self.MinToHours(), "hours and",
                         self.MinToMins(), "minute in", self.mins, "minute.")

        elif self.MinToMins() == 1:
            return print("\nThere are", self.MinToDay(), "days", self.MinToHours(), "hours and",
                         self.MinToMins(), "minute in", self.mins, "minutes.")

        else:
            return print("\nThere are", self.MinToDay(), "days", self.MinToHours(), "hours and",
                         self.MinToMins(), "minutes in", self.mins, "minutes.")


example_a = MinToDaysHoursMinutes()

example_a.toString()