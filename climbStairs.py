TASKLIST = ['work,0650,0730',
            'read,1100,1115',
            'play,1210,1250',
            'read,1515,1530',
            'eat,1130,1430',
            'run,1750,1930',
            'eat,2000,2100',
            'play,1800,2100']

# a={1,2} b={1,4} a[0] <= b[0] or b[0] <= a[0] and
# {1,4} {2,3}

# 1 Print out name of each activity
# 2 Print name of unique activity
# 3 Print activity and the duration of each of the activity
# 4 Can you tell which activity overlap and how long do they overlap?


def check_overlapping(data):
    i = 0
    j = 1
    readings = {}
    for d in data:
        activity, start_time, end_time = d.split(',')
        if activity not in readings:
            readings[activity] = [(start_time, end_time)]
        else:
            readings[activity].append((start_time,end_time))

    sorted_readings = []
    for v in readings.values():
        for v1 in v:
            sorted_readings.append(v1)

    sorted_readings = sorted(sorted_readings)
    for i in range(len(sorted_readings) - 1):
        if sorted_readings[i][1] >= sorted_readings[i+1][0]:
            overlapping_interval = sorted_readings[i+1]
            for k,v in readings.items():
                if overlapping_interval in v:
                    print "Overlapping Event = %s" %k


def check_overlapping_two(data):
    intervals = [d.split(',') for d in data]
    intervals = sorted(intervals[1:],key=lambda i: i[1])
    for i in range(len(intervals) - 1):
        if int(intervals[i+1][1]) <= int(intervals[i][2]):
            print "Activity (%s) is overlapping with activity (%s)" % (intervals[i+1][0],intervals[i][0])

def unique_activities(data):
    unique_activities = set()
    for d in data:
        activity = d.split(',')[0]
        if activity not in unique_activities:
            unique_activities.add(activity)

    print unique_activities








if __name__ == '__main__':
    check_overlapping_two(TASKLIST)
    unique_activities(TASKLIST)

