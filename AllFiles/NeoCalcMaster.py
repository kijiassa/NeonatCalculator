import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstWindow(Screen):
    pass

class FentanilWindow(Screen):
    pass

class AboutWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("NeoCalcKivy.kv")

class NeonatalApp(App): #Neonatal - это заголовок
    def build(self):
        return kv

if __name__ == "__main__":
    NeonatalApp().run()