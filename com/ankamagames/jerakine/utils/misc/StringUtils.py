from com.ankamagames.jerakine.logger.Logger import Logger
import re

logger = Logger(__name__)


class StringUtils:
    accents: str = (
        "ŠŒŽšœžÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜŸÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýÿþ"
    )
    pattern = None

    def fill(str: str, len: int, char: str, before: bool = True) -> str:
        if not char or not len(char):
            return str
        while len(str) != len:
            if before:
                str = char + str
            else:
                str += char
        return str

    def initPatterns():
        StringUtils.pattern = {
            "Š": "S",
            "Œ": "Oe",
            "Ž": "Z",
            "š": "s",
            "œ": "oe",
            "ž": "z",
            "À": "A",
            "Á": "A",
            "Â": "A",
            "Ã": "A",
            "Ä": "A",
            "Å": "A",
            "Æ": "Ae",
            "Ç": "C",
            "È": "E",
            "É": "E",
            "Ê": "E",
            "Ë": "E",
            "Ì": "I",
            "Í": "I",
            "Î": "I",
            "Ï": "I",
            "Ð": "D",
            "Ñ": "N",
            "Ò": "O",
            "Ó": "O",
            "Ô": "O",
            "Õ": "O",
            "Ö": "O",
            "Ø": "O",
            "Ù": "U",
            "Ú": "U",
            "Û": "U",
            "Ü": "U",
            "Ÿ": "Y",
            "Ý": "Y",
            "Þ": "Th",
            "ß": "ss",
            "à": "a",
            "á": "a",
            "â": "a",
            "ã": "a",
            "ä": "a",
            "å": "a",
            "æ": "ae",
            "ç": "c",
            "è": "e",
            "é": "e",
            "ê": "e",
            "ë": "e",
            "ì": "i",
            "í": "i",
            "î": "i",
            "ï": "i",
            "ð": "d",
            "ñ": "n",
            "ò": "o",
            "ó": "o",
            "ô": "o",
            "õ": "o",
            "ö": "o",
            "ø": "o",
            "ù": "u",
            "ú": "u",
            "û": "u",
            "ü": "u",
            "ý": "y",
            "ÿ": "y",
            "þ": "th",
        }

    def concatSamestr(pstr: str, pstrToConcat: str) -> str:
        firstIndex: int = pstr.find(pstrToConcat)
        previousIndex: int = 0
        currentIndex: int = firstIndex
        while currentIndex != -1:
            previousIndex = currentIndex
            currentIndex = pstr.find(pstrToConcat, previousIndex + 1)
            if currentIndex == firstIndex:
                break
            if currentIndex == previousIndex + len(pstrToConcat):
                pstr = pstr[0:currentIndex] + pstr[currentIndex + len(pstrToConcat) :]
                currentIndex -= len(pstrToConcat)
        return pstr

    def getDelimitedText(
        pText: str,
        pFirstDelimiter: str,
        pSecondDelimiter: str,
        pIncludeDelimiter: bool = False,
    ) -> list[str]:
        r = re.findall(
            re.escape(pFirstDelimiter) + r"(.*?)" + re.escape(pSecondDelimiter), pText
        )
        r = [_.lstrip(pFirstDelimiter).rstrip(pSecondDelimiter) for _ in r]
        if pIncludeDelimiter:
            r = [pFirstDelimiter + _ + pSecondDelimiter for _ in r]
        return r

    def getAllIndexOf(pc: str, pText: str) -> list[int]:
        return [i for i, c in enumerate(pText) if c == pc]

    def noAccent(src: str) -> str:
        if StringUtils.pattern is None:
            StringUtils.initPatterns()
        return StringUtils.decomposeUnicode(src)

    def decomposeUnicode(src: str) -> str:
        toCheck: str = (
            src if len(StringUtils.accents) < len(src) else StringUtils.accents
        )
        toLoop: str = (
            StringUtils.accents if len(StringUtils.accents) < len(src) else src
        )
        for c in toLoop:
            if c in toCheck:
                src = re.sub(c, StringUtils.pattern[c], src)
        return src


if __name__ == "__main__":
    r = StringUtils.getAllIndexOf("k", "dsqkdjklsjkhalidskdjkj")
    print(r)
