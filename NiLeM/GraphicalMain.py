#!/usr/bin/python3
from tkinter import *
from tkPDFViewer.tkPDFViewer import *
from . import Settings
from . import Translations
from . import Other
from . import Updating


def info(self):
    self.erase()
    Label(self.root, text=Translations.about(self.language), font=("Lucida Sans", 60),
          bg=self.background_color, fg=self.text_color).pack()
    for i in range(4):
        Label(self.root, text=Translations.about_string(self.language, i),
              bg=self.background_color, fg=self.text_color).pack()
    info_buttons = Frame(self.root, bg=self.background_color)
    manual_button = Button(info_buttons, text=Translations.manual(self.language),
                           command=lambda: self.show_pdf("Manual.pdf"),
                           bg=self.background_color, fg=self.text_color)
    manual_button.grid(row=0, column=0)
    sources_button = Button(info_buttons, text=Translations.sources(self.language),
                            command=lambda: self.show_pdf("Sources.pdf"),
                            bg=self.background_color, fg=self.text_color)
    sources_button.grid(row=0, column=1)
    info_buttons.pack()
    exit_buttons = Frame(self.root, bg=self.background_color)
    turn_off_button = Button(exit_buttons, text=Translations.turn_off(self.language),
                             command=lambda: self.turn_off(),
                             bg=self.background_color, fg=self.text_color)
    turn_off_button.grid(row=0, column=0)
    back_button = Button(exit_buttons, text=Translations.to_main(self.language),
                         command=lambda: self.main_menu(),
                         bg=self.background_color, fg=self.text_color)
    back_button.grid(row=0, column=1)
    exit_buttons.pack()


def main_menu(self):
    self.erase()
    Label(self.root, text=Translations.main(self.language), font=("Lucida Sans", 60),
          bg=self.background_color, fg=self.text_color).pack()
    main_part = Frame(self.root, bg=self.background_color)
    left = Frame(main_part, bg=self.background_color)
    right = Frame(main_part, bg=self.background_color)
    Label(left, text=Translations.settings(self.language), font=("Lucida Sans", 40),
          bg=self.background_color, fg=self.text_color).pack()
    settings_button = Button(
        left, image=self.settings_image, command=lambda: self.settings(),
        bg=self.background_color, fg=self.text_color)
    settings_button.pack()
    Label(left, text=Translations.about(self.language), font=("Lucida Sans", 40),
          bg=self.background_color, fg=self.text_color).pack()
    about_button = Button(left, image=self.about_image, command=lambda: self.info(),
                          bg=self.background_color, fg=self.text_color)
    about_button.pack()
    Label(right, text="NiLeM", font=("Lucida Sans", 40),
          bg=self.background_color, fg=self.text_color).pack()
    nilem_button = Button(right, image=self.subject_images[1],
                          command=lambda: self.nilem_menu(),
                          bg=self.background_color, fg=self.text_color)
    nilem_button.pack()
    Label(right, text="NiLeSh", font=("Lucida Sans", 40),
          bg=self.background_color, fg=self.text_color).pack()
    nilesh_button = Button(right, image=self.subject_images[15],
                           command=lambda: self.nilesh_main(),
                           bg=self.background_color, fg=self.text_color)
    nilesh_button.pack()
    left.grid(row=0, column=0)
    right.grid(row=0, column=1)
    main_part.columnconfigure(0, minsize=350)
    main_part.columnconfigure(1, minsize=350)
    main_part.pack()
    exit_buttons = Frame(self.root, bg=self.background_color)
    turn_off_button = Button(exit_buttons, text=Translations.turn_off(self.language),
                             command=lambda: self.turn_off(),
                             bg=self.background_color, fg=self.text_color)
    turn_off_button.grid(row=0, column=0)
    exit_buttons.pack()


