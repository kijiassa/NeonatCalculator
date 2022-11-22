import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label



class FirstWindow(Screen):
    def fentBtn(self):
        sm.current = "fentanil"

    def aboutBtn(self):
        sm.current = "about"

class FentanilWindow(Screen):
    def back(self):
        sm.current = "first"

class AboutWindow(Screen):
    def back(self):
        sm.current = "first"

class WindowManager(ScreenManager):
    pass

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