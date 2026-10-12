import time
from collections.abc import Generator

from loop.loop import EventLoop


def trampoline(event_loop: EventLoop, t: float):
    dt = time.monotonic() - t
    print(f"trampoline tick {dt:.1f}s")
    event_loop.call_later(0.2, trampoline, event_loop, t)


def is_palindrome(num: int) -> bool:
    if num // 10 == 0:
        return False

    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    return num == reversed_num


def infinite_palindrome() -> Generator[int, int | None, None]:
    num = 0
    while True:
        if is_palindrome(num):
            i = yield num
            if i is not None:
                num = i
        num += 1


if __name__ == "__main__":
    loop = EventLoop()
    loop.call_soon(trampoline, loop, time.monotonic())
    loop.call_later(5, loop.stop)
    loop.run_forever()
