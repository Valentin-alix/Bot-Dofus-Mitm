from typing import Callable

from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot


class WorkerSignals(QObject):
    function_result = pyqtSignal(object)


class Worker(QObject):
    def __init__(self, func: Callable, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.signals = WorkerSignals()
        self.func = func

    @pyqtSlot()
    def run(self):
        res = self.func()
        self.signals.function_result.emit(res)


def run_in_background(func: Callable) -> tuple[QThread, Worker]:
    worker = Worker(func)
    thread = QThread()

    worker.moveToThread(thread)
    thread.started.connect(worker.run)
    worker.signals.function_result.connect(lambda: on_finished_thread(worker, thread))
    thread.start()
    return thread, worker


def on_finished_thread(worker: Worker, thread: QThread) -> None:
    worker.deleteLater()
    thread.quit()
    thread.wait()
