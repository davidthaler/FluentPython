# Example 17-3 from Fluent Python

from concurrent import futures

from seqential import save_flag, get_flag, show, main

MAX_WORKERS = 5

def download_one(cc):
    img = get_flag(cc)
    show(cc)
    save_flag(img, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    num_workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(num_workers) as executor:
        result = executor.map(download_one, sorted(cc_list))
    return len(list(result))

if __name__ == '__main__':
    main(download_many)