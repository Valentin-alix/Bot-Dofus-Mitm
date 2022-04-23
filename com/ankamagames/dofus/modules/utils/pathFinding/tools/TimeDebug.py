from time import perf_counter
from types import FunctionType


class TimeDebug:

    lastTime: int = perf_counter()

    def __init__(self):
        super().__init__()

    @classmethod
    def reset(cls, value: int = -1) -> None:
        if value < 0:
            cls.lastTime = perf_counter()
        else:
            cls.lastTime = value

    @classmethod
    def getElapsedTime(cls, autoReset: bool = True) -> int:
        time: int = perf_counter()
        elapsedTime: int = time - cls.lastTime
        if autoReset:
            cls.reset(time)
        return elapsedTime

    @classmethod
    def exec(cls, f: FunctionType, onEnd: FunctionType = None) -> float:
        duration: float = None
        if f != None:
            cls.reset()
            f()
            duration = cls.getElapsedTimeInSeconds()
            if onEnd != None:
                onEnd(duration)
            return duration
        return -1


if __name__ == "__main__":
    from time import sleep

    TimeDebug.reset()
    sleep(1)
    print(TimeDebug.getElapsedTime())
