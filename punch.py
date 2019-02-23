# PUNCHMEIN v0.1
# Last Update: 02/18/2019

mins = list(range(0,60))
hrs = list(range(0,24))*2

time_window = {"00": mins[53:] + mins[:8], 15: mins[8:23], 30: mins[23:38], 45: mins[38:53]}

print(("*")*60)
print("Welcome to Punch Me In!\nAll times are assumed to be in military format in this version!")
print(("*")*60)

def check_for_exit(user_input):
    if user_input.lower() == "exit":
        print("Goodbye")
        quit()

def check24(time):
    return '{:02d}'.format("00") if time >= 24 else time

def timeformat(time):
    return f"{time:02d}" if time < 10 else time

def timestamp():
    while True:
        start_time = input("What time did you punch in today? (HH:MM) ")
        check_for_exit(start_time)
        if ":" not in start_time or len(start_time) != 5:
            print("You must enter your time in the HH:MM format")
            continue
        elif int(start_time[:2]) not in range(0,24) or int(start_time[3:]) not in range(0,60):
            print("Please enter a valid time. Remember, use 24 hour time.\n(Ex. 7:45am = 07:45 :: 7:45 = 19:45)")
            continue
        else:
            break
    return start_time

def daily_grind():
    while True:
        shift_length = input("Do you work 8, 10, or 12 hour shifts? ")
        check_for_exit(shift_length)
        try:
            shift_length = int(shift_length)
        except ValueError:
            print("Please enter an integer")
            continue
        if shift_length not in [8,12,10]:
          print("Currently this program requires 8, 10, or 12 hr workdays")
          continue
        else:
          break
    return shift_length


punchin = timestamp()
workday = daily_grind()

hour = int(punchin.split(":")[0])
minutes = int(punchin.split(":")[1])
shift = hour + workday
hrs_end = hrs[shift]

if minutes in mins[53:]:
    hour += 1
    hrs_end += 1

clockout = timeformat(hrs[shift-1]) if minutes in mins[:8] else timeformat(hrs[shift])

for x in time_window:
  if minutes in time_window[x]:
    hour = timeformat(hour)
    hrs_end = timeformat(hrs_end)
    print(f"You entered {punchin} as your clock in time. Your workday starts at {hour}:{x} and ends at {hrs_end}:{x}. You can clock out starting at {clockout}:{timeformat(time_window[x][0])}")
