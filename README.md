# Setup :

- Install Jpexs-decompiler to decompile DofusInvoker.swf : https://github.com/jindrapetrik/jpexs-decompiler
- Launch init.bat to setup environment
- Create .env file
    - example of .env :
      ```
      D2O_FOLDER="C:\\Users\\valen\\AppData\\Local\\Ankama\\Dofus\\data\\common"
      D2I_FILE="C:\\Users\\valen\\AppData\\Local\\Ankama\\Dofus\\data\\i18n\\i18n_fr.d2i"
      DOFUS_INVOKER="C:\\Users\\valen\\AppData\\Local\\Ankama\\Dofus\\DofusInvoker.swf"
      FFDECJAR_PATH="C:\\Program Files (x86)\\FFDec\\ffdec.jar"
      ```
- Launch init.py for
    - Extract DofusInvoker.swf file into action script code
    - Build protocol.pk to get json from network message
    - Create all python class from dofus file with type hint for good autocompetion
    - Unpack d2o and d2i files to translate id to real name
    - Initialize database with d2o and d2i files

- To run test:
    - python -m unittest

# Current state :

Sniffer &#8594; done

We can go to a hdv and launch bot to automatically retreive all prices from hdv and put it in the database.

Currently working for automatically sell all objects in hdv.

# Technology

➡️ 🐍 [Python](#-python)