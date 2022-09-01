import random
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton

screen_helper = """
ScreenManager:
    id: screen_manager
    WordScreen:
    MeaningScreen:
    Win1Screen:
    Win2Screen:
    Win3Screen:
    Win4Screen:
    InfoScreen:


<WordScreen>
    name: 'wordscreen'
    FitImage:
        source: 'img/bgr.png'
    MDRaisedButton:
        text: 'Играть'
        font_name: 'img/KankinRegular.otf'
        md_bg_color: 0.9, 0, 0, 0.9 
        id: search_button
        pos_hint: {'center_x': 0.5, 'center_y': 0.25}
        on_release: on_release: app.show_confirmation_dialog()



    MDRaisedButton:
        text: 'Инфо'
        font_name: 'img/KankinRegular.otf'
        md_bg_color: 0.9, 0, 0, 0.9 
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        on_release: root.manager.current = 'infoscreen'


<MeaningScreen>
    name: 'meaningscreen'

    FitImage:
        source: 'img/bgr4.png' 
    MDRaisedButton:
        text: 'показать карту'
        font_name: 'img/KankinRegular.otf'
        md_bg_color: 0.9, 0, 0, 0 
        id: show_map
        pos_hint: {'center_x': 0.5, 'center_y': 0.53}
        size_hint: 0.7, 0.58
        on_press : root.on_karta()
        Image:
            id: imageView
            source: 'img/ico.png'
            allow_stretch: True
            size_hint: (1.1, 1.1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
    MDRaisedButton:
        text: 'скрыть карту'
        font_name: 'img/KankinRegular.otf'
        id: hide_map
        pos_hint: {'center_x': 0.5, 'center_y': 0.17}
        on_press : root.off_karta()
        md_bg_color: 0.9, 0, 0, 0.9 
    MDBottomAppBar:
        opposite_colors: True
        md_bg_color: "ff0000"
        MDToolbar:
            id: meaningbar
            title: "Игрок №1"
            icon: "play"
            mode: "end"
            type: "bottom"
            on_action_button: root.start_game()
            left_action_items: [["menu", lambda x: root.restart() ]]
            icon_color: "ff0000"

<Win1Screen>
    name: 'infoscreen2'
    FitImage:
        source: 'img/bgr3.png'
        size_hint: 1.29, 1.29
        pos_hint: {"center_x": .5, "center_y": .5}
    MDRaisedButton:    
        text: 'Назад'
        font_name: 'img/KankinRegular.otf'
        md_bg_color: 0.9, 0, 0, 0.9 
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_release: root.manager.current = 'infoscreen'


<Win2Screen>
    name: 'zh_pobeda'
    FitImage:
        source: 'img/bgr5.png'
    MDRaisedButton:  
        text: 'Домой'
        font_name: 'img/KankinRegular.otf'
        md_bg_color: 0.9, 0, 0, 0.9 
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        on_release: root.manager.current = 'wordscreen'
        
<Win4Screen>
    name: 'm_pobeda'
    FitImage:
        source: 'img/bgr6.png'
    MDRaisedButton:  
        text: 'Домой'
        font_name: 'img/KankinRegular.otf'
        md_bg_color: 0.9, 0, 0, 0.9 
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        on_release: root.manager.current = 'wordscreen'

<Win3Screen>
    name: 'gamescreen'
    FitImage:
        source: 'img/bgr4.png'
    MDLabel:   
        text: "Игрок: "
        font_name: 'img/KankinRegular.otf'
        id: meaning
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: [1, 1, 1, 1]
        font_style: 'Body1'
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
    GridLayout:
        size_hint_y: None
        size_hint_x: None
        height: self.minimum_height
        width: self.minimum_width
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        rows: 4
        cols: 3
        font_size: dp(.1)
        spacing: "12dp"
        padding: "12dp"
        MDRaisedButton:
            id: p1
            text: "1"
            font_name: 'img/KankinRegular.otf'
            on_press: root.signal("1")
            md_bg_color: 0.9, 0, 0, 0.9
        MDRaisedButton:
            id: p2
            text: "2"
            font_name: 'img/KankinRegular.otf'
            on_press: root.signal("2")
            md_bg_color: 0.9, 0, 0, 0.9
        MDRaisedButton:
            id: p3
            text: "3"
            font_name: 'img/KankinRegular.otf'
            on_press: root.signal("3")
            md_bg_color: 0.9, 0, 0, 0.9 
        MDRaisedButton:
            id: p4
            text: "4"
            font_name: 'img/KankinRegular.otf'
            on_press: root.signal("4")
            md_bg_color: 0.9, 0, 0, 0.9 
        MDRaisedButton:
            id: p5
            text: "5"
            font_name: 'img/KankinRegular.otf'
            on_press: root.signal("5")
            md_bg_color: 0.9, 0, 0, 0.9 
        MDRaisedButton:
            id: p6
            text: "6"
            font_name: 'img/KankinRegular.otf'
            on_press: root.signal("6")
            md_bg_color: 0.9, 0, 0, 0.9 
        MDRaisedButton:
            id: p7
            text: "7"
            font_name: 'img/KankinRegular.otf'
            on_press: root.signal("7")
            md_bg_color: 0.9, 0, 0, 0.9 
        MDRaisedButton:
            id: p8
            text: "8"
            font_name: 'img/KankinRegular.otf'
            on_press: root.signal("8")
            md_bg_color: 0.9, 0, 0, 0.9 
        MDRaisedButton:
            id: p9
            text: "9"
            font_name: 'img/KankinRegular.otf'
            on_press: root.signal("9")
            md_bg_color: 0.9, 0, 0, 0.9 
        MDRaisedButton:
            id: p10
            text: "10"
            font_name: 'img/KankinRegular.otf'
            on_press: root.signal("10")
            md_bg_color: 0.9, 0, 0, 0.9 
        MDRaisedButton:
            id: p11
            text: "11"
            font_name: 'img/KankinRegular.otf'
            on_press: root.signal("11")
            md_bg_color: 0.9, 0, 0, 0.9 
        MDRaisedButton:        
            id: p12
            text: "12"
            font_name: 'img/KankinRegular.otf'
            on_press: root.signal("12")
            md_bg_color: 0.9, 0, 0, 0.9

    MDRaisedButton:
        size_hint: (.055, .055)
        font_name: 'img/KankinRegular.otf'
        md_bg_color: 0.9, 0, 0, 0.9 
        pos_hint: {'center_x': 0.35, 'center_y': 0.2}
        on_release: root.manager.current = 'wordscreen'
        Image:
            source: "img/nazad.png"
            size_hint: (0.5, 0.5)
    MDRaisedButton:
        size_hint: (.055, .055)
        pos_hint: {'center_x': 0.65, 'center_y': 0.2}
        on_press: root.next_hod()
        md_bg_color: 0.9, 0, 0, 0.9
        Image:
            source: "img/galochka.png"
            size_hint: (0.5, 0.5)

<InfoScreen>
    name: 'infoscreen'
    FitImage:
        source: 'img/bgr2.png'
        size_hint: 1.29, 1.29
        pos_hint: {"center_x": .5, "center_y": .5}
    MDRaisedButton:    
        text: 'Дальше'
        font_name: 'img/KankinRegular.otf'
        md_bg_color: 0.9, 0, 0, 0.9 
        pos_hint: {'center_x': 0.6, 'center_y': 0.13}
        on_release: root.manager.current = 'infoscreen2'
    MDRaisedButton:    
        text: 'Назад'
        font_name: 'img/KankinRegular.otf'
        md_bg_color: 0.9, 0, 0, 0.9 
        pos_hint: {'center_x': 0.3, 'center_y': 0.13}
        on_release: root.manager.current = 'wordscreen'


    MDList:
        id: box

<Content>
    name: 'content'
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "60dp"

    MDTextField:
        name: "count_play"
        text_color: [0.9, 0, 0, 0.9]
        line_color_focus: 0.9, 0, 0, 0.9
        hint_text: "Количество игроков"
        font_name: 'img/KankinRegular.otf'
        text: "4"

"""
role = {"mafia": 'img/m.png',
        "doctor": 'img/d.png',
        "detective": 'img/sh.png',
        "inhabitants": 'img/j1.png',
        "lusya": "img/j2.png"}


