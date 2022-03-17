from tkinter import *

from PIL import Image, ImageTk

from assets.colors import Colors
from assets.fonts import Fonts
from databases.database_management import DatabaseManagement

inserted_item = []
interface = None


def reset_inserted_item():
    inserted_item.clear()


class Interface:
    def __init__(self):
        self.__root = Tk()
        self.__title = 'Bot FM'
        self.__backgroundColor = Colors.background_color
        self.__currentPageIsHome = False
        self.__widthSize = 800
        self.__heightSize = 500
        self.__icon_menu_size = 20
        self.__icon_size = 26
        self.__database = DatabaseManagement()
        self.image_home = None
        self.image_ajout_item = None
        self.image_start_item = None
        self.image_change_item = None
        self.image_delete_item = None
        self.image_valider = None
        self.image_cancel = None
        self.frame_menu = None

    @property
    def root(self):
        return self.__root

    @property
    def icon_size(self):
        return self.__icon_size

    @property
    def heightSize(self):
        return self.__heightSize

    @property
    def title(self):
        return self.__title

    @property
    def backgroundColor(self):
        return self.__backgroundColor

    @property
    def currentPageIsHome(self):
        return self.__currentPageIsHome

    @property
    def widthSize(self):
        return self.__widthSize

    @property
    def database(self):
        return self.__database

    @currentPageIsHome.setter
    def currentPageIsHome(self, value: bool):
        self.__currentPageIsHome = value

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            if widget != self.frame_menu:
                widget.destroy()
        self.currentPageIsHome = False

    def window(self):

        self.root.title(self.title)
        self.root.iconbitmap('./assets/icones/icone.ico')
        self.root.config(bg=self.backgroundColor)
        self.root.option_add("*font", Fonts.baseFont)

        height_center = int(self.root.winfo_screenheight() / 2) - int(self.heightSize / 2)
        width_center = int(self.root.winfo_screenwidth() / 2) - int(self.widthSize / 2)

        self.root.geometry("+{}+{}".format(width_center, height_center))
        self.root.minsize(self.widthSize, self.heightSize)
        self.root.maxsize(self.widthSize, height=0)

        self.frame_menu = Frame(self.root)
        self.frame_menu.grid()

        self.image_home = Image.open("./assets/icones/home.png")
        self.image_home = self.image_home.resize((self.icon_size, self.icon_size), Image.ANTIALIAS)
        self.image_home = ImageTk.PhotoImage(self.image_home)

        self.image_ajout_item = Image.open("./assets/icones/add.png")
        self.image_ajout_item = self.image_ajout_item.resize((self.icon_size, self.icon_size), Image.ANTIALIAS)
        self.image_ajout_item = ImageTk.PhotoImage(self.image_ajout_item)

        self.image_start_item = Image.open("./assets/icones/arme.png")
        self.image_start_item = self.image_start_item.resize((self.icon_size, self.icon_size), Image.ANTIALIAS)
        self.image_start_item = ImageTk.PhotoImage(self.image_start_item)

        bouton_home = Button(self.frame_menu, image=self.image_home,
                             command=lambda: [self.clear_frame(self.root), self.home()])
        bouton_home.grid()
        bouton_ajout_item = Button(self.frame_menu, image=self.image_ajout_item,
                                   command=lambda: [self.clear_frame(self.root),
                                                    self.ajout_item_window()])
        bouton_ajout_item.grid(row=1, column=0)

        bouton_bot_working = Button(self.frame_menu, image=self.image_start_item,
                                    command=lambda: [self.clear_frame(self.root),
                                                     self.start_item_window()])
        bouton_bot_working.grid(row=2, column=0)
        self.home()

    def home(self):
        if not self.currentPageIsHome:
            frame_home = Frame(self.root, bg=self.backgroundColor)
            frame_home.grid(row=1, column=1)

            self.currentPageIsHome = True

    def ajout_item_window(self):
        self.currentPageIsHome = False
        frame_ajout_item = Frame(self.root, bg=self.backgroundColor)
        frame_ajout_item.grid(row=1, column=1)
        if not inserted_item:
            label_text_attente = Label(frame_ajout_item, text="Insérer un Item dans l'atelier de forgemagie",
                                       font=(Fonts.baseFont, 10), width=78, height=20,
                                       bg=Colors.background_color, fg=Colors.foreground_color, relief="ridge")
            label_text_attente.grid(row=0, column=0)
        else:

            types_runes = self.database.select_types_rune_by_runes_id(inserted_item[0])

            type_rune_title = Label(frame_ajout_item, text="Type Rune", width=15, font=Fonts.baseFont,
                                    bg=Colors.light_black, fg=Colors.foreground_color)
            type_rune_title.grid(column=0, row=1, pady=2, padx=2)

            value_rune_title = Label(frame_ajout_item, text="Valeur Ciblé", width=15,
                                     font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
            value_rune_title.grid(column=1, row=1, pady=2, padx=2)

            line_rune_title = Label(frame_ajout_item, text="Ligne Rune", width=15,
                                    font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
            line_rune_title.grid(column=2, row=1, pady=2, padx=2)

            column_rune_title = Label(frame_ajout_item, text="Colonne Rune", width=15,
                                      font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
            column_rune_title.grid(column=3, row=1, pady=2, padx=2)

            name_item_label = Label(frame_ajout_item, text="Nom : ", font=Fonts.baseFont, bg=Colors.light_black,
                                    fg=Colors.foreground_color, width=15, height=2)
            name_item_label.grid(column=0, row=0)

            name_item_variable = StringVar()

            name_item = Entry(frame_ajout_item, width=25, font=(Fonts.baseFont, 20), textvariable=name_item_variable)
            name_item.grid(column=1, columnspan=3, row=0)

            image_cancel_item = Image.open("./assets/icones/cancel.png")
            image_cancel_item = image_cancel_item.resize((self.icon_size, self.icon_size), Image.ANTIALIAS)
            self.image_cancel = ImageTk.PhotoImage(image_cancel_item)

            button_cancel = Button(frame_ajout_item, image=self.image_cancel,
                                   command=lambda: [reset_inserted_item(), self.clear_frame(self.root),
                                                    self.ajout_item_window()])
            button_cancel.grid(row=0, column=4, padx=5)

            image_valider_item = Image.open("./assets/icones/valider.png")
            image_valider_item = image_valider_item.resize((self.icon_size, self.icon_size), Image.ANTIALIAS)
            self.image_valider = ImageTk.PhotoImage(image_valider_item)

            item_edited = []

            button_valider = Button(frame_ajout_item, image=self.image_valider,
                                    command=lambda: [
                                        self.get_entry_and_insert_into_database(name_item_variable.get(), item_edited,
                                                                                types_runes),
                                        reset_inserted_item(),
                                        self.clear_frame(self.root),
                                        self.ajout_item_window()])
            button_valider.grid(row=0, column=5)

            # FIXME FAIRE TRUC INT VAR POUR RECUP VALUE
            for i in range(len(types_runes)):
                type_rune = Label(frame_ajout_item, text=types_runes[i], width=15, font=Fonts.baseFont,
                                  bg="green")
                type_rune.grid(column=0, row=i + 2, pady=2, padx=2)

                variable_value_rune = IntVar()
                variable_line_rune = IntVar()
                variable_column_rune = IntVar()

                value_rune = Entry(frame_ajout_item, width=15, font=Fonts.baseFont, textvariable=variable_value_rune)
                value_rune.grid(column=1, row=i + 2, pady=2)
                value_rune.delete(first=0)
                value_rune.insert(0, inserted_item[1][i])

                line_rune = Entry(frame_ajout_item, width=15, font=Fonts.baseFont, textvariable=variable_line_rune)
                line_rune.grid(column=2, row=i + 2, pady=2)
                line_rune.delete(first=0)

                column_rune = Entry(frame_ajout_item, width=15, font=Fonts.baseFont, textvariable=variable_column_rune)
                column_rune.grid(column=3, row=i + 2, pady=2)
                column_rune.delete(first=0)

                skip_line_button = Checkbutton(frame_ajout_item, text="Skip", font=Fonts.baseFont)
                skip_line_button.grid(column=4, row=i + 2)

                item_edited.append([variable_value_rune, variable_line_rune, variable_column_rune])

    def start_item_window(self):

        self.currentPageIsHome = False
        frame_ajout_item = Frame(self.root, bg=self.backgroundColor)
        frame_ajout_item.grid(row=1, column=1)
        image_change_item = Image.open("./assets/icones/modifier.png")
        image_change_item = image_change_item.resize((self.icon_size, self.icon_size), Image.ANTIALIAS)
        self.image_change_item = ImageTk.PhotoImage(image_change_item)

        image_delete_item = Image.open("./assets/icones/supprimer.png")
        image_delete_item = image_delete_item.resize((self.icon_size, self.icon_size), Image.ANTIALIAS)
        self.image_delete_item = ImageTk.PhotoImage(image_delete_item)

        items = self.database.select_all_items()
        for i in range(len(items)):
            bouton_item = Button(frame_ajout_item, text=items[i], font=Fonts.baseFont, width=70)
            bouton_item.grid(row=i + 1, column=0)

            bouton_change_item = Button(frame_ajout_item,
                                        image=self.image_change_item)
            bouton_change_item.grid(row=i + 1, column=1)

            bouton_delete_item = Button(frame_ajout_item,
                                        image=self.image_delete_item,
                                        command=lambda: [self.database.drop_target_lines_item(items[i]),
                                                         self.database.drop_item(items[i]),
                                                         frame_ajout_item.destroy(), self.start_item_window()])
            bouton_delete_item.grid(row=i + 1, column=2)

    def get_entry_and_insert_into_database(self, name: str, item_edited: list, types_runes: list) -> list:
        values_runes = []
        lines_runes = []
        columns_runes = []
        for i in range(len(item_edited)):
            values_runes.append(item_edited[i][0].get())
            lines_runes.append(item_edited[i][1].get())
            columns_runes.append(item_edited[i][2].get())

        self.database.insert_or_update_target_lines_item(name, types_runes, values_runes, lines_runes, columns_runes)
