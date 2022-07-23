import datetime
from time import time


def timeit(func):
    def inner(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"耗时{end_time - start_time}")
        return result

    return inner


@timeit
def test(
    x,
    y,
):
    return (x**2) * (y**2)


if __name__ == "__main__":
    print(test(1, 2))
