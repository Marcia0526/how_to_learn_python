# from concurrent.futures import ThreadPoolExecutor
# from time import sleep
#
#
# def task(message):
#     sleep(2)
#     return message
#
#
# def main():
#     executor = ThreadPoolExecutor(5)
#     future = executor.submit(task, 'Completed')
#     print(future.done())
#     sleep(2.5)
#     print(future.done())
#     print(future.result())
#
#
# if __name__ == '__main__':
#     main()


# import concurrent.futures
# import urllib.request
#
# URLS = ['http://www.foxnews.com/',
#         'http://www.cnn.com/',
#         'http://europe.wsj.com/',
#         'http://www.bbc.co.uk/',
#         'http://some-made-up-domain.com/']
#
#
# def load_url(url, timeout):
#     with urllib.request.urlopen(url, timeout=timeout) as conn:
#         return conn.read()
#
#
# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#     future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
#     for future in concurrent.futures.as_completed(future_to_url):
#         url = future_to_url[future]
#         try:
#             data = future.result()
#         except Exception as exc:
#             print('%r generated an exception: %s' % (url, exc))
#         else:
#             print('%r page is %d bytes' % (url, len(data)))


from concurrent.futures import ThreadPoolExecutor
import time

values = [2, 3, 4, 5]


def square(n):
    return n * n


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        start = time.time()
        results = executor.map(square, values)
        for result in results:
            print(result)
        end = time.time()
        print('done in {:.8f} seconds'.format(end - start))


if __name__ == '__main__':
    main()
    # start = time.time()
    # square(2)
    # square(3)
    # square(4)
    # square(5)
    # end = time.time()
    # print('done in {:.8f} seconds'.format(end - start))



