#! python3
import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

class LoginScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        # self.GridLayout(cols=2, row_force_default=True, row_default_height=40)
        # self.FloatLayout(size = (300, 300))
        self.size = (50, 50)
        # the enter button
        self.button = Button(text = 'Enter',
                        size_hint = (.25, .10),
                        pos_hint = {'x':.37, 'y':.4}
                        # pos = (300, 300)
                            )
        self.add_widget(self.button)

        # The username prompt label
        self.username_label = Label(text = 'Username: ',
                                size_hint = (.25, .10),
                                pos_hint = {'x': .10, 'y':.80})
        self.add_widget(self.username_label)

        # the username textbox
        self.username = TextInput(multiline = False,
                        size_hint = (.3, .05),
                        pos_hint = {'x': .35, 'y': .825})
        self.add_widget(self.username)

        # the password prompt label
        self.password_label = Label(text = 'Password: ',
                                size_hint = (.25, .10),
                                pos_hint = {'x': .10, 'y':.70})
        self.add_widget(self.password_label)

        self.password = TextInput(multiline = False,
                        size_hint = (.3, .05),
                        pos_hint = {'x': .35, 'y': .725})
        self.add_widget(self.password)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
