class Task(object):

    def __init__(self, param):
        print("Executing hard to execute task initializer: %s" % param)


import time


class HeavyInitializationClass(object):
    def __init__(self, *args):
        time.sleep(1)
        print("One second delay after hard task")


from python_settings import LazySetting

LAZY_TASK = LazySetting(Task, "Making it lazy")

LAZY_TASK_HEAVY_INITIALIZATION = LazySetting(HeavyInitializationClass, "127.0.0.1:4222")