def mafia_lot(number, lot):
    global dict, dict_players, pl, amount_players, amount_mafia
    mafia = lot[0]
    pl = 0
    dict_players = []
    amount_players = int(number)  # Сколько игроков в игре
    amount_mafia = int(mafia)  # Сколько мафий в игре для дороботок
    amount_detective = lot[1]  # есть или нет детектив в игре для дороботок
    amount_lusya = lot[2]
    count = number
    game.gaming.amount_mafia = amount_mafia
    players = list(range(1, amount_players + 1))
    mafia = [players.pop() for _ in range(amount_mafia)]
    doctor = players.pop()
    if amount_detective:
        detective = players.pop()
    if amount_lusya:
        lusya = players.pop()
        game.gaming.role = "lusya"
    else:
        game.gaming.role = "mafia"
    inhabitants = players
    for i in mafia:
        dict_players.append("mafia")
    dict_players.append("doctor")
    if amount_detective:
        dict_players.append("detective")
    if amount_lusya:
        dict_players.append("lusya")
    for i in inhabitants:
        dict_players.append("inhabitants")

    dict = random.sample(dict_players, len(dict_players))

class Win4Screen(Screen):
    def on_pre_enter(self, *args):
        game.gaming.click.play()

class Gaming:
    def __init__(self):
        self.restart()
        self.click = SoundLoader.load("img/click.wav")
        self.tts = SoundLoader.load("img/tts.wav")
        self.tts_m = SoundLoader.load("img/tts_m.wav")
        self.tts_do = SoundLoader.load("img/tts_do.wav")
        self.tts_de = SoundLoader.load("img/tts_de.wav")
        self.tts_l = SoundLoader.load("img/tts_l.wav")
        self.tts_zh = SoundLoader.load("img/tts_zh.wav")
        self.tts_zhp = SoundLoader.load("img/tts_zhp.wav")

    def restart(self):
        self.lech = 0
        self.dict_players = []
        self.zhertva = ""
        self.alibi = 0
        self.arest = ""
        self.tm = "Город засыпает, просыпается мафия"
        self.tz = "Мафия сделал свой выбор, мафия засыпает"
        self.td = "Просыпается доктор"
        self.tdz = "Доктор сделал свой выбор, доктор засыпает"
        self.tg = "Город просыпается"
        self.tdetective = "Просыпается шериф"
        self.dgorod = "Город просыпается\n"
        self.dlech = "Доктор вылечил:\n"
        self.dmaf = "Мафия убила:\n"
        self.ddet = "Шериф арестовал:\n"
        self.ddettrue = "Шериф обнаружил мафию"
        self.ddetfalse = "Шериф не обануржил мафию"
        self.lech = ""
        self.zhertva_m = ""
        self.sleep = ""

    def mafia_found(self, zhertva):
        game.dialog_info = True
        game.list_zhertv.append(zhertva)
        if dict[int(zhertva) - 1] == "mafia":
            game.gaming.amount_mafia -= 1
            if "mafia" in dict:
                if game.gaming.amount_mafia == 0:
                    self.zhertva = "Жители победили, мафия проиграла"                     
                    game.root.current = "zh_pobeda"
                    self.sleep = "просыпается мафия"
                else:
                    self.zhertva = "Мафия обнаружена, осталось " + str(game.gaming.amount_mafia)
                    if self.role == "detective":
                        self.role = "inhabitants"
                    else:
                        if "lusya" in dict:
                            self.role = "lusya"
                        else:
                            self.role = "mafia"
                return "Мафия обнаружена"
        else:
                self.zhertva = "Мафия необнаружена"
                if self.role == "detective":
                    self.role = "inhabitants"
                else:
                    live = int(len(dict)) - int(dict.count("-"))
                    print(live)
                    m_live = int(dict.count("mafia"))
                    if live - m_live <= 2:
                        self.zhertva = "Мафия победила"
                        game.root.current = "m_pobeda"
                        game.gaming.tts.play()
                    else:
                        if "lusya" in dict:
                            self.role = "lusya"
                        else:
                            self.role = "mafia"
    def lusya_func(self):
        if self.alibi == self.zhertva_m:
            game.list_zhertv.append(dict.index("lusya")-1)
            self.zhertva_m += " и " + str(dict.index("lusya")+1)
        if self.alibi == self.arest:
            game.list_zhertv.remove(self.arest)
        if self.alibi == str(dict.index("detective")+1):
            game.list_zhertv.remove(self.arest)
        if self.alibi == (dict.index("mafia")+1) and game.amount_mafia == 1:
            game.list_zhertv.remove(self.zhertva_m)

    def win_dialog(self):
        if "lusya" in dict:
            self.lusya_func()
        text = "Просыпается город\n\n" + self.dmaf + self.zhertva_m + "\n\n"
        if "lusya" in dict:
            text += "Любовница провела ночь с:\n" + self.alibi + " (У этого игрока алиби на голосовании)\n\n"
        if "doctor" in dict:
            text += self.dlech + self.lech + "\n\n"
        if "detective" in dict:
            text += self.ddet + self.arest + "\n\n"
            if dict[int(self.arest)-1] == "mafia":
                #dict[int(self.arest) - 1] = "-"
                text += "Шериф обнаружил мафию"
            else:
                text += "Шериф не обнаружил мафию"
        self.ulz()
        live = int(len(dict)) - int(dict.count("-"))
        print(live)
        m_live = int(dict.count("mafia"))
        if live - m_live < 2:
            self.zhertva = "Мафия победила"
            game.root.current = "m_pobeda"

        return text

    def ulz(self):
        for z in game.list_zhertv:
            dict[int(z) - 1] = "-"

    def hod(self, zhertva):
        if self.role == "lusya":
            self.alibi = zhertva
            self.role = "mafia"
        elif self.role == "mafia":
            self.zhertva_m = zhertva
            if "doctor" in dict:
                self.sleep = self.td
                self.role = "doctor"
            elif "detective" in dict:
                self.sleep = self.tdetective
                self.role = "detective"
            else:
                self.sleep = self.tg
                self.role = "inhabitants"
            if not "doctor" in dict:
                game.list_zhertv.append(self.zhertva_m)
                if self.zhertva_m == self.alibi:
                    game.list_zhertv.append(str(dict.index("lusya")+1))
            return self.tz
        elif self.role == "doctor":
            self.lech = zhertva
            game.list_lech.append(self.lech)
            if self.zhertva_m == self.lech and dict[int(self.alibi)-1] != "doctor":
               self.zhertva_m = ""
            else:
               game.list_zhertv.append(self.zhertva_m)
               if self.zhertva_m == self.alibi and self.lech != str(dict.index("lusya")+1):
                   game.list_zhertv.append(str(dict.index("lusya")+1))
            if "detective" in dict:
                self.sleep = self.tdetective
                self.role = "detective"
            else:
                self.sleep = self.tg
                self.role = "inhabitants"
            game.dialog_info = True
            return self.tdz
        elif self.role == "detective":
            self.arest = zhertva
            found = self.mafia_found(self.arest)
            return found
        elif self.role == "inhabitants":
            found = self.mafia_found(zhertva)
            return found


