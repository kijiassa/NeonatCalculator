import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.widget import Widget

#Сначала настройка окон, какое есть какое и их обозначение для дальнейшего переключения
class FirstWindow(Screen):
    def fentBtn(self):
        sm.current = "fentanil"
    def aboutBtn(self):
        sm.current = "about"
class FentanilWindow(Screen):
    masBabe = ObjectProperty(None)
    dosFent = ObjectProperty(None)
    numAmp = ObjectProperty(None)
    raschet = ObjectProperty(None)
    def change(self):
        m = int(self.masBabe.text)
        sp_fent = int(self.dosFent.text)
        n_fent = int(self.numAmp.text)
        v_fent = 2 * (n_fent)
        v_NaCl = round((round((n_fent * 100 / (m / 1000)) / sp_fent, 1)) - v_fent, 1)
        qq = 'Sol.Phentanyli 50mkg/ml - {}mkg ({}ml) \n Sol.Natrii Chloridi 0.9% - {}ml \n Скорость инфузии: 1мл/ч - {}мкг/кг*час'.format((100 * n_fent), (v_fent), (v_NaCl), (sp_fent))
        self.raschet = qq
        print(self.raschet)
        sm.current = "first"
class AboutWindow(Screen):
    def back(self):
        sm.current = "first"
class WindowManager(ScreenManager):
    pass
#Установка и подключение киви файла
kv = Builder.load_file("NeoCalcKivy.kv")

sm = WindowManager()

screens = [FirstWindow(name="first"), FentanilWindow(name="fentanil"), AboutWindow(name="about")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "first"


class NeonatalApp(App): #Neonatal - это заголовок
    def build(self):
        return sm

if __name__ == "__main__":
    NeonatalApp().run()