#!/usr/bin/python3


def subject_name(subject, language):
    if language == "english":
        return subject.capitalize()
    elif language == "czech":
        if subject == "math":
            return "Matematika"
        elif subject == "physics":
            return "Fyzika"
        elif subject == "chemistry":
            return "Chemie"
        elif subject == "biology":
            return "Biologie"
        elif subject == "geography":
            return "Zeměpis"
        elif subject == "history":
            return "Dějepis"
        elif subject == "english":
            return "Angličtina"
        elif subject == "german":
            return "Němčina"
        elif subject == "czech":
            return "Čeština"
        elif subject == "russian":
            return "Ruština"
        elif subject == "french":
            return "Francouzština"
        elif subject == "spanish":
            return "Španělština"
        elif subject == "literature":
            return "Literatura"
        elif subject == "music":
            return "Hudba"
        elif subject == "art":
            return "Umění"
        elif subject == "informatics":
            return "Informatika"
    elif language == "russian":
        if subject == "math":
            return "Математика"
        elif subject == "physics":
            return "Физика"
        elif subject == "chemistry":
            return "Химия"
        elif subject == "biology":
            return "Биология"
        elif subject == "geography":
            return "География"
        elif subject == "history":
            return "История"
        elif subject == "english":
            return "Английский"
        elif subject == "german":
            return "Немецкий"
        elif subject == "czech":
            return "Чешский"
        elif subject == "russian":
            return "Русский"
        elif subject == "french":
            return "Французский"
        elif subject == "spanish":
            return "Испанский"
        elif subject == "literature":
            return "Литература"
        elif subject == "music":
            return "Музыка"
        elif subject == "art":
            return "Искусство"
        elif subject == "informatics":
            return "Информатика"
    elif language == "german":
        if subject == "math":
            return "Mathe"
        elif subject == "physics":
            return "Physik"
        elif subject == "chemistry":
            return "Chemie"
        elif subject == "biology":
            return "Biologie"
        elif subject == "geography":
            return "Geografie"
        elif subject == "history":
            return "Geschichte"
        elif subject == "english":
            return "Englisch"
        elif subject == "german":
            return "Deutsch"
        elif subject == "czech":
            return "Tschechisch"
        elif subject == "russian":
            return "Russisch"
        elif subject == "french":
            return "Französisch"
        elif subject == "spanish":
            return "Spanisch"
        elif subject == "literature":
            return "Literatur"
        elif subject == "music":
            return "Musik"
        elif subject == "art":
            return "Kunst"
        elif subject == "informatics":
            return "Informatik"
    elif language == "french":
        if subject == "math":
            return "Mathématiques"
        elif subject == "physics":
            return "Physique"
        elif subject == "chemistry":
            return "Chimie"
        elif subject == "biology":
            return "Biologie"
        elif subject == "geography":
            return "Géographie"
        elif subject == "history":
            return "Histoire"
        elif subject == "english":
            return "Anglais"
        elif subject == "german":
            return "Allemand"
        elif subject == "czech":
            return "Tchèque"
        elif subject == "russian":
            return "Russe"
        elif subject == "french":
            return "Français"
        elif subject == "spanish":
            return "Espagnol"
        elif subject == "literature":
            return "Littérature"
        elif subject == "music":
            return "Musique"
        elif subject == "art":
            return "Arts"
        elif subject == "informatics":
            return "Informatique"
    elif language == "spanish":
        if subject == "math":
            return "Matemáticas"
        elif subject == "physics":
            return "Física"
        elif subject == "chemistry":
            return "Química"
        elif subject == "biology":
            return "Biología"
        elif subject == "geography":
            return "Geografía"
        elif subject == "history":
            return "Historial"
        elif subject == "english":
            return "Inglés"
        elif subject == "german":
            return "Alemán"
        elif subject == "czech":
            return "Checo"
        elif subject == "russian":
            return "Ruso"
        elif subject == "french":
            return "Francés"
        elif subject == "spanish":
            return "Español"
        elif subject == "literature":
            return "Literatura"
        elif subject == "music":
            return "Música"
        elif subject == "art":
            return "Arte"
        elif subject == "informatics":
            return "Informática"


