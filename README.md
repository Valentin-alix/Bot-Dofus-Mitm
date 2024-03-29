# En cours de développement

# Setup :

- Install Jpexs-decompiler to decompil DofusInvoker.swf : https://github.com/jindrapetrik/jpexs-decompiler
- Create .env file
  - example of .env :
  ```
  D2O_FOLDER="C:\\Users\\valen\\AppData\\Local\\Ankama\\Dofus\\data\\common"
  D2P_FOLDER="C:\\Users\\valen\\AppData\\Local\\Ankama\\Dofus\\content\\gfx\\items"
  D2P_FOLDER2="C:\\Users\\valen\\AppData\\Local\\Ankama\\Dofus\\content\\gfx\\sprites"
  D2I_FILE="C:\\Users\\valen\\AppData\\Local\\Ankama\\Dofus\\data\\i18n\\i18n_fr.d2i"
  DOFUS_INVOKER="C:\\Users\\valen\\AppData\\Local\\Ankama\\Dofus\\DofusInvoker.swf"
  FFDECJAR_PATH="C:\\Program Files (x86)\\FFDec\\ffdec.jar"
  ```
- Launch init.bat to setup environment and
  - Extract DofusInvoker.swf file into action script code
  - Build protocol.pk to get json from network message
  - Create all python class from dofus file with type hint for good autocompletion
  - Unpack d2o and d2i files to translate id to real name
  - Initialize database with d2o and d2i files

# Current state :

- Sniffer

- Scrapping sale hotel

  - Chart on prices by item FIXME Need to remove values when equal to zero
  - Top 10 of best benefits item in nuggets
  - Top 10 of most important price drop
  - Find best benefits from crafting

- Automate sells resource in hdv
  - Automatic sells of objects(resources/consumable) in sale hotel
  - Automatic update of price objects (resources/consumable) in sale hotel

# Technologies :

➡️ 🐍 Python

- SQLAlchemy
- PyQt5

## Bot hdv scrapping :

![scrapping bot](./resources/scrapping_bot.png)

### Benefit from craft :

![craft bot](./resources/benefit_craft.png)

## Bot hdv selling :

![selling bot](./resources/selling_bot.gif)

## Sniffer :

![sniffer](./resources/sniffer.png)
