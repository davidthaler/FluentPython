# Example 17-4 from Fluent Python, with explicit creation and 
# result collection from the futures.

from concurrent import futures

from seqential import save_flag, get_flag, show, main

def download_one(cc):
    img = get_flag(cc)
    show(cc)
    save_flag(img, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        todo = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            todo.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(todo):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)

if __name__ == '__main__':
    main(download_many)