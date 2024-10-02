import time
import datetime
import winsound
from threading import Timer

class AlarmClock:
    def __init__(self):
        self.alarms = []

    def add_alarm(self, alarm_time, sound_file=None, message="Wake up!", recurring=False, snooze_duration=5):
        alarm = {
            "time": alarm_time,
            "sound_file": sound_file,
            "message": message,
            "recurring": recurring,
            "snooze_duration": snooze_duration,
            "snoozed": False
        }
        self.alarms.append(alarm)

    def start(self):
        while True:
            current_time = datetime.datetime.now().time().strftime("%H:%M:%S")
            for alarm in self.alarms:
                if current_time == alarm["time"] and not alarm["snoozed"]:
                    self.trigger_alarm(alarm)
                    if not alarm["recurring"]:
                        self.alarms.remove(alarm)
            time.sleep(1)

    def trigger_alarm(self, alarm):
        print(alarm["message"])
        if alarm["sound_file"]:
            winsound.PlaySound(alarm["sound_file"], winsound.SND_FILENAME)
        else:
            winsound.Beep(2500, 1000)  # Default beep sound
        if input("Snooze? (y/n): ").lower() == 'y':
            alarm["snoozed"] = True
            t = Timer(alarm["snooze_duration"] * 60, self.snooze_alarm, [alarm])
            t.start()

    def snooze_alarm(self, alarm):
        alarm["snoozed"] = False

def main():
    alarm_clock = AlarmClock()
    alarm_time = input("Enter the time to set the alarm (HH:MM:SS): ")
    sound_file = input("Enter the path to the sound file (or leave blank for default beep): ")
    message = input("Enter the alarm message: ")
    recurring = input("Should the alarm be recurring? (y/n): ").lower() == 'y'
    snooze_duration = int(input("Enter the snooze duration in minutes: "))

    alarm_clock.add_alarm(alarm_time, sound_file, message, recurring, snooze_duration)
    alarm_clock.start()

if __name__ == "__main__":
    main()
