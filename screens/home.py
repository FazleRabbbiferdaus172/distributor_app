from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from KivyMD.kivymd.uix.boxlayout import MDBoxLayout
from KivyMD.kivymd.uix.button import MDRaisedButton
from KivyMD.kivymd.uix.datatables import MDDataTable
from KivyMD.kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

KV = '''
<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "420dp"

    MDTextField:
        hint_text: "A"

    MDTextField:
        hint_text: "B"
        
    MDTextField:
        hint_text: "C"


MDFloatLayout:

    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_confirmation_dialog()
'''


class Content(BoxLayout):
    pass


class HomeScreen(Screen):
    dialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(orientation='vertical', adaptive_height=True, size_hint_x=1, size_hint_y=1)

        # Top section
        topAppBar = MDTopAppBar(title='Home')

        # middle section
        self.data_tables = MDDataTable(
            check=True,
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
                )],
        )

        self.data_tables.bind(on_row_press=self.edit_data_pressed)

        # bottom section
        self.bottom_layout = MDBoxLayout(
            pos_hint={"center_x": 0.5},
            adaptive_size=True,
            padding="24dp",
            spacing="24dp",
        )
        self.bottom_layout.add_widget(
            MDRaisedButton(text="Add data", on_press=self.add_data_pressed)
        )
        self.bottom_layout.add_widget(
            MDRaisedButton(text="Remove data", on_press=self.remove_data_pressed)
        )
        layout.add_widget(topAppBar)
        layout.add_widget(self.data_tables)
        layout.add_widget(self.bottom_layout)
        self.add_widget(layout)

    def add_data_pressed(self, button):
        if True:
            self.dialog = MDDialog(
                title="Form",
                type="custom",
                content_cls=MDBoxLayout(
                    MDTextField(
                        id="input_a",
                        hint_text="A",
                    ),
                    MDTextField(
                        id="input_b",
                        hint_text="S",
                    ),
                    MDTextField(
                        id="input_c",
                        hint_text="D",
                    ),
                    orientation="vertical",
                    spacing="12dp",
                    size_hint_y=None,
                    height="180dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        on_press=self.on_add_ok
                    ),
                ],
            )
        self.dialog.open()

    def on_add_ok(self, button):
        self.data_tables.add_row((self.dialog.content_cls.ids.input_a.text, self.dialog.content_cls.ids.input_b.text,
                                  self.dialog.content_cls.ids.input_c.text))
        self.dialog.dismiss(force=True)

    def on_edit_ok(self, button):
        self.data_tables.add_row((self.dialog.content_cls.ids.input_a.text, self.dialog.content_cls.ids.input_b.text,
                                  self.dialog.content_cls.ids.input_c.text))
        self.dialog.dismiss(force=True)

    def on_edit_ok(self, button):
        self.data_tables.row_data[self.row_edit_index] = (
        self.dialog.content_cls.ids.input_a.text, self.dialog.content_cls.ids.input_b.text,
        self.dialog.content_cls.ids.input_c.text)
        self.dialog.dismiss(force=True)

    def edit_data_pressed(self, button=None, something=None):
        self.row_edit_index = int(something.Index) // len(button.column_data)
        if int(something.Index) % len(button.column_data):
            current_row_data = self.data_tables.row_data[self.row_edit_index]
            self.dialog = MDDialog(
                title="Form",
                type="custom",
                content_cls=MDBoxLayout(
                    MDTextField(
                        id="input_a",
                        hint_text="A",
                        text=str(current_row_data[0]),
                    ),
                    MDTextField(
                        id="input_b",
                        hint_text="S",
                        text=str(current_row_data[1]),
                    ),
                    MDTextField(
                        id="input_c",
                        hint_text="D",
                        text=str(current_row_data[2]),
                    ),
                    orientation="vertical",
                    spacing="12dp",
                    size_hint_y=None,
                    height="180dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        on_press=self.on_edit_ok
                    ),
                ],
            )
            self.dialog.open()

    def remove_data_pressed(self, button):
        checked_row_index_list = [cell.index // self.data_tables.table_data.total_col_headings for cell in self.data_tables.table_data.cell_row_obj_dict.values() if cell.ids.check.state == 'down']
        # if len(self.data_tables.row_data):
        #     self.data_tables.remove_row(self.data_tables.row_data[-1])
        rows_to_remove = [self.data_tables.row_data[i] for i in checked_row_index_list]
        for row_to_remove in rows_to_remove:
            self.data_tables.remove_row(row_to_remove)

