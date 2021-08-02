from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.clearcolor = [.3,.3,.3,1]

class CalcApp(App):

    def build(self):
        bl = BoxLayout(orientation="vertical",
                       padding = 10,
                       spacing = 3)
        self.input = TextInput(
                                multiline = False,
                                readonly = False,
                                font_size ='40sp',
                                halign = "right",
                                input_filter = "float",
                                size_hint =(1, .2))
        bl.add_widget(self.input)

        gl = GridLayout(cols = 4,
                        spacing = 3)
        buttons = [
            ['1/x', 'x^2', 'sqrt(x)', '<-'],
            ['7', '8', '9', 'x'],
            ['4', '5', '6', '/'],
            ['1', '2', '3', '-'],
            ['C', '0', '.', '+'],
        ]
        for row in buttons:
            for label in row:
                button = Button(text = label,
                                    font_size = '20sp',
                                    size_hint =(1, .6),
                                    background_color = [.5,.5,.5,1])
                if button.text == '<-':
                    button.bind(on_press = self.delete)
                else:
                    button.bind(on_press = self.on_button_press)
                gl.add_widget(button)

        bl.add_widget(gl)
        equals_button = Button(text = '=',
                             font_size = '30sp',
                             size_hint = (1, .2),
                             background_color=[.5, .5, .5, 1])
        equals_button.bind(on_press = self.solution)
        bl.add_widget(equals_button)
        return bl

    def on_button_press(self, instance):
        if self.input.text == 'Error':
            self.input.text = ''
        if instance.text == 'C':
            self.input.text = ''
        elif instance.text == 'x':
            self.input.text += '*'
        elif instance.text == '1/x':
            self.input.text = '1/(' + self.input.text + ')'
        elif instance.text == 'x^2':
            self.input.text = 'pow('+ self.input.text +', 2)'
        elif instance.text == 'sqrt(x)':
            self.input.text = 'sqrt(' + self.input.text + ')'
        else:
            self.input.text += instance.text

    def solution(self, instance):
        if self.input.text:
            try:
                self.input.text = str(eval(self.input.text))
            except:
                self.input.text ="Error"

    def delete(self, instance):
        self.input.text = str(self.input.text[: - 1])

if __name__ == '__main__':
    CalcApp().run()