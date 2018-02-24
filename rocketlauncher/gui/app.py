from kivy.app import App
from kivy.uix.widget import Widget


class MainWindow(Widget):
    pass


class RocketLauncherApp(App):
    def build(self):
        return MainWindow()


def run():
    RocketLauncherApp().run()