class InfoScreen(Screen):
    def on_pre_enter(self, *args):
        game.gaming.click.play()


class WordScreen(Screen):
    def on_pre_enter(self, *args):
        game.gaming.click.play()


class Win1Screen(Screen):
    def on_pre_enter(self, *args):
        game.gaming.click.play()


class Win2Screen(Screen):
    def on_pre_enter(self, *args):
        game.gaming.tts_zh.stop()
        game.gaming.tts_m.stop()
        game.gaming.tts_do.stop()
        game.gaming.tts_de.stop()
        game.gaming.tts_l.stop()
        game.gaming.tts_zhp.play()


class Content(BoxLayout):
    pass


class MeaningScreen(Screen):
    Dialog = None

    def on_pre_enter(self, *args):
        game.gaming.click.play()

    def on_karta(self):
        global pl
        game.gaming.click.play()
        if pl == 0:
            self.on = True
        if self.on:
            i = dict[pl]
            self.ids.imageView.source = role[i]
            pl += 1
            self.on = False
        self.ids.meaningbar.title = "Игрок №" + str(pl)

    def off_karta(self):
        if pl < len(dict):
            game.gaming.click.play()
            self.on = True
            self.ids.imageView.source = 'img/ico.png'
        else:
            game.gaming.click.play()
            self.ids.imageView.source = 'img/ico.png'

    def next_game(self, *args):
        self.off_karta()
        game.gaming.click.play()
        self.dialog.dismiss()
        self.ids.meaningbar.title = "Игрок №1"
        self.manager.current = "wordscreen"

    def restart(self):
        if not self.Dialog:
            self.dialog = MDDialog(
                text="Вы уверены в окончание игры?",
                buttons=[
                    MDFlatButton(
                        text="Отмена",
                        on_release=self.closedialog
                    ),
                    MDFlatButton(
                        text="Ок",
                        on_release=self.next_game
                    ),
                ],
            )
            self.dialog.open()

    def closedialog(self, inst):
        game.gaming.click.play()
        self.dialog.dismiss()

    def start_game(self):
        if pl == int(game.searchword):
            game.gaming.click.play()
            game.gaming.restart()
            self.off_karta()
            self.ids.meaningbar.title = "Игрок №1"
            self.manager.current = "gamescreen"


