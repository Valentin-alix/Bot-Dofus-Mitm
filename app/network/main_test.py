from importlib import import_module
import os
from pathlib import Path
from pstats import SortKey, Stats
import sys
from cProfile import Profile
from time import perf_counter
from timeit import timeit

from numpy import number


sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from types_.parsed_message import ParsedMessageHandler
from types_.dofus.utils import CLASSES_BY_NAME
from network.utils import convert_snake_case_to_camel_case


if __name__ == "__main__":
    before = perf_counter()
    print(CLASSES_BY_NAME.get("ForceAccountStatusMessage"))
    print(perf_counter() - before)
