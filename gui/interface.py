import tkinter.messagebox
from tkinter import *
from PIL import Image, ImageTk

from static.assets.colors import Colors
from static.assets.fonts import Fonts
from databases.database import Database
from factory import action
from models.item import Item

inserted_item_test = Item()
interface = None


def bot_is_playing_to_false():
    action.bot_is_playing = False


def catch_entries(item_edited) -> bool:
    try:
        item = Item()
        for i, line in enumerate(item_edited):
            if not line[4].get():
                item.runes.append({"value": line[0].get(), "line": line[1].get(), "column": line[2].get()})
    except tkinter.TclError:
        return False
    return True


class Interface:
    TITLE = 'Bot FM'
    BACKGROUND_COLOR = Colors.background_color
    WIDTH_SIZE = 900
    HEIGHT_SIZE = 500
    ICON_MENU_SIZE = 20
    ICON_SIZE = 26

    def __init__(self):
        self.__root = Tk()
        self.__current_page_is_home = False

        self.path_images = "static/assets/icones/"

        self.image_home = self.convert_image_to_interface_image(self.path_images + "home.png")
        self.image_add_item = self.convert_image_to_interface_image(self.path_images + "add.png")
        self.image_start_item = self.convert_image_to_interface_image(self.path_images + "weapon.png")
        self.image_change_item = self.convert_image_to_interface_image(self.path_images + "change.png")
        self.image_delete_item = self.convert_image_to_interface_image(self.path_images + "delete.png")
        self.image_validate = self.convert_image_to_interface_image(self.path_images + "validate.png")
        self.image_cancel = self.convert_image_to_interface_image(self.path_images + "cancel.png")
        self.image_play = self.convert_image_to_interface_image(self.path_images + "play.png")

        self.frame_menu = None
        self.frame_edit = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, value):
        self.__root = value

    @property
    def current_page_is_home(self):
        return self.__current_page_is_home

    @current_page_is_home.setter
    def current_page_is_home(self, value: bool):
        self.__current_page_is_home = value

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            if widget != self.frame_menu:
                widget.destroy()
        self.current_page_is_home = False

    def window(self):
        self.root.title(self.TITLE)
        self.root.iconbitmap(self.path_images + 'logo.ico')
        self.root.config(bg=self.BACKGROUND_COLOR)
        self.root.option_add("*font", Fonts.baseFont)

        height_center = int(self.root.winfo_screenheight() / 2) - int(self.HEIGHT_SIZE / 2)
        width_center = int(self.root.winfo_screenwidth() / 2) - int(self.WIDTH_SIZE / 2)

        self.root.geometry(f"+{width_center}+{height_center}")
        self.root.minsize(self.WIDTH_SIZE, self.HEIGHT_SIZE)
        self.root.maxsize(self.WIDTH_SIZE, height=0)

        self.frame_menu = Frame(self.root)
        self.frame_menu.grid()

        bouton_home = Button(self.frame_menu, image=self.image_home,
                             command=lambda: [self.clear_frame(self.root), self.home()])
        bouton_home.grid()
        bouton_ajout_item = Button(self.frame_menu, image=self.image_add_item,
                                   command=lambda: [self.clear_frame(self.root),
                                                    self.ajout_item_window()])
        bouton_ajout_item.grid(row=1, column=0)

        bouton_bot_working = Button(self.frame_menu, image=self.image_start_item,
                                    command=lambda: [self.clear_frame(self.root),
                                                     self.start_item_window()])
        bouton_bot_working.grid(row=2, column=0)
        self.home()

    def home(self):
        if not self.current_page_is_home:
            frame_home = Frame(self.root, bg=self.BACKGROUND_COLOR)
            frame_home.grid(row=1, column=1)

            self.current_page_is_home = True

    def ajout_item_window(self):
        self.current_page_is_home = False
        frame_ajout_item = Frame(self.root, bg=self.BACKGROUND_COLOR)
        frame_ajout_item.grid(row=1, column=1)
        print(len(inserted_item_test.runes))
        print(inserted_item_test.runes)
        if not inserted_item_test.runes:
            label_text_attente = Label(frame_ajout_item, text="Insérer un Item dans l'atelier de forgemagie",
                                       font=(Fonts.baseFont, 10), width=78, height=20,
                                       bg=Colors.background_color, fg=Colors.foreground_color, relief="ridge")
            label_text_attente.grid(row=0, column=0)
        else:

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

            button_cancel = Button(frame_ajout_item, image=self.image_cancel,
                                   command=lambda: [inserted_item_test.__init__(), self.clear_frame(self.root),
                                                    self.ajout_item_window()])
            button_cancel.grid(row=0, column=4, padx=5)

            item_edited = []

            button_valider = Button(frame_ajout_item, image=self.image_validate,
                                    command=lambda: [
                                        self.on_valid_button_from_inserted_item(item_edited,
                                                                                name_item_variable.get())])
            button_valider.grid(row=0, column=5)

            for i in range(len(inserted_item_test.runes)):
                type_rune = Label(frame_ajout_item, text=inserted_item_test.runes[i].get("type"), width=15,
                                  font=Fonts.baseFont,
                                  bg="green")
                type_rune.grid(column=0, row=i + 2, pady=2, padx=2)

                variable_value_rune = IntVar()
                variable_line_rune = IntVar()
                variable_column_rune = IntVar()

                skip_value = IntVar()

                value_rune = Entry(frame_ajout_item, width=15, font=Fonts.baseFont, textvariable=variable_value_rune)
                value_rune.grid(column=1, row=i + 2, pady=2)
                value_rune.delete(first=0)
                value_rune.insert(0, inserted_item_test.runes[i].get("value"))

                line_rune = Entry(frame_ajout_item, width=15, font=Fonts.baseFont, textvariable=variable_line_rune)
                line_rune.grid(column=2, row=i + 2, pady=2)
                line_rune.delete(first=0)

                column_rune = Entry(frame_ajout_item, width=15, font=Fonts.baseFont, textvariable=variable_column_rune)
                column_rune.grid(column=3, row=i + 2, pady=2)
                column_rune.delete(first=0)

                skip_line_button = Checkbutton(frame_ajout_item,
                                               variable=skip_value, text="Skip", font=Fonts.baseFont,
                                               )
                skip_line_button.grid(column=4, row=i + 2)

                item_edited.append([variable_value_rune, variable_line_rune, variable_column_rune,
                                    inserted_item_test.runes[i].get("type"), skip_value])

    def start_item_window(self):

        self.current_page_is_home = False
        frame_ajout_item = Frame(self.root, bg=self.BACKGROUND_COLOR)
        frame_ajout_item.grid(row=1, column=1)

        items = Database().select_all_name_items()

        for i, item in enumerate(items):
            bouton_item = Button(frame_ajout_item, text=item, font=Fonts.baseFont, width=70)
            bouton_item.grid(row=i + 1, column=0)

            bouton_change_item = Button(frame_ajout_item,
                                        image=self.image_change_item,
                                        command=lambda item=item: [self.clear_frame(self.root),
                                                                   self.edit_item(item)])
            bouton_change_item.grid(row=i + 1, column=2)

            bouton_delete_item = Button(frame_ajout_item,
                                        image=self.image_delete_item,
                                        command=lambda item=item: [Database().delete_target_line_item(item),
                                                                   Database().drop_item_name(item),
                                                                   frame_ajout_item.destroy(),
                                                                   self.start_item_window()])
            bouton_delete_item.grid(row=i + 1, column=1)

            bouton_play_item = Button(frame_ajout_item,
                                      image=self.image_play,
                                      command=lambda item=item: [self.clear_frame(self.root), self.frame_menu.destroy(),
                                                                 self.working_window(item)])
            bouton_play_item.grid(row=i + 1, column=3)

    def edit_item(self, name: str):

        old_name = name
        self.frame_edit = Frame(self.root)
        self.frame_edit.grid(row=1, column=1)

        item = Database().select_item_by_name(name)

        type_rune_title = Label(self.frame_edit, text="Type Rune", width=15, font=Fonts.baseFont,
                                bg=Colors.light_black, fg=Colors.foreground_color)
        type_rune_title.grid(column=0, row=1, pady=2, padx=2)

        value_rune_title = Label(self.frame_edit, text="Valeur Ciblé", width=15,
                                 font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
        value_rune_title.grid(column=1, row=1, pady=2, padx=2)

        line_rune_title = Label(self.frame_edit, text="Ligne Rune", width=15,
                                font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
        line_rune_title.grid(column=2, row=1, pady=2, padx=2)

        column_rune_title = Label(self.frame_edit, text="Colonne Rune", width=15,
                                  font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
        column_rune_title.grid(column=3, row=1, pady=2, padx=2)

        name_item_label = Label(self.frame_edit, text="Nom : ", font=Fonts.baseFont, bg=Colors.light_black,
                                fg=Colors.foreground_color, width=15, height=2)
        name_item_label.grid(column=0, row=0)

        name_item_variable = StringVar()

        name_item = Entry(self.frame_edit, width=25, font=(Fonts.baseFont, 20), textvariable=name_item_variable)
        name_item.grid(column=1, columnspan=3, row=0)
        name_item.insert(0, item.name)

        button_cancel = Button(self.frame_edit, image=self.image_cancel,
                               command=lambda: [self.clear_frame(self.root), self.start_item_window()])
        button_cancel.grid(row=0, column=4, padx=5)

        item_edited = []
        button_valider = Button(self.frame_edit, image=self.image_validate,
                                command=lambda: self.on_valid_button_from_edit_item(item_edited, old_name,
                                                                                    name_item_variable.get())
                                )
        button_valider.grid(row=0, column=5)

        for i, rune in enumerate(item.runes):
            type_rune = Label(self.frame_edit, text=rune.get("type"), width=15, font=Fonts.baseFont,
                              bg="green")
            type_rune.grid(column=0, row=i + 2, pady=2, padx=2)

            variable_value_rune = IntVar()
            variable_line_rune = IntVar()
            variable_column_rune = IntVar()

            skip_value = IntVar()

            value_rune = Entry(self.frame_edit, width=15, font=Fonts.baseFont, textvariable=variable_value_rune)
            value_rune.grid(column=1, row=i + 2, pady=2)
            value_rune.delete(first=0)
            value_rune.insert(0, rune.get("value"))

            line_rune = Entry(self.frame_edit, width=15, font=Fonts.baseFont, textvariable=variable_line_rune)
            line_rune.grid(column=2, row=i + 2, pady=2)
            line_rune.delete(first=0)
            line_rune.insert(0, rune.get("line"))

            column_rune = Entry(self.frame_edit, width=15, font=Fonts.baseFont, textvariable=variable_column_rune)
            column_rune.grid(column=3, row=i + 2, pady=2)
            column_rune.delete(first=0)
            column_rune.insert(0, rune.get("column"))

            skip_line_button = Checkbutton(self.frame_edit,
                                           variable=skip_value, text="Skip", font=Fonts.baseFont,
                                           )
            skip_line_button.grid(column=4, row=i + 2)

            item_edited.append(
                [variable_value_rune, variable_line_rune, variable_column_rune, rune.get("type"), skip_value])

    def on_valid_button_from_edit_item(self, item_edited, old_name, name_item_variable):
        if catch_entries(item_edited):
            Database().delete_target_line_item(old_name),
            Database().drop_item_name(old_name),
            self.get_entries_and_insert_into_database(item_edited,
                                                      name_item_variable),
            self.clear_frame(self.root),
            self.start_item_window()
        else:
            tkinter.messagebox.showwarning("Erreur valeur", "Veuillez remplir tout les champs ou utiliser \"skip\"")

    def on_valid_button_from_inserted_item(self, item_edited, name_item_variable):
        if catch_entries(item_edited):
            self.get_entries_and_insert_into_database(item_edited,
                                                      name_item_variable)
            self.clear_frame(self.root),
            inserted_item_test.__init__(),
            self.ajout_item_window(),
        else:
            tkinter.messagebox.showwarning("Erreur valeur", "Veuillez remplir tout les champs ou utiliser \"skip\"")

    def get_entries_and_insert_into_database(self, item_edited: list, name: str):
        item = Item()
        item.name = name
        base_size = len(item.runes)
        for i, line in enumerate(item_edited):
            if not line[4].get():
                item.runes.append(
                    {"value": line[0].get(), "line": line[1].get(), "column": line[2].get(), "type": line[3]})
            else:
                del item.runes[i - (base_size - len(item.runes))]
        Database().insert_or_update_item(item)

    def convert_image_to_interface_image(self, path: str):
        image = Image.open(path)
        image = image.resize((self.ICON_SIZE, self.ICON_SIZE), Image.ANTIALIAS)

        return ImageTk.PhotoImage(image)

    def working_window(self, name):

        action.bot_is_playing = True

        action.target_item = Database().select_item_by_name(name)

        working_window_frame = Frame(self.root)
        working_window_frame.grid(row=1, column=1)
        stop_button = Button(working_window_frame, bg="red", width=10, height=5, text="STOP",
                             command=lambda: [bot_is_playing_to_false(), self.clear_frame(self.root), self.window()])
        stop_button.grid(row=0, column=4, rowspan=2)

        type_rune_title = Label(working_window_frame, text="Type Rune", width=15, font=Fonts.baseFont,
                                bg=Colors.light_black, fg=Colors.foreground_color)
        type_rune_title.grid(column=0, row=1, pady=2, padx=2)

        value_rune_title = Label(working_window_frame, text="Valeur Ciblé", width=15,
                                 font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
        value_rune_title.grid(column=1, row=1, pady=2, padx=2)

        line_rune_title = Label(working_window_frame, text="Ligne Rune", width=15,
                                font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
        line_rune_title.grid(column=2, row=1, pady=2, padx=2)

        column_rune_title = Label(working_window_frame, text="Colonne Rune", width=15,
                                  font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
        column_rune_title.grid(column=3, row=1, pady=2, padx=2)

        name_item_label = Label(working_window_frame, text=f"Nom : {action.target_item.name}", font=Fonts.baseFont,
                                bg=Colors.light_black,
                                fg=Colors.foreground_color, height=3, width=65)
        name_item_label.grid(column=0, row=0, columnspan=4)

        for i, rune in enumerate(action.target_item.runes):
            label_type = Label(working_window_frame, text=rune.get("type"))
            label_type.grid(column=0, row=i + 2)

            label_value = Label(working_window_frame, text=rune.get("value"))
            label_value.grid(column=1, row=i + 2)

            label_line = Label(working_window_frame, text=rune.get("line"))
            label_line.grid(column=2, row=i + 2)

            label_column = Label(working_window_frame, text=rune.get("column"))
            label_column.grid(column=3, row=i + 2)
