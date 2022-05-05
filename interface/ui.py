import asyncio
import tkinter
from asyncio import Queue, Event
import tkinter as tk
from tkinter import messagebox

from PIL import ImageTk, Image

from databases.database import Database
from models.item import Item
from static import constant
from static.assets.colors import Colors
from static.assets.fonts import Fonts


class Ui(tk.Tk):
    def __init__(self, queue_target_item: Queue, queue_inserted_item: Queue, queue_actual_item: Queue,
                 event_is_playing: Event) -> None:
        super().__init__()
        self.queue_target_item: Queue = queue_target_item
        self.queue_inserted_item: Queue = queue_inserted_item
        self.queue_actual_item: Queue = queue_actual_item
        self.event_is_playing: Event = event_is_playing
        self.frame_menu: tk.Frame = None
        self.frame_edit: tk.Frame = None
        self.page: str = ""
        self.interval = 1 / 20
        self.inserted_item: Item = Item()
        self.path_images: str = "static/assets/icones/"
        self.image_home: ImageTk = self.convert_image_to_interface_image(self.path_images + "home.png")
        self.image_add_item: ImageTk = self.convert_image_to_interface_image(self.path_images + "add.png")
        self.image_start_item: ImageTk = self.convert_image_to_interface_image(self.path_images + "weapon.png")
        self.image_change_item: ImageTk = self.convert_image_to_interface_image(self.path_images + "change.png")
        self.image_delete_item: ImageTk = self.convert_image_to_interface_image(self.path_images + "delete.png")
        self.image_validate: ImageTk = self.convert_image_to_interface_image(self.path_images + "validate.png")
        self.image_cancel: ImageTk = self.convert_image_to_interface_image(self.path_images + "cancel.png")
        self.image_play: ImageTk = self.convert_image_to_interface_image(self.path_images + "play.png")
        self.image_graphic: ImageTk = ImageTk.PhotoImage(Image.open("static/assets/images/cost_rune_graph.png"))
        self.database: Database = Database()

    async def window(self) -> None:
        self.title(constant.TITLE)
        self.iconbitmap("static/assets/icones/logo.ico")
        self.config(bg=constant.BACKGROUND_COLOR)
        self.option_add("*font", Fonts.baseFont)

        height_center = int(self.winfo_screenheight() / 2) - int(constant.HEIGHT_SIZE / 2)
        width_center = int(self.winfo_screenwidth() / 2) - int(constant.WIDTH_SIZE / 2)

        self.geometry(f"+{width_center}+{height_center}")
        self.minsize(constant.WIDTH_SIZE, constant.HEIGHT_SIZE)
        self.maxsize(constant.WIDTH_SIZE, height=0)

        self.menu()
        self.home_page()

    async def updater(self):
        while True:
            self.update()
            await asyncio.sleep(self.interval)

    def menu(self) -> None:
        self.frame_menu = tk.Frame(self)
        bouton_home = tk.Button(self.frame_menu, image=self.image_home,
                                command=lambda: [self.home_page()])
        bouton_home.grid()

        bouton_ajout_item = tk.Button(self.frame_menu, image=self.image_add_item,
                                      command=lambda: asyncio.ensure_future(self.ajout_item_page()))
        bouton_ajout_item.grid(row=1, column=0)

        bouton_bot_working = tk.Button(self.frame_menu, image=self.image_start_item,
                                       command=lambda: [self.start_item_page()])
        bouton_bot_working.grid(row=2, column=0)
        self.frame_menu.grid(row=0, column=0)

    def home_page(self) -> None:
        if self.page != "Home":
            self.clear_frame(self)
            frame_home = tk.Frame(self, bg=constant.BACKGROUND_COLOR)
            frame_home.grid(row=1, column=1)
            self.page = "Home"
            label_image = tk.Label(frame_home, image=self.image_graphic)
            label_image.pack()

    async def check_inserted_item(self) -> None:
        while True:
            self.inserted_item = await self.queue_inserted_item.get()
            self.clear_frame(self)
            await self.ajout_item_page()

    async def ajout_item_page(self) -> None:
        if self.page != "Ajout Item":
            self.clear_frame(self)
            self.page = "Ajout Item"
            frame_ajout_item = tk.Frame(self, bg=constant.BACKGROUND_COLOR)
            frame_ajout_item.grid(row=1, column=1)
            label_text_attente = tk.Label(frame_ajout_item, text="Insérer un Item dans l'atelier de forgemagie",
                                          font=(Fonts.baseFont, 10), width=104, height=35,
                                          bg=Colors.background_color, fg=Colors.foreground_color, relief="ridge")
            label_text_attente.grid(row=0, column=0)
            if len(self.inserted_item.runes) != 0:
                label_text_attente.destroy()
                type_rune_title = tk.Label(frame_ajout_item, text="Type Rune", width=15, font=Fonts.baseFont,
                                           bg=Colors.light_black, fg=Colors.foreground_color)
                type_rune_title.grid(column=0, row=1, pady=2, padx=2)

                value_rune_title = tk.Label(frame_ajout_item, text="Valeur Ciblé", width=15,
                                            font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
                value_rune_title.grid(column=1, row=1, pady=2, padx=2)

                line_rune_title = tk.Label(frame_ajout_item, text="Ligne Rune", width=15,
                                           font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
                line_rune_title.grid(column=2, row=1, pady=2, padx=2)

                column_rune_title = tk.Label(frame_ajout_item, text="Colonne Rune", width=15,
                                             font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
                column_rune_title.grid(column=3, row=1, pady=2, padx=2)

                name_item_label = tk.Label(frame_ajout_item, text="Nom : ", font=Fonts.baseFont, bg=Colors.light_black,
                                           fg=Colors.foreground_color, width=15, height=2)
                name_item_label.grid(column=0, row=0)

                name_item_variable = tk.StringVar()

                name_item = tk.Entry(frame_ajout_item, width=25, font=(Fonts.baseFont, 20),
                                     textvariable=name_item_variable)
                name_item.grid(column=1, columnspan=3, row=0)

                button_cancel = tk.Button(frame_ajout_item, image=self.image_cancel,
                                          command=lambda: [self.inserted_item.__init__(), self.clear_frame(self),
                                                           asyncio.ensure_future(self.ajout_item_page())])
                button_cancel.grid(row=0, column=4, padx=5)

                item_edited = []

                button_valider = tk.Button(frame_ajout_item, image=self.image_validate,
                                           command=lambda: [
                                               self.add_or_update_item(item_edited, name_item_variable.get()),
                                               self.inserted_item.__init__(), self.clear_frame(self),
                                               asyncio.ensure_future(self.ajout_item_page())])
                button_valider.grid(row=0, column=5)

                for i in range(len(self.inserted_item.runes)):
                    type_rune = tk.Label(frame_ajout_item, text=self.inserted_item.runes[i].get("type"), width=15,
                                         font=Fonts.baseFont,
                                         bg="green")
                    type_rune.grid(column=0, row=i + 2, pady=2, padx=2)

                    variable_value_rune = tk.IntVar()
                    variable_line_rune = tk.IntVar()
                    variable_column_rune = tk.IntVar()

                    skip_value = tk.IntVar()

                    value_rune = tk.Entry(frame_ajout_item, width=15, font=Fonts.baseFont,
                                          textvariable=variable_value_rune)
                    value_rune.grid(column=1, row=i + 2, pady=2)
                    value_rune.delete(first=0)
                    value_rune.insert(0, self.inserted_item.runes[i].get("value"))

                    line_rune = tk.Entry(frame_ajout_item, width=15, font=Fonts.baseFont,
                                         textvariable=variable_line_rune)
                    line_rune.grid(column=2, row=i + 2, pady=2)
                    line_rune.delete(first=0)

                    column_rune = tk.Entry(frame_ajout_item, width=15, font=Fonts.baseFont,
                                           textvariable=variable_column_rune)
                    column_rune.grid(column=3, row=i + 2, pady=2)
                    column_rune.delete(first=0)

                    skip_line_button = tk.Checkbutton(frame_ajout_item,
                                                      variable=skip_value, text="Skip", font=Fonts.baseFont,
                                                      )
                    skip_line_button.grid(column=4, row=i + 2)

                    item_edited.append([variable_value_rune, variable_line_rune, variable_column_rune,
                                        self.inserted_item.runes[i].get("type"), skip_value])

    def start_item_page(self) -> None:
        if self.page != "Start Item":
            self.clear_frame(self)
            frame_ajout_item = tk.Frame(self, bg=constant.BACKGROUND_COLOR)
            frame_ajout_item.grid(row=1, column=1)

            items = self.database.select_all_name_items()

            for i, item in enumerate(items):
                bouton_item = tk.Button(frame_ajout_item, text=item, font=Fonts.baseFont, width=88)
                bouton_item.grid(row=i + 1, column=0)
                if self.database.select_price_item_per_tenta(item) >= 100000:
                    color: str = 'red'
                elif self.database.select_price_item_per_tenta(item) >= 50000:
                    color: str = 'orange'
                else:
                    color: str = 'green'
                label_average_price = tk.Button(frame_ajout_item, bg=color,
                                                text=self.database.select_price_item_per_tenta(item),
                                                width=15
                                                )
                label_average_price.grid(row=i + 1, column=1)

                bouton_change_item = tk.Button(frame_ajout_item,
                                               image=self.image_change_item,
                                               command=lambda item=item: [
                                                   self.edit_item_page(item)])
                bouton_change_item.grid(row=i + 1, column=3)

                bouton_delete_item = tk.Button(frame_ajout_item,
                                               image=self.image_delete_item,
                                               command=lambda item=item: [self.database.delete_target_line_item(item),
                                                                          self.database.drop_item_name(item),
                                                                          self.clear_frame(self),
                                                                          self.start_item_page()])
                bouton_delete_item.grid(row=i + 1, column=2)

                bouton_play_item = tk.Button(frame_ajout_item,
                                             image=self.image_play,
                                             command=lambda item=item: [
                                                 self.frame_menu.destroy(),
                                                 asyncio.ensure_future(self.working_page(item))])
                bouton_play_item.grid(row=i + 1, column=4)
            self.page = "Start Item"

    async def working_page(self, name: str) -> None:
        if self.page != "Working":
            self.clear_frame(self)
            self.event_is_playing.set()
            target_item = self.database.select_item_by_name(name)
            await self.queue_target_item.put(target_item)

            working_window_frame = tk.Frame(self)
            working_window_frame.grid(row=1, column=1)
            stop_button = tk.Button(working_window_frame, bg="red", width=10, height=5, text="STOP",
                                    command=lambda: [asyncio.ensure_future(self.stop_bot()), self.menu(),
                                                     self.start_item_page()])
            stop_button.grid(row=0, column=4, rowspan=2)

            type_rune_title = tk.Label(working_window_frame, text="Type Rune", width=15, font=Fonts.baseFont,
                                       bg=Colors.light_black, fg=Colors.foreground_color)
            type_rune_title.grid(column=0, row=1, pady=2, padx=2)

            value_rune_title = tk.Label(working_window_frame, text="Valeur Ciblé", width=15,
                                        font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
            value_rune_title.grid(column=1, row=1, pady=2, padx=2)

            line_rune_title = tk.Label(working_window_frame, text="Ligne Rune", width=15,
                                       font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
            line_rune_title.grid(column=2, row=1, pady=2, padx=2)

            column_rune_title = tk.Label(working_window_frame, text="Colonne Rune", width=15,
                                         font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
            column_rune_title.grid(column=3, row=1, pady=2, padx=2)

            name_item_label = tk.Label(working_window_frame, text=f"Nom : {target_item.name}",
                                       font=Fonts.baseFont,
                                       bg=Colors.light_black,
                                       fg=Colors.foreground_color, height=3, width=65)
            name_item_label.grid(column=0, row=0, columnspan=4)

            for i, rune in enumerate(target_item.runes):
                label_type = tk.Label(working_window_frame, text=rune.get("type"))
                label_type.grid(column=0, row=i + 2)

                label_value = tk.Label(working_window_frame, text=rune.get("value"))
                label_value.grid(column=1, row=i + 2)

                label_line = tk.Label(working_window_frame, text=rune.get("line"))
                label_line.grid(column=2, row=i + 2)

                label_column = tk.Label(working_window_frame, text=rune.get("column"))
                label_column.grid(column=3, row=i + 2)
            self.page = "Working"

    def edit_item_page(self, name: str) -> None:
        if self.page != "Edit Item":
            self.clear_frame(self)
            old_name = name
            self.frame_edit = tk.Frame(self)
            self.frame_edit.grid(row=1, column=1)

            item = self.database.select_item_by_name(name)

            type_rune_title = tk.Label(self.frame_edit, text="Type Rune", width=15, font=Fonts.baseFont,
                                       bg=Colors.light_black, fg=Colors.foreground_color)
            type_rune_title.grid(column=0, row=1, pady=2, padx=2)

            value_rune_title = tk.Label(self.frame_edit, text="Valeur Ciblé", width=15,
                                        font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
            value_rune_title.grid(column=1, row=1, pady=2, padx=2)

            line_rune_title = tk.Label(self.frame_edit, text="Ligne Rune", width=15,
                                       font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
            line_rune_title.grid(column=2, row=1, pady=2, padx=2)

            column_rune_title = tk.Label(self.frame_edit, text="Colonne Rune", width=15,
                                         font=Fonts.baseFont, bg=Colors.light_black, fg=Colors.foreground_color)
            column_rune_title.grid(column=3, row=1, pady=2, padx=2)

            name_item_label = tk.Label(self.frame_edit, text="Nom : ", font=Fonts.baseFont, bg=Colors.light_black,
                                       fg=Colors.foreground_color, width=15, height=2)
            name_item_label.grid(column=0, row=0)

            name_item_variable = tk.StringVar()

            name_item = tk.Entry(self.frame_edit, width=25, font=(Fonts.baseFont, 20), textvariable=name_item_variable)
            name_item.grid(column=1, columnspan=3, row=0)
            name_item.insert(0, item.name)

            button_cancel = tk.Button(self.frame_edit, image=self.image_cancel,
                                      command=lambda: [self.clear_frame(self), self.start_item_page()])
            button_cancel.grid(row=0, column=4, padx=5)

            item_edited = []
            button_valider = tk.Button(self.frame_edit, image=self.image_validate,
                                       command=lambda: [
                                           self.add_or_update_item(item_edited, name_item_variable.get(), old_name),
                                           self.clear_frame(self), self.start_item_page()]
                                       )
            button_valider.grid(row=0, column=5)

            for i, rune in enumerate(item.runes):
                type_rune = tk.Label(self.frame_edit, text=rune.get("type"), width=15, font=Fonts.baseFont,
                                     bg="green")
                type_rune.grid(column=0, row=i + 2, pady=2, padx=2)

                variable_value_rune = tk.IntVar()
                variable_line_rune = tk.IntVar()
                variable_column_rune = tk.IntVar()

                skip_value = tk.IntVar()

                value_rune = tk.Entry(self.frame_edit, width=15, font=Fonts.baseFont, textvariable=variable_value_rune)
                value_rune.grid(column=1, row=i + 2, pady=2)
                value_rune.delete(first=0)
                value_rune.insert(0, rune.get("value"))

                line_rune = tk.Entry(self.frame_edit, width=15, font=Fonts.baseFont, textvariable=variable_line_rune)
                line_rune.grid(column=2, row=i + 2, pady=2)
                line_rune.delete(first=0)
                line_rune.insert(0, rune.get("line"))

                column_rune = tk.Entry(self.frame_edit, width=15, font=Fonts.baseFont,
                                       textvariable=variable_column_rune)
                column_rune.grid(column=3, row=i + 2, pady=2)
                column_rune.delete(first=0)
                column_rune.insert(0, rune.get("column"))

                skip_line_button = tk.Checkbutton(self.frame_edit,
                                                  variable=skip_value, text="Skip", font=Fonts.baseFont,
                                                  )
                skip_line_button.grid(column=4, row=i + 2)

                item_edited.append(
                    [variable_value_rune, variable_line_rune, variable_column_rune, rune.get("type"), skip_value])
            self.page = "Edit Item"

    def clear_frame(self, frame) -> None:
        for widget in frame.winfo_children():
            if widget != self.frame_menu:
                widget.destroy()
        self.page = ""

    @staticmethod
    def convert_image_to_interface_image(path: str) -> ImageTk:
        image = Image.open(path)
        image = image.resize((constant.ICON_SIZE, constant.ICON_SIZE), Image.ANTIALIAS)

        return ImageTk.PhotoImage(image)

    def add_or_update_item(self, item_edited: list, name: str, old_name: str = "") -> None:
        try:
            self.database.delete_target_line_item(old_name),
            self.database.drop_item_name(old_name),
            item = Item()
            item.name = name
            for i, line in enumerate(item_edited):
                if not line[4].get():
                    item.runes.append(
                        {"value": line[0].get(), "line": line[1].get(), "column": line[2].get(), "type": line[3]})
            self.database.insert_or_update_item(item)
        except tkinter.TclError:
            messagebox.showwarning("Erreur valeur", "Veuillez remplir tout les champs ou utiliser \"skip\"")

    async def stop_bot(self) -> None:
        self.queue_actual_item = None
        self.queue_target_item = None
        self.event_is_playing.clear()
