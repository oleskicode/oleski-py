import threading
import time


def walk_the_dog(dog_name):
    print(f"Walking the dog {dog_name} - Start")
    time.sleep(4)
    print(f"Walking the dog {dog_name} - End")


def take_out_trash():
    print("Taking out the trash - Start")
    time.sleep(3)
    print("Taking out the trash - End")


def check_mailbox():
    print("Checking the mailbox - Start")
    time.sleep(2)
    print("Checking the mailbox - End")


# walk_the_dog()
# take_out_trash()
# check_mailbox()

chore1 = threading.Thread(target=walk_the_dog, args=("Barkey",))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=check_mailbox)
chore3.start()

# waiting for threads to finish
chore1.join()
chore2.join()
chore3.join()

print("All tasks are complete!")
