# Example 17-6 from Fluent Python

from time import sleep, strftime
from concurrent import futures

def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)

def loiter(n):
    msg = '{}loiter({}): doing nothing for {}sec'
    display(msg.format('\t' * n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t' * n, n))
    return n * 10

def main():
    display('Script Starting')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(5))
    display('results: ', results)
    display('Waiting for individual results:')
    for i, result in enumerate(results):
        display('result {}: {}'.format(i, result))

main()