class Win3Screen(Screen):
    Dialog = None

    def on_pre_enter(self, *args):
        game.list_zhertv = []
        self.activ()
        self.number_player = "Игрок: № "
        self.sound = SoundLoader.load("img/sound_1.wav")
        self.sound.play()
        self.grey()

    def grey(self):
        for z in range(1, 13):
            p = "p" + str(z)
            if z <= amount_players and str(z) not in game.list_zhertv:
                self.ids[p].md_bg_color = .9, 0, 0, .9
            else:
                self.ids[p].md_bg_color = .5, 0, 0, .9

    def activ(self, *args):
        if game.gaming.role == "mafia":
            role = "мафия"
        elif game.gaming.role == "doctor":
            role = "доктор"
        elif game.gaming.role == "detective":
            role = "шериф"
        elif game.gaming.role == "inhabitants":
            role = "город"
        elif game.gaming.role == "lusya":
            role = "любовница"
        if role != "город":
            if role == "мафия":
                game.gaming.tts_m.play()
            if role == "доктор":
                game.gaming.tts_do.play()
            if role == "шериф":
                game.gaming.tts_de.play()
            if role == "любовница":
                game.gaming.tts_l.play()
            self.dialog = MDDialog(
                text="Просыпается " + role,
                radius=[20]
            )
            self.dialog.open()
        else:
            game.gaming.tts_zh.play()
            self.dialog = MDDialog(text=game.gaming.win_dialog(), radius=[20])
            self.dialog.open()
            self.grey()

    def dialog_close(self, inst):
        self.dialog.dismiss()

    def signal(self, signal):
        game.gaming.click.play()
        pred_number = "Игрок: № "
        self.number_player = pred_number + signal
        self.ids.meaning.text = self.number_player

    def clear(self):
        self.ids.meaning.text = "Игрок: № "

    def next_hod(self):
        if self.number_player != "Игрок: № ":
            number2 = self.number_player.split("Игрок: № ")
            zhertva = number2[1]
            if zhertva not in game.list_zhertv and (int(zhertva) > 0 and int(zhertva) <= amount_players):
                if zhertva == game.list_lech[-1] and game.gaming.role == "doctor":
                    self.dialog = MDDialog(
                        text="Второй раз подряд лечить нельзя",
                        radius=[20]
                    )
                    self.dialog.open()
                    self.ids.meaning.text = "Игрок: № "
                elif dict[int(zhertva)-1] == "mafia" and game.gaming.role == "mafia":
                    self.dialog = MDDialog(
                        text="Своих не бьют!",
                        radius=[20]
                    )
                    self.dialog.open()
                elif dict[int(zhertva)-1] == "detective" and game.gaming.role == "detective":
                    self.dialog = MDDialog(
                        text="Своих не бьют!",
                        radius=[20]
                    )
                    self.dialog.open()

                else:
                    self.ids.meaning.text = "Игрок: № "
                    game.gaming.hod(zhertva)
                    self.activ()

            else:
                self.dialog = MDDialog(
                    text="Игрока с таким номером нет\nили он убит",
                    radius=[20]
                )
                self.dialog.open()
                self.ids.meaning.text = "Игрок: № "
        else:
            self.dialog = MDDialog(
                text="Выберете игрока",
                radius=[20]
            )
            self.dialog.open()
            self.ids.meaning.text = "Игрок: № "


