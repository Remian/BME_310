from concurrent.futures import ThreadPoolExecutor
import threading

def read_arduino_1_data():

    while(True):
        print("arduino 1: Sending Sensor Data")


def read_sensor_2_data():
    while (True):
        print("arduino 2: Sending Sensor Data")

def executor():
    executor = ThreadPoolExecutor(max_workers=2)
    thread_1 = executor.submit(read_arduino_1_data)
    thread_2 = executor.submit(read_sensor_2_data)

def UI_component():
    while(True):
        print("UI Component: Checking for User Input")

def thread_func():
    thread = threading.Thread(target=executor())
    thread.start()
    UI_component()

thread_func()
