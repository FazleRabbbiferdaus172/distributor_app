from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from KivyMD.kivymd.app import MDApp

Builder.load_file('screens/Login.kv')
# Builder.load_file('screens/Home.kv')

from screens.login import LoginScreen
from screens.home import HomeScreen

class DistributorApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == '__main__':
    DistributorApp().run()