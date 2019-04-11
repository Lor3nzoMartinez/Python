# Chapter 2 Exercise 7 Homework

'''

Exercise 7:
You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At
what time does the alarm go off? (Hint: you could count on your fingers, but this is not
what we’re after. If you are tempted to count on your fingers, change the 51 to 5100.)

'''

class AlarmClock:

    def __init__(self):
        self.hours = int(input("\nHow many hours would you like to set the alarm for: "))
        self.time = int(input("\nWhat time is it: "))
        self.hour = 0
        self.endTime = 0
        self.tod = ""

    def timeConverter(self):
        self.hour = self.hours % 12
        return self.hour

    def theTime(self):
        self.endTime = self.timeConverter() + self.time
        return self.endTime

    def amorpm(self):
        counter = 0
        for i in range(self.time):
            if i % 12 == 0:
                counter += 1
        if counter % 2 != 0:
            return "AM"
        else:
            return "PM"

    def toString(self):
        print("\nI will wake you up in", self.hours, "hours at", self.theTime(), "O'clock.", self.amorpm())


alarm = AlarmClock()

alarm.toString()
