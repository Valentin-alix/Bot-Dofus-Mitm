# Setup :

- Désactiver l'ipv6 sur votre PC

- Installer Jpexs-decompiler : https://github.com/jindrapetrik/jpexs-decompiler
- Créer un fichier .env dans app/.env , vous pouvez prendre exemple sur le fichier app/.env.template :
  ```
  D2O_FOLDER="C:\\Users\\valen\\AppData\\Local\\Ankama\\Dofus\\data\\common"
  D2P_FOLDER="C:\\Users\\valen\\AppData\\Local\\Ankama\\Dofus\\content\\gfx\\items"
  D2P_FOLDER2="C:\\Users\\valen\\AppData\\Local\\Ankama\\Dofus\\content\\gfx\\sprites"
  D2I_FILE="C:\\Users\\valen\\AppData\\Local\\Ankama\\Dofus\\data\\i18n\\i18n_fr.d2i"
  DOFUS_INVOKER="C:\\Users\\valen\\AppData\\Local\\Ankama\\Dofus\\DofusInvoker.swf"
  FFDECJAR_PATH="C:\\Program Files (x86)\\FFDec\\ffdec.jar"
  ```

`init.bat` # Initialise le bot (c'est à faire à chaque nouvelle maj)

Vous ne devez avoir qu'une seule instance du jeu ouvert.

`start.bat` # Lance le bot

Vous n'avez plus qu'à connecter votre personnage (vous devez déco/reco si votre personnage est déjà connecté).

Il peut arriver que la connexion se passe mal et que la console affiche un caractère bizzard de ce style : ▲M
Si c'est le cas c'est probablement à cause de la latence, rééssayer et ça devrait passer.

# Fonctionnalités :

Toutes les données sont stockés en local dans un fichier sqlite, pour enregistrer les prix vous devez aller à un hdv et lancer le bot depuis la page scrapping avec le bouton play, il ne vous reste plus qu'a attendre la fin.

- Sniffer

- Scrapping de l'hdv

  - Graphique du prix des items au fil du temps
  - Top 10 des meilleurs bénéfices au recyclage des pépites
  - Top 10 des chutes les plus importantes de prix

- Automatisation de la vente d'objets en hdv
  - Vente automatique des objets(ressources/consommables/cosmétiques) en hdv (il faut être dans l'onglet vente de l'hdv correspondant)
  - Modification automatique des prix des objets (ressources/consommables/cosmétiques) en hdv (il faut être dans l'onglet vente de l'hdv correspondant)

# Technologies :

➡️ 🐍 Python

- SQLAlchemy
- PyQt5

## Interface d'évolution des prix :

![scrapping bot](./docs/screenshots/evolution_price.png)

## Interface des chutes de prix / bénéfices du recyclage :

![scrapping bot](./docs/screenshots/price_drop_recycling.png)

## Interface des bénéfices par craft :

![scaping craft](./docs/screenshots/benefit_craft.png)

## Automatisation de la vente :

![selling bot](./docs/screenshots/selling_bot.gif)

## Interface du sniffer :

![sniffer](./docs/screenshots/sniffer_interface.png)
