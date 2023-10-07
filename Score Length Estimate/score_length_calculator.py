import math

try:
    time_signature = int(input("Please enter the numerator (top number) of the time signature: "))
    beats_per_minute = int(input("Please enter the corresponding BPM: "))
    measures = int(input("Please enter the total amount of measures: "))
except ValueError:
    print("Invalid input, please enter a number")
    
total_beats = time_signature * measures
decimal_time = round(total_beats / beats_per_minute, 2)

minutes = math.floor(decimal_time)
seconds = round((decimal_time % 1) * 60)

second = round(minutes*60+seconds)

while True:
    more_time_signature = str.lower(input("Does the score have another time signature? (y/n): "))
    if more_time_signature == "y":
            time_signature2 = int(input("Please enter the numerator (top number) of the time signature: "))
            beats_per_minute2 = int(input("Please enter the corresponding BPM: "))
            measures2 = int(input("Please enter the total amount of measures: "))
            
            total_beats2 = time_signature2 * measures2
            decimal_time2 = round(total_beats2 / beats_per_minute2, 2)

            minutes2 = math.floor(decimal_time2)
            seconds2 = (decimal_time2 % 1) * 60
            
            second2 = round(minutes2*60+seconds2)
            total_seconds = second+second2
            
            m, s = divmod(total_seconds, 60)
            h, m = divmod(m, 60)
            total_time = print(f"\nThe piece will last for approximately {('%d:%02d:%02d' % (h, m, s))}")
            break
        
    elif more_time_signature == "n":
        print(f"\nThe piece will last for approximately {minutes} minute(s) and {seconds} second(s)")
        break
    
    else:
        print("Please answer y or n.")
        
print("-------------------------")
print("Does not work for scores that have more than 2 time signatures.")
print("If there are more than 2, repeat the process accordingly, and manually sum up the total times.")