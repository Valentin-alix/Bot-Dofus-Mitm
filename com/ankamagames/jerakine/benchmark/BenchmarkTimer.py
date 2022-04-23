from threading import Timer
from com.ankamagames.jerakine.benchmark.FileLoggerEnum import FileLoggerEnum
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(FileLoggerEnum.BENCHMARKTIMERS)


class BenchmarkTimer:

    startedTimers = set["BenchmarkTimer"]()

    startWithoutResetCount: int = 0

    hasBeenReset: bool = True

    name: str = "unamed"

    def __init__(self, delay: int, repeatCount: int = 0, name: str = ""):
        self.name = name
        self.repeatCount = repeatCount
        self.delay = delay

    def printUnstoppedTimers(self) -> None:
        unstoppedTimersCount: int = 0
        for timer in BenchmarkTimer.startedTimers:
            unstoppedTimersCount += 1
            logger.info("This Timer is unstopped: ")
            logger.info("Total unstopped Timers: " + str(unstoppedTimersCount))
            logger.info("Stop Recording BenchmarkTimers.")

    def start(self) -> None:
        # TODO: fix this shit
        super().start()
        if not self.hasBeenReset:
            self.startWithoutResetCount += 1
            logger.info("This Timer has not been reset before start: " + self.name)
        if not BenchmarkTimer.startedTimers.get(self):
            BenchmarkTimer.startedTimers.add(self)
        self.hasBeenReset = False

    def stop(self) -> None:
        super().stop()
        del BenchmarkTimer.startedTimers[self]

    def reset(self) -> None:
        super().reset()
        self.hasBeenReset = True
