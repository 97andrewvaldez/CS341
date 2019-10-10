#! python3
import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
    def p(self):
        print(self.username)
        print(self.password)

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text = 'Who is you daddy?'))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)
        self.add_widget(Label(text = 'And what does he do?'))
        self.password = TextInput(password = True, multiline = False)
        self.add_widget(self.password)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
