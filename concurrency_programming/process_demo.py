import threading
import time


def sleepy_man(secs):
    print('Starting to sleep inside')
    time.sleep(secs)
    print('Woke up inside')


x = threading.Thread(target=sleepy_man, args=(1,))
x.start()
print(threading.activeCount())
time.sleep(1.1)
print('Done')


# import threading
# import time
#
#
# def sleepy_man(secs):
#     print('Starting to sleep inside - Iteration {}'.format(5 - secs))
#     time.sleep(secs)
#     print('Woke up inside - Iteration {}'.format(5 - secs))
#
#
# for i in range(3):
#     x = threading.Thread(target=sleepy_man, args=(5 - i,))
#     x.start()
#
# print('Active threads- ', threading.activeCount())


# import time
#
#
# def sleepy_man():
#     print('Starting to sleep')
#     time.sleep(1)
#     print('Done sleeping')
#
#
# tic = time.time()
# sleepy_man()
# sleepy_man()
# toc = time.time()
#
# print('Done in {:.4f} seconds'.format(toc - tic))


# import multiprocessing
# import time
# from multiprocessing.dummy import freeze_support
#
#
# def sleepy_man():
#     print('Starting to sleep')
#     time.sleep(1)
#     print('Done sleeping')
#
#
# if __name__ == '__main__':
#     freeze_support()
#     tic = time.time()
#     p1 = multiprocessing.Process(target=sleepy_man)
#     p2 = multiprocessing.Process(target=sleepy_man)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     toc = time.time()
#     print('Done in {:.4f} seconds'.format(toc-tic))


# import multiprocessing
# import time
# from multiprocessing.dummy import freeze_support
#
#
# def sleepy_man():
#     print('Starting to sleep')
#     time.sleep(1)
#     print('Done sleeping')
#
#
# if __name__ == '__main__':
#     freeze_support()
#     tic = time.time()
#     process_list = []
#     for i in range(10):
#         p = multiprocessing.Process(target=sleepy_man)
#         p.start()
#         process_list.append(p)
#
#     for process in process_list:
#         process.join()
#
#     toc = time.time()
#
#     print('Done in {:.4f} seconds'.format(toc - tic))


# import multiprocessing
# import time
# from multiprocessing.dummy import freeze_support
#
#
# def sleepy_man(sec):
#     print('Starting to sleep')
#     time.sleep(sec)
#     print('Done sleeping')
#
#
# if __name__ == '__main__':
#     freeze_support()
#     tic = time.time()
#     process_list = []
#     for i in range(10):
#         p = multiprocessing.Process(target=sleepy_man, args=[2])
#         p.start()
#         process_list.append(p)
#
#     for process in process_list:
#         process.join()
#
#     toc = time.time()
#
#     print('Done in {:.4f} seconds'.format(toc-tic))


# import multiprocessing
# import time
# from multiprocessing.dummy import freeze_support
#
#
# def sleepy_man(sec):
#     print('Starting to sleep for {} seconds'.format(sec))
#     time.sleep(sec)
#     print('Done sleeping for {} seconds'.format(sec))
#
#
# if __name__ == '__main__':
#     print("Number of cpu : ", multiprocessing.cpu_count())
#     freeze_support()
#     tic = time.time()
#
#     pool = multiprocessing.Pool(5)
#     pool.map(sleepy_man, range(1, 11))
#     # pool.apply(sleepy_man, range(1, 11))
#     pool.close()
#     pool.join()
#
#     toc = time.time()
#
#     print('Done in {:.4f} seconds'.format(toc - tic))
