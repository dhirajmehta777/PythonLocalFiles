"""
Multi Threading and Multi Tasking
"""
"""
There are two types of multi tasking:
1. Process based multi tasking
2. Thread based multi tasking
"""
"""
1.--->
Each task is seperate and independent process 
here tasks are not same as well as they are not dependent on each other
These type of multi tasking is best suitable at OS level and not at application level very rarely used
Ex:
Typing a python program in a editor
listening audio songs from the same system
downloading new songs from internet
"""

"""
2.--->
Each task is an independent part of the same program is called as thread.
Same program with multiple treads.
Most commonly used concept at application level.
A flow of execution is considered as a thread.
It is a python object.
for every thread an independent job is available.
once we started the tread that job is automatically that thread is responsible for completing that job.
The biggest advantage of multi threading is by default the performance is going to improve as we are executing the threads simultaeneously

for example we have one program consists of 10k lines if we execute, it will take 10 minutes to complete.
suppose one program consists of two independent parts that is first 5k lines of code is for customer1 and
second 5k lines of code belongs to customer2 and if we execute these two independent parts simultaeneously
then we can execute in less time as compare to earlier so these process is called as thread based multi tasking
and each independent part is treated as one thread

for example Gmail, simultaeneously at a time we can request to server upto 60 times that means for each requesst
a seperate thread is allocated.

where we can use multi threading concept happily we can use multi media graphics, animations, video games, server
implementations

Python provides inbuilt modules to develop multi threaded applications, that is threading module hence it has 
inbuilt threading module therefore multi threading program is very easy in python

"""
# import threading
# print('current executing thread:',threading.current_thread().getName())#--->MAinThread

"""
There are three ways we can define the thread:
1. Creating a thread without using any class
2. Creating a thread by extending thread class
3. Creating a thread without extending a thread class
"""
"""
1.--->Example
"""
# from threading import *
# def display():
#     print('child thread name:',current_thread().getName())
#     for i in range(10):
#         print('child thread')
#
# t=Thread(target=display)#creation of thread object to execute display, Thread is a predefined class present in a threading module

#t.start()#here the line 64 qnd 66 both are executed by maun thread itself once the creation of child thread and start of the thread is done then at that time both the treads will execute independenly

# print('Main thread name:',current_thread().getName())
# for i in range(10):
#     print('Main Thread')

#here in which order it may execute the job must be completed then only we have to go for multi threading concept were order is not maintained
#Here both the for loops executes simulteneously without mainting order so that is called as threading

"""
2.--->Example
"""
from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(10):
            print('child thread')
t=MyThread()
t.start()
for i in range(10):
    print('Main thread')
