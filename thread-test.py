import threading
import time

def th(sec: int):
    time.sleep(sec)
    print("thread")

t = threading.Thread(target=th,args=(10,))
t.start()
print("hello")






# def threaded(f, daemon=False):
#     import queue

#     def wrapped_f(q, *args, **kwargs):
#         '''this function calls the decorated function and puts the 
#         result in a queue'''
#         ret = f(*args, **kwargs)
#         q.put(ret)

#     def wrap(*args, **kwargs):
#         '''this is the function returned from the decorator. It fires off
#         wrapped_f in a new thread and returns the thread object with
#         the result queue attached'''

#         q = queue.Queue()

#         t = threading.Thread(target=wrapped_f, args=(q,)+args, kwargs=kwargs)
#         t.daemon = daemon
#         t.start()
#         t.result_queue = q        
#         return t

#     return wrap

# @threaded
# def long_task(x):
#     import time
#     x = x + 5
#     time.sleep(5)
#     return x

# # does not block, returns Thread object
# y = long_task(10)
# # print(y)

# # this blocks, waiting for the result
# result = y.result_queue.get()
# print(result)

# for i in range(5):
#     print(i)