import os
import time
import sys
from datetime import datetime, timedelta


def shutdown_pc():
    """Shutdown the PC using system commands"""
    try:
        if os.name == 'nt':  # Windows
            os.system("shutdown /s /t 1")
        elif os.name == 'posix':  # Linux/Mac
            os.system("sudo shutdown -h now")
        else:
            print("Unsupported operating system")
    except Exception as e:
        print(f"Error during shutdown: {e}")


def countdown_timer(hours=1):
    """Countdown timer with live display"""
    total_seconds = hours * 3600  # Convert hours to seconds

    # Calculate end time
    end_time = datetime.now() + timedelta(seconds=total_seconds)
    print(f"🕐 PC will shutdown at: {end_time.strftime('%I:%M:%S %p')}")
    print("⚠️  Press Ctrl+C to cancel the shutdown timer\n")

    try:
        while total_seconds > 0:
            # Calculate hours, minutes, seconds remaining
            hours_left = total_seconds // 3600
            minutes_left = (total_seconds % 3600) // 60
            seconds_left = total_seconds % 60

            # Display countdown
            time_str = f"{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}"
            print(f"\r⏳ Time remaining: {time_str}", end="", flush=True)

            # Wait 1 second
            time.sleep(1)
            total_seconds -= 1

            # Show warnings at specific intervals
            if total_seconds == 300:  # 5 minutes warning
                print("WARNING: PC will shutdown in 5 minutes!")
            elif total_seconds == 60:  # 1 minute warning
                print(" WARNING: PC will shutdown in 1 minute!")
            elif total_seconds == 10:  # 10 seconds warning
                print(" WARNING: PC will shutdown in 10 seconds!")

        print("Shutting down PC now")
        shutdown_pc()

    except KeyboardInterrupt:
        print("Shutdown timer cancelled by user")
        sys.exit(0)


def main():
    print("=" * 50)
    print("🖥️  PC SHUTDOWN TIMER")
    print("=" * 50)

    # Ask user for confirmation
    response = input("This will shutdown your PC in 1.5 hours. Continue? (y/n): ")

    if response.lower() in ['y', 'yes']:
        print("Starting 2-hour shutdown timer...")
        countdown_timer(2)  # 2 hours
    else:
        print("Shutdown timer cancelled")
        sys.exit(0)


if __name__ == "__main__":
    main()