class Task(object):

    def __init__(self, param):
        print("Executing hard to execute task with: %s" % param)

    def im_not_lazy(self):
        return "ddddd"

from python_settings.conf import LazySetting

LAZY_TASK = LazySetting(Task, "Making it lazy")
