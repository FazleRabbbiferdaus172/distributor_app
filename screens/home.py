from kivy.metrics import dp

from kivy.uix.screenmanager import Screen

from KivyMD.kivymd.uix.boxlayout import MDBoxLayout
from KivyMD.kivymd.uix.button import MDRaisedButton
from KivyMD.kivymd.uix.datatables import MDDataTable
from KivyMD.kivymd.uix.toolbar import MDTopAppBar


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(orientation='vertical', adaptive_height=True, size_hint_x=1, size_hint_y=1)

        # Top section
        topAppBar = MDTopAppBar(title='Home')

        # middle section
        dataTable = MDDataTable(
            size_hint=(.9, .9),
            pos_hint={"center_x": .5, "center_y": .5},
            column_data=[
                ("No.", dp(20)),
                ("Status", dp(50)),
                ("Signal Name", dp(50)),
            ],
            row_data=[
                (
                    "1",
                    ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
                    "Astrid: NE shared managed",),
                (
                    "2",
                    ("alert-circle", [1, 0, 0, 1], "Offline"),
                    "Cosmo: prod shared ares",
                )]
        )

        # bottom section
        bottom_layout = MDBoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(48),
            padding=dp(8),
            spacing=dp(8),
            pos_hint={"center_x": .5}
        )
        bottom_layout.add_widget(
            MDRaisedButton(text="Add data", on_press=self.add_data_pressed)
        )
        bottom_layout.add_widget(
            MDRaisedButton(text="Edit data", on_press=self.edit_data_pressed)
        )
        bottom_layout.add_widget(
            MDRaisedButton(text="Remove data", on_press=self.remove_data_pressed)
        )
        layout.add_widget(topAppBar)
        layout.add_widget(dataTable)
        layout.add_widget(bottom_layout)
        self.add_widget(layout)

    def add_data_pressed(self, button):
        print('Added data')

    def edit_data_pressed(self, button):
        print('edited data')

    def remove_data_pressed(self, button):
        print('removed data')