from concurrent.futures import ThreadPoolExecutor

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

executor()