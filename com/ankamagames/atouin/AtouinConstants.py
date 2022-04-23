import math
from com.ankamagames.jerakine.types.positions.MapPoint import Point


class AtouinConstants:

    DEBUG_FILES_PARSING: bool = False

    DEBUG_FILES_PARSING_ELEMENTS: bool = False

    MAP_WIDTH: int = 14

    MAP_HEIGHT: int = 20

    MAP_CELLS_COUNT: int = 560

    ADJACENT_CELL_LEFT_MARGIN: int = 5

    ADJACENT_CELL_RIGHT_MARGIN: int = 5

    CELL_WIDTH: int = 86

    CELL_HALF_WIDTH: int = 43

    CELL_HEIGHT: int = 43

    CELL_HALF_HEIGHT: float = 21.5

    ALTITUDE_PIXEL_UNIT: int = 10

    LOADERS_POOL_INITIAL_SIZE: int = 30

    LOADERS_POOL_GROW_SIZE: int = 5

    LOADERS_POOL_WARN_LIMIT: int = 100

    OVERLAY_MODE_ALPHA: float = 0.7

    MAX_ZOOM: int = 4

    MAX_GROUND_CACHE_MEMORY: int = 5

    GROUND_MAP_VERSION: int = 2

    MIN_DISK_SPACE_AVAILABLE: float = math.pow(2, 20) * 512

    PSEUDO_INFINITE: int = 63

    PATHFINDER_MIN_X: int = 0

    PATHFINDER_MAX_X: int = 33 + 1

    PATHFINDER_MIN_Y: int = -19

    PATHFINDER_MAX_Y: int = 13 + 1

    VIEW_DETECT_CELL_WIDTH: int = 2 * CELL_WIDTH

    MIN_MAP_X: int = -255

    MAX_MAP_X: int = 255

    MIN_MAP_Y: int = -255

    MAX_MAP_Y: int = 255

    RESOLUTION_HIGH_QUALITY: Point = Point(1978, 1024)

    RESOLUTION_MEDIUM_QUALITY: Point = Point(1483.5, 768)

    RESOLUTION_LOW_QUALITY: Point = Point(989, 512)

    MOVEMENT_WALK: int = 1

    MOVEMENT_NORMAL: int = 2

    WIDESCREEN_BITMAP_WIDTH: int = 0
