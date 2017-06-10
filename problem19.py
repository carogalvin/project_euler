monthsReg = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthsLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

regDays = {0:[0], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
leapDays = {0:[0], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
weekdays = {0:"Sunday",
            1:"Monday",
            2:"Tuesday",
            3:"Wednesday",
            4:"Thursday",
            5:"Friday",
            6:"Saturday"}
months = {0:"January",
          1:"February",
          2:"March",
          3:"April",
          4:"May",
          5:"June",
          6:"July",
          7:"August",
          8:"September",
          9:"October",
          10:"November",
          11:"December"}

tot = monthsReg[0]
for j in range(1, len(monthsReg)):
    regDays[tot%7].append(j)
    tot += monthsReg[j]

tot = monthsLeap[0]
for j in range(1, len(monthsLeap)):
    leapDays[tot%7].append(j)
    tot += monthsLeap[j]

allMonthsCt = 0
start = 1901
end = 2001
curr = 2

for year in range(start, end):
    # leap year logic
    print("January 1 " + str(year) + " falls on a " + str(weekdays[curr]))
    if(year % 4 == 0 and (not(year % 100 == 0) or (year % 400 == 0))):
        print("leap year!")
        print("months that start on a Sunday: " + str(map(lambda x: months[x], leapDays[(7 - curr) % 7])))
        allMonthsCt += len(leapDays[(7 - curr) % 7])
        curr = (curr + 366) % 7
    else:
        print("not leap year")
        print("months that start on a Sunday: " + str(map(lambda x: months[x], regDays[(7 - curr) % 7])))
        allMonthsCt += len(regDays[(7 - curr) % 7])
        curr = (curr + 365) % 7
print(allMonthsCt)