def on_subject_menu(subject, language):
    if language == "english":
        if subject == "math":
            return "Back to Math menu"
        elif subject == "physics":
            return "Back to Physics menu"
        elif subject == "chemistry":
            return "Back to Chemistry menu"
        elif subject == "biology":
            return "Back to Biology menu"
        elif subject == "geography":
            return "Back to Geography menu"
        elif subject == "history":
            return "Back to History menu"
        elif subject == "english":
            return "Back to English menu"
        elif subject == "german":
            return "Back to German menu"
        elif subject == "czech":
            return "Back to Czech menu"
        elif subject == "russian":
            return "Back to Russian menu"
        elif subject == "french":
            return "Back to French menu"
        elif subject == "spanish":
            return "Back to Spanish menu"
        elif subject == "literature":
            return "Back to Literature menu"
        elif subject == "music":
            return "Back to Music menu"
        elif subject == "art":
            return "Back to Art menu"
        elif subject == "informatics":
            return "Back to Informatics menu"
    elif language == "czech":
        if subject == "math":
            return "Zpátky na menu matematiky"
        elif subject == "physics":
            return "Zpátky na menu fyziky"
        elif subject == "chemistry":
            return "Zpátky na menu chemie"
        elif subject == "biology":
            return "Zpátky na menu biologie"
        elif subject == "geography":
            return "Zpátky na menu zeměpisu"
        elif subject == "history":
            return "Zpátky na menu dějepisu"
        elif subject == "english":
            return "Zpátky na menu angličtiny"
        elif subject == "german":
            return "Zpátky na menu němčiny"
        elif subject == "czech":
            return "Zpátky na menu češtiny"
        elif subject == "russian":
            return "Zpátky na menu ruštiny"
        elif subject == "french":
            return "Zpátky na menu francouzštiny"
        elif subject == "spanish":
            return "Zpátky na menu španělštiny"
        elif subject == "literature":
            return "Zpátky na menu literatury"
        elif subject == "music":
            return "Zpátky na menu hudby"
        elif subject == "art":
            return "Zpátky na menu umění"
        elif subject == "informatics":
            return "Zpátky na menu informatiky"
    elif language == "russian":
        if subject == "math":
            return "Обратно на меню математики"
        elif subject == "physics":
            return "Обратно на меню физики"
        elif subject == "chemistry":
            return "Обратно на меню химии"
        elif subject == "biology":
            return "Обратно на меню биологии"
        elif subject == "geography":
            return "Обратно на меню географии"
        elif subject == "history":
            return "Обратно на меню истории"
        elif subject == "english":
            return "Обратно на меню английского"
        elif subject == "german":
            return "Обратно на меню немецкого"
        elif subject == "czech":
            return "Обратно на меню чешского"
        elif subject == "russian":
            return "Обратно на меню русского"
        elif subject == "french":
            return "Обратно на меню французского"
        elif subject == "spanish":
            return "Обратно на меню испанского"
        elif subject == "literature":
            return "Обратно на меню литературы"
        elif subject == "music":
            return "Обратно на меню музыки"
        elif subject == "art":
            return "Обратно на меню искусства"
        elif subject == "informatics":
            return "Обратно на меню информатики"
    elif language == "german":
        if subject == "math":
            return "Zurück zum Mathe-Menü"
        elif subject == "physics":
            return "Zurück zum Physik-Menü"
        elif subject == "chemistry":
            return "Zurück zum Chemie-Menü"
        elif subject == "biology":
            return "Zurück zum Biologie-Menü"
        elif subject == "geography":
            return "Zurück zum Geografie-Menü"
        elif subject == "history":
            return "Zurück zum Geschichte-Menü"
        elif subject == "english":
            return "Zurück zum Englisch-Menü"
        elif subject == "german":
            return "Zurück zum Deutsch-Menü"
        elif subject == "czech":
            return "Zurück zum Tschechisch-Menü"
        elif subject == "russian":
            return "Zurück zum Russisch-Menü"
        elif subject == "french":
            return "Zurück zum Französisch-Menü"
        elif subject == "spanish":
            return "Zurück zum Spanisch-Menü"
        elif subject == "literature":
            return "Zurück zum Literatur-Menü"
        elif subject == "music":
            return "Zurück zum Musik-Menü"
        elif subject == "art":
            return "Zurück zum Kunst-Menü"
        elif subject == "informatics":
            return "Zurück zum Informatik-Menü"
    elif language == "french":
        if subject == "math":
            return "Retour au menu mathématiques"
        elif subject == "physics":
            return "Retour au menu physique"
        elif subject == "chemistry":
            return "Retour au menu chimie"
        elif subject == "biology":
            return "Retour au menu biologie"
        elif subject == "geography":
            return "Retour au menu géographie"
        elif subject == "history":
            return "Retour au menu histoire"
        elif subject == "english":
            return "Retour au menu anglais"
        elif subject == "german":
            return "Retour au menu allemand"
        elif subject == "czech":
            return "Retour au menu tchèque"
        elif subject == "russian":
            return "Retour au menu russe"
        elif subject == "french":
            return "Retour au menu français"
        elif subject == "spanish":
            return "Retour au menu espagnol"
        elif subject == "literature":
            return "Retour au menu littérature"
        elif subject == "music":
            return "Retour au menu musique"
        elif subject == "art":
            return "Retour au menu arts"
        elif subject == "informatics":
            return "Retour au menu informatique"
    elif language == "spanish":
        if subject == "math":
            return "Volver al menú de matemáticas"
        elif subject == "physics":
            return "Volver al menú de Física"
        elif subject == "chemistry":
            return "Volver al menú de Química"
        elif subject == "biology":
            return "Volver al menú de Biología"
        elif subject == "geography":
            return "Volver al menú Geografía"
        elif subject == "history":
            return "Volver al menú Historial"
        elif subject == "english":
            return "Volver al menú en inglés"
        elif subject == "german":
            return "Volver al menú alemán"
        elif subject == "czech":
            return "Volver al menú checo"
        elif subject == "russian":
            return "Volver al menú ruso"
        elif subject == "french":
            return "Volver al menú francés"
        elif subject == "spanish":
            return "Volver al menú en español"
        elif subject == "literature":
            return "Volver al menú literatura"
        elif subject == "music":
            return "Volver al menú música"
        elif subject == "art":
            return "Volver al menú arte"
        elif subject == "informatics":
            return "Volver al menú informática"


def local(language):
    if language == "english":
        return "Local"
    elif language == "czech":
        return "Lokální"
    elif language == "russian":
        return "Локальная"
    elif language == "german":
        return "Lokal"
    elif language == "french":
        return "Local"
    elif language == "spanish":
        return "Local"
