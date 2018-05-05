import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt


class CallCenter(object):

    def __init__(self, num, call_duration, hold_time):
        self.num = num
        self.call_duration = call_duration
        self.hold_time = hold_time

    def __repr__(self):
        return "CallCenter('{}', '{}', '{}')".format(self.num, self.call_duration, self.hold_time)


if __name__ == '__main__':
    random.seed(0)
    rep2 = []
    rep1 = []
    total_wait_time = 0
    n = 7
    for rep in range(1, 4):
        print('aaaaaaa', rep)
        drop_avg1 = 0
        drop_avg2 = 0
        drop_avg3 = 0

        average_speed_answer1_1 = 0
        average_speed_answer2_2 = 0
        average_speed_answer3_3 = 0
        for k in range(10):
            print('kkkkkkkkk', k)
            d = []
            e = []

            drop_count = 0
            normal_pop_count = 0

            # n = int(random.triangular(4, 20, 50))
            n = 7
            print('number of callers', n)
            for i in range(n):
                num = i + 1

                # call_duration = np.random.randint(1, 10)
                call_duration = int(random.normalvariate(5, 1.5))
                while call_duration <= 0:
                    call_duration = int(random.normalvariate(5, 1.5))

                if not call_duration:
                    print("I am zero")
                # print("CallDuration",call_duration)

                # hold_time = np.random.randint(1, 12)
                hold_time = int(random.normalvariate(15, 4.5))
                while hold_time <= 0:
                    hold_time = int(random.normalvariate(5, 1.5))
                if not hold_time:
                    print("I am zero hold")
                # print("HoldTime",hold_time)

                disney = CallCenter(num, call_duration, hold_time)
                disney.attr = n
                d.append(disney)
            print(d)
            print('number of representatives available:', rep)
            if len(d) == n:
                if rep == 3:
                    e.append(d[0].call_duration)
                    print("Normal popup", d[0])
                    d.pop(0)
                    normal_pop_count += 1
                    e.append(d[0].call_duration)
                    print("Normal popup", d[0])
                    d.pop(0)
                    normal_pop_count += 1
                    e.append(d[0].call_duration)
                    print("Normal popup", d[0])
                    d.pop(0)
                    normal_pop_count += 1
                    print('list of callers assigned for 3 reps', e)
                if rep == 2:
                    e.append(d[0].call_duration)
                    print("Normal popup", d[0])
                    d.pop(0)
                    normal_pop_count += 1
                    e.append(d[0].call_duration)
                    print("Normal popup", d[0])
                    d.pop(0)
                    normal_pop_count += 1
                    print('list of callers assigned 2 reps', e)
                if rep == 1:
                    e.append(d[0].call_duration)
                    print("Normal popup", d[0])
                    d.pop(0)
                    normal_pop_count += 1
                    print('list of callers assigned 1 rep', e)

            drop1 = 0
            drop2 = 0
            drop3 = 0
            average_speed_answer1 = 0
            average_speed_answer2 = 0
            average_speed_answer3 = 0
            total_wait_time = 0

            for i in range(len(d)):

                if len(d) != 0:

                    call_assigned = 1
                    count = 0
                    wait_time = min(e)
                    print("Min e Rujuta = ", min(e))
                    total_wait_time = total_wait_time + wait_time
                    print('Aditiiiii total wait time', total_wait_time)
                    #print("Wait Time",wait_time)
                    # print(wait_time)
                    for member in d:
                        if member.hold_time <= wait_time:
                            print("Droupout counter", member)
                            drop_count += 1
                            d.remove(member)

                    while True:  # starting first loop
                        count += 1

                        if wait_time == count:
                            print('cnt..', count)
                            for member in d:
                                member.hold_time = member.hold_time - wait_time
                                if member.hold_time <= 0:
                                    print("Droupout counter", member)
                                    drop_count += 1
                                    d.remove(member)
                            e = [x - wait_time for x in e]
                            print('e..', e)
                            break

                    cnt = e.count(0)
                    print('count of 0 mins in caller list:', e.count(0))
                    if 0 in e:
                        if len(d) != 0:
                            if cnt == 1:
                                print('drop from e.. 0')
                                e.remove(0)
                                print('appending next val to e', d[0].call_duration)
                                e.append(d[0].call_duration)
                                print('new list e..', e)
                                print('Normal pop from queue..', d[0])
                                d.pop(0)
                                #print('hello min e', min(e))
                                #total_wait_time += min(e)
                                #print('hello.. min e', min(e))
                                #print("total_wait_time = ",total_wait_time)
                                normal_pop_count += 1
                            if cnt == 2:
                                if len(d) > 1:
                                    print('drop from e.. 0')
                                    e.remove(0)
                                    e.remove(0)
                                    print('appending next val to caller list', d[0].call_duration)
                                    e.append(d[0].call_duration)
                                    print('appending next val to caller list', d[1].call_duration)
                                    e.append(d[1].call_duration)
                                    print('new list of callers', e)
                                    print('Normal pop from queue', d[0])
                                    d.pop(0)
                                    normal_pop_count += 1
                                    print('Normal pop from queue', d[0])
                                    d.pop(0)
                                    normal_pop_count += 1
                                    print('Minimum e.......',min(e))
                                    #print('Aditiiiii total_wait_time', total_wait_time)
                                    #total_wait_time += min(e)
                                    #print('Aditiiiiiiii total wait time', total_wait_time)
                                elif len(d) == 1:
                                    print('drop from e.... 0')
                                    e.remove(0)
                                    print('appending next val to caller list..', d[0].call_duration)
                                    e.append(d[0].call_duration)
                                    print('new list of callers', e)
                                    print('list of queue..', d)
                                    d.pop(0)
                                    #print('Minimum e........', min(e))
                                    #total_wait_time += min(e)
                                    #print("Toal wait time",total_wait_time)

                            if cnt == 3:
                                if len(d) > 2:
                                    print('drop from e.. 0')
                                    e.remove(0)
                                    e.remove(0)
                                    e.remove(0)
                                    print('appending next val to caller list', d[0].call_duration)
                                    e.append(d[0].call_duration)
                                    print('appending next val to caller list', d[1].call_duration)
                                    e.append(d[1].call_duration)
                                    print('appending next val to caller list', d[2].call_duration)
                                    e.append(d[2].call_duration)
                                    print('new list of callers', e)
                                    print('Normal pop from queue', d[0])
                                    d.pop(0)
                                    normal_pop_count += 1
                                    print('Normal pop from queue', d[0])
                                    d.pop(0)
                                    normal_pop_count += 1
                                    print('Normal pop from queue', d[0])
                                    d.pop(0)
                                    normal_pop_count += 1
                                    print('Minimum---', min(e))
                                    total_wait_time += min(e)
                                elif len(d) == 2:
                                    print('drop from e -> 0')
                                    e.remove(0)
                                    e.remove(0)
                                    print('appending next val to caller list...', d[0].call_duration)
                                    e.append(d[0].call_duration)
                                    print('appending next val to caller list..', d[1].call_duration)
                                    e.append(d[1].call_duration)
                                    print('new list of callers', e)
                                    print('Normal pop from queue -->', d[0])
                                    d.pop(0)
                                    normal_pop_count += 1
                                    print('Normal pop from queue -->', d[0])
                                    d.pop(0)
                                    normal_pop_count += 1
                                    print('Minimum----->>', min(e))
                                    total_wait_time += min(e)
                                elif len(d) == 1:
                                    print('drop from e:: 0')
                                    e.remove(0)
                                    print('appending next val to caller list:', d[0].call_duration)
                                    e.append(d[0].call_duration)
                                    print('new list of callers', e)
                                    print('Normal pop from queue .. ', d[0])
                                    print('list of queue.. ..', d)
                                    d.pop(0)
                                    normal_pop_count += 1
                                    print('Minimum------>>', min(e))
                                    total_wait_time += min(e)
                        elif len(d) == 0:
                            total_wait_time += min(e)
                            print('Aditiiiiiiii total wait time', total_wait_time)
            print('drop count.. Aditi', drop_count)
            if rep == 1:
                drop1 = (drop_count / n) * 100
                print('drop1', drop1)
                drop_avg1 += drop1

                print("Normal Pop Rujuta", normal_pop_count)
                total_wait_time += min(e)
                print("Total wait Rujuta.....", total_wait_time)
                average_speed_answer1 = total_wait_time / normal_pop_count
                print("AvG speed Rujuta", average_speed_answer1)

                average_speed_answer1_1 += average_speed_answer1
                print("Ag speed 1 Rujuta", average_speed_answer1_1)
            if rep == 2:
                drop2 = (drop_count / n) * 100
                print('drop2', drop2)
                drop_avg2 += drop2
                total_wait_time += min(e)
                print("Total wait Rujuta.....", total_wait_time)
                print("Normal Pop Rujuta", normal_pop_count)
                print("Last e values=", min(e))
                average_speed_answer2 = total_wait_time / normal_pop_count
                print('Aditi...', average_speed_answer2)
                average_speed_answer2_2 += average_speed_answer2
            if rep == 3:
                drop3 = (drop_count / n) * 100
                print('drop3', drop3)
                drop_avg3 += drop3
                total_wait_time += min(e)
                print("Total wait Rujuta.....", total_wait_time)
                average_speed_answer3 = total_wait_time / normal_pop_count
                average_speed_answer3_3 += average_speed_answer3
        if rep == 1:
            print('drop for 1 rep', drop_avg1 / 10)
            rep1.append(drop_avg1 / 10)
            rep2.append(average_speed_answer1_1 / 10)
        elif rep == 2:
            print('drop for 2 rep', drop_avg2 / 10)
            rep1.append(drop_avg2 / 10)
            rep2.append(average_speed_answer2_2 / 10)
        elif rep == 3:
            print('drop for 3 rep', drop_avg3 / 10)
            rep1.append(drop_avg3 / 10)
            rep2.append(average_speed_answer3_3 / 10)
        else:
            print('none')

rep = [1, 2, 3]
print(rep2)
plt.scatter(rep, rep1)
plt.xlabel('No of Representatives')
plt.ylabel('Avg. dropout percentage')
plt.title('Avg dropout Percentage vs No of Reprenstatives')
plt.show()
print(rep)
print(rep1)
