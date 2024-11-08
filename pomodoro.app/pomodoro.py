# pomodoro.py
import time
import subprocess


def play_sound(sound_file):
    """Play a sound using aplay.

    Args:
        sound_file (str): Path to sound file
    """
    try:
        subprocess.run(["aplay", sound_file])

    except subprocess.CalledProcessError as e:
        print(f"Error playing sound: {e}")


def pomodoro_timer(work_time=25, short_break=5, long_break=15):
    """
    Implements the Pomodoro Technique.

    Args:
      work_time: Duration of a work interval in minutes.
      short_break: Duration of a short break in minutes.
      long_break: Duration of a long break in minutes.
    """

    try:
        for cycle in range(4):
            # Work interval
            print("Work session started!")
            play_sound("beep7.mp3")
            work_seconds = work_time * 60
            start_time = time.time()
            while time.time() - start_time < work_seconds:
                time_left = work_seconds - (time.time() - start_time)
                minutes_left = int(time_left // 60)
                seconds_left = int(time_left % 60)
                print(f"Time left: {minutes_left:02d}:{seconds_left:02d}", end="\r")
                time.sleep(1)
            print("\nWork session finished!")
            play_sound("beep7.mp3")

            # Short break
            if cycle < 3:
                print("Short break started!")
                play_sound("beep7.mp3")
                short_break_seconds = short_break * 60
                start_time = time.time()
                while time.time() - start_time < short_break_seconds:
                    time_left = short_break_seconds - (time.time() - start_time)
                    minutes_left = int(time_left // 60)
                    seconds_left = int(time_left % 60)
                    print(f"Time left: {minutes_left:02d}:{seconds_left:02d}", end="\r")
                    time.sleep(1)
                print("\nShort break finished!")

                # Long break
                print("Long break started!")
                play_sound("beep7.mp3")
                long_break_seconds = long_break * 60
                start_time = time.time()
                while time.time() - start_time < long_break_seconds:
                    time_left = long_break_seconds - (time.time() - start_time)
                    minutes_left = int(time_left // 60)
                    seconds_left = int(time_left % 60)
                    print(f"Time left: {minutes_left:02d}:{seconds_left:02d}", end="\r")
                    time.sleep(1)
                print("\nLong break finished!")
                play_sound("beep7.mp3")

    except KeyboardInterrupt:
        print("\nPomodoro timer interrupted.")


if __name__ == "__main__":
    input("Press any key to start the Pomodoro timer: ")
    pomodoro_timer()
