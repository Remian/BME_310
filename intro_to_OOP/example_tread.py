from concurrent.futures import ThreadPoolExecutor
import time
import threading



def sub_one():

    for i in range(0,50):

        if (i % 10 == 0):
            time.sleep(1)
            print("\nTread 1 : Slept 1 sec bro!\n")

        else:
            print("Thread 1 : running bro!")


def sub_two():

    for i in range(0,50):
        if(i%10==0):
            time.sleep(1)
            print("\nTread 2 : Slept 1 sec bro!\n")

        else:
            print("Thread 2 : running bro!")


def sub_three():

    for i in range(0, 50):
        if (i % 10 == 0):
            time.sleep(1)
            print("\nTread 3 : Slept 1 sec bro!\n")

        else:
            print("Thread 3 : running bro!")

def executor_thread():
    executor = ThreadPoolExecutor(max_workers=2)
    thread_1 = executor.submit(sub_one)
    thread_2 = executor.submit(sub_two)



thread_example = threading.Thread(target=executor_thread)
thread_example.start()
sub_three()



#java support multithread, python and js single thread