def settings(self):
    self.erase()
    Label(self.root, text="Settings", font=("Lucida Sans", 60),
          bg=self.background_color, fg=self.text_color).pack()
    Label(self.root, text=Translations.languages(self.language), font=("Lucida Sans", 40),
          bg=self.background_color, fg=self.text_color).pack()
    languages = Frame(self.root, bg=self.background_color)
    language_list = ["english", "czech", "russian", "german", "french", "spanish"]
    language_buttons = []
    for i in range(len(language_list)):
        if language_list[i] == self.language:
            language_buttons.append(Button(
                languages, image=self.language_images[i], command=lambda action=language_list[i]:
                self.change_language(action), bg=self.background_color, fg=self.text_color))
        else:
            language_buttons.append(Button(
                languages, image=self.language_bw_images[i], command=lambda action=language_list[i]:
                self.change_language(action), bg=self.background_color, fg=self.text_color))
        language_buttons[i].grid(row=0, column=i)
    languages.pack()
    Label(self.root, text=Translations.mode(self.language), font=("Lucida Sans", 40),
          bg=self.background_color, fg=self.text_color).pack()
    modes = Frame(self.root, bg=self.background_color)
    mode_list = ["dark", "light", "fire", "water", "grass"]
    mode_buttons = []
    for i in range(len(mode_list)):
        mode_buttons.append(Button(
            modes, image=self.mode_images[i], command=lambda action=mode_list[i]:
            self.change_mode(action), bg=self.background_color, fg=self.text_color))
        mode_buttons[i].grid(row=0, column=i)
    modes.pack()
    Label(self.root, text=Translations.update(self.language), font=("Lucida Sans", 40),
          bg=self.background_color, fg=self.text_color).pack()
    updates = Frame(self.root, bg=self.background_color)
    language_update = Frame(updates, bg=self.background_color)
    Label(language_update, text=Translations.languages(self.language), font=("Lucida Sans", 25),
          bg=self.background_color, fg=self.text_color).pack()
    Button(language_update, image=self.language_images[Other.get_language_number(self.language)],
           command=lambda: Updating.update(self.language), bg=self.background_color,
           fg=self.text_color).pack()
    complete_update = Frame(updates, bg=self.background_color)
    Label(complete_update, text=Translations.all_languages(self.language), font=("Lucida Sans", 25),
          bg=self.background_color, fg=self.text_color).pack()
    Button(complete_update, image=self.database_image, command=lambda:
           Updating.complete_update(), bg=self.background_color, fg=self.text_color).pack()
    language_update.grid(row=0, column=0)
    complete_update.grid(row=0, column=1)
    updates.columnconfigure(0, minsize=250)
    updates.columnconfigure(1, minsize=250)
    updates.pack()
    exit_buttons = Frame(self.root, bg=self.background_color)
    turn_off_button = Button(exit_buttons, text=Translations.turn_off(self.language),
                             command=lambda: self.turn_off(),
                             bg=self.background_color, fg=self.text_color)
    turn_off_button.grid(row=0, column=0)
    back_button = Button(exit_buttons, text=Translations.to_main(self.language),
                         command=lambda: self.main_menu(),
                         bg=self.background_color, fg=self.text_color)
    back_button.grid(row=0, column=1)
    exit_buttons.pack()


def change_mode(self, mode):
    if mode != "error":
        Settings.change_setting("mode", mode)
    self.set_mode(mode)
    self.settings()


def set_mode(self, mode):
    if mode == "dark":
        self.root.configure(background="black")
        self.text_color = "#fff"
        self.background_color = "#000"
    elif mode == "light":
        self.root.configure(background="white")
        self.text_color = "#000"
        self.background_color = "#fff"
    elif mode == "fire":
        self.root.configure(background="red")
        self.text_color = "#000"
        self.background_color = "#f00"
    elif mode == "water":
        self.root.configure(background="blue")
        self.text_color = "#000"
        self.background_color = "#00f"
    elif mode == "grass":
        self.root.configure(background="#0f0")
        self.text_color = "#000"
        self.background_color = "#0f0"


def change_language(self, language):
    self.language = language
    Settings.change_setting("language", language)
    self.settings()


def show_pdf(self, name):
    self.erase()
    v1 = ShowPdf()
    v2 = v1.pdf_view(self.root, pdf_location="Info/" + name, width=75, height=100)
    v2.pack()
    exit_buttons = Frame(self.root, bg=self.background_color)
    turn_off_button = Button(exit_buttons, text=Translations.turn_off(self.language),
                             command=lambda: self.turn_off(),
                             bg=self.background_color, fg=self.text_color)
    turn_off_button.grid(row=0, column=0)
    back_button = Button(exit_buttons, text=Translations.to_info(self.language),
                         command=lambda: self.info(),
                         bg=self.background_color, fg=self.text_color)
    back_button.grid(row=1, column=0)
    exit_buttons.place(relx=0.75, rely=0.5)
