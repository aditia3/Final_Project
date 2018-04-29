import numpy as np
import pandas as pd

class CallCenter(object):

    def __init__(self, num, call_duration, hold_time):
        self.num = num;
        self.call_duration = call_duration
        self.hold_time = hold_time


    def __repr__(self):
       return "CallCenter('{}', '{}', '{}')".format(self.num, self.call_duration, self.hold_time)

if __name__ == '__main__':
    d = []
    for i in range(5):
        num = i+1

        call_duration = np.random.randint(1, 10)
        print("CallDuration",call_duration)

        hold_time = np.random.randint(1, 10)
        print("HoldTime",hold_time)

        disney = CallCenter(num,call_duration,hold_time)
        disney.attr = 5
        d.append(disney)
    print(d)
    for i in range(len(d)):
        if len(d) != 1 and len(d) != 0:
            wait_time = d[0].call_duration
            print("Normal Pop",d[0])
            d.pop(0)
            call_assigned = 1
            count = 0
            while True:  # starting first loop
                count += 1
                for member in d:
                    if member.hold_time == count:
                        print("Dropout counter", member)
                        index = d.index(member)
                        d.pop(index)
                        #break
                """
                for k in range(0,len(d)):
                    if len(d) != 1:
                        if d[k].hold_time == count:
                            print("Dropout counter", d[k])
                            d.pop(k)
                            break
                """
                if wait_time == count:
                    break
        elif len(d) == 1:
            print("NormalPopLastEntry",d[0])
            d.pop(0)
