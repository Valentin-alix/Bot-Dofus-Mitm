from pathlib import Path
from types import FunctionType
from com.ankamagames.jerakine.logger.Logger import Logger


logger = Logger(__name__)


class FileLoader:
    def __init__(self):
        super().__init__()

    def loadExternalFile(self, path: str, onLoaded: FunctionType) -> None:
        uri: Path = Path(path)
        loader: IResourceLoader = ResourceLoaderFactory.getLoader(
            ResourceLoaderType.SINGLE_LOADER
        )
        loader.addEventListener(
            ResourceErrorEvent.ERROR, self.loaderError, False, 0, True
        )
        loader.addEventListener(
            ResourceLoadedEvent.LOADED, self.loaderComplete, False, 0, True
        )
        if onLoaded != None:
            loader.addEventListener(ResourceLoadedEvent.LOADED, onLoaded, False, 0)
        try:
            loader.load(uri)
        except Exception as e:
            logger.error("Unable to load requested document. ", exc_info=True)

    def removeLoadingListeners(self, loader: IResourceLoader) -> None:
        loader.removeEventListener(ResourceErrorEvent.ERROR, self.loaderError)
        loader.removeEventListener(ResourceLoadedEvent.LOADED, self.loaderComplete)

    def loaderComplete(self, e: ResourceLoadedEvent) -> None:
        self.removeLoadingListeners(e.dispatcher)
        logger.info(e.uri + "successfully loaded !")

    def loaderError(self, e: ResourceErrorEvent) -> None:
        self.removeLoadingListeners(e.dispatcher)
        logger.error(e.uri + " loading failed => " + e.errorMsg)
