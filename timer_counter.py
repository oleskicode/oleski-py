import time

inputSeconds = input("Set timer seconds:")
# inputSeconds = 3663
inputSeconds = int(inputSeconds)

for x in range(inputSeconds, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(0.3)

print("Time's up!")
