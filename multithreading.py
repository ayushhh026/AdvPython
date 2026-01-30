# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.thread(target=my_function)

import threading
import time
def walk_dog(first):
    time.sleep(8)#have to wait 8 seconds after running the function
    print(f"You finished walking the {first}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")
#-------------------------------------------------------
# walk_dog()
# take_out_trash()
# get_mail()
#-------------------------------------------------------
# these are executed sequentially in a single threead one by one
# so when reachind get_mail you will take 8+2+4 seconds

# create thread to solve in mutithreads
chore1 = threading.Thread(target=walk_dog,args=("Scooby",))# if it has argument right in keyword arguments in a tupple
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

# here the smalled time taken will be done first simultaneously output will be:-
# You take out the trash
# You get the mail
# You finished walking the dog

chore1.join() # .join() allows to proceed only if all the chores are commplete
chore2.join()
chore2.join()

print("All chores are complete")
