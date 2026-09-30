from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class MyApp(App):
    def build(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        number = TextInput(
            hint_text="Enter number",
            input_filter="int",
            multiline=False,
            font_size=25
        )

        button = Button(
            text="Show multiplication table",
            font_size=22
        )

        result = Label(
            text="Result",
            font_size=25
        )

        def calculate(instance):
            if number.text:
                n = int(number.text)
                result.text = ""

                for i in range(1, 11):
                    result.text += f"{n} × {i} = {n*i}\n"

        button.bind(on_press=calculate)

        layout.add_widget(number)
        layout.add_widget(button)
        layout.add_widget(result)

        return layout


MyApp().run()