class TestApp(MDApp):
    dialog = None

    def __init__(self, **kwargs):
        self.title = "Mafia"
        self.searchword = 0
        self.list_zhertv = []
        self.list_lech = [0]
        self.amount_mafia = 0
        self.gaming = Gaming()
        self.win = Win3Screen()
        self.dialog_info = False
        super().__init__(**kwargs)

    def build(self):
        window_size = Window.size
        win_h = window_size[1]
        win_w = win_h / 16 * 9
        Window.size = (win_w, win_h)
        sm = Builder.load_string(screen_helper)
        self.icon = "img/logo.png"
        return sm

    def show_data_meaning(self, p, m):
        self.searchword = p
        mafia_lot(int(self.searchword), int(m))
        self.amount_mafia = int(m)
        return self.searchword

    def my_func(self, p):
        if not 4 <= int(p) <= 12:
            return False
        d = True
        if int(p) >= 10:
            m = "4"
            l = "1"
        elif int(p) >= 8:
            m = "3"
            l = "1"
        elif int(p) >= 6:
            m = "2"
            l = "1"
        else:
            m = "1"
            d = False
            l = False
        return (m, d, l)  # d добавить детективов

    def newwindows(self, *args):
        compos = []
        for obj in self.dialog.content_cls.children:
            if isinstance(obj, MDTextField):
                compos.append(obj.text)
        p = compos[0]
        s_game = self.my_func(p)
        self.dialog.dismiss()
        self.root.current = "meaningscreen"
        if s_game:
            mafia_lot(p, s_game)
            self.searchword = p
        else:
            self.dialog_err = MDDialog(
                text="Нельзя меньше 4-х и больше 11-и человек!",
                radius=[20]
            )
            self.dialog_err.open()
            self.root.current = "wordscreen"

    def zp(self, *args):
        game.gaming.tts_zh.stop()
        game.gaming.tts_m.stop()
        game.gaming.tts_do.stop()
        game.gaming.tts_de.stop()
        game.gaming.tts_l.stop()
        self.root.current = "zh_pobeda"

    def closedialog(self, inst):
        self.dialog.dismiss()

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Состав игроков:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="Отмена", text_color=self.theme_cls.primary_color, on_release=self.closedialog
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color, on_release=self.newwindows)
                ],
            )
        self.dialog.open()


if __name__ == '__main__':
    game = TestApp()
    game.run()
