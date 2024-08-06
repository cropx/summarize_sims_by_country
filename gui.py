import customtkinter
from PIL import Image
from tkinter import ttk
import read_ext_files
from CTkMessagebox import CTkMessagebox

read_ext_files = read_ext_files.ReadExcel()


class Gui(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.treeview_2 = None
        self.tree_frame_2 = None
        self.hologram_label = None
        self.hologram_pic = None
        self.picture_frame = None
        self.treeview_1 = None
        self.tree_frame_1 = None
        self.clear_frames = False
        self.iconbitmap("icon.ico")
        self.version = 0.2
        self.title(f"SimBa          Ver: {self.version}")
        self.geometry(f"{850}x{900}")
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.grid(row=0, column=0, sticky="e")

        im = Image.open(f'picture_logo.png')
        width, height = im.size
        logo = customtkinter.CTkImage(dark_image=Image.open('picture_logo.png'),
                                      size=(int(width * 0.9), int(height * 0.8)))

        logo_label = customtkinter.CTkLabel(self.buttons_frame,
                                            text="",
                                            image=logo)
        logo_label.grid(row=0, column=0, padx=(200, 200), pady=2)

        im = Image.open(f'cropx_logo.png')
        width, height = im.size
        logo = customtkinter.CTkImage(dark_image=Image.open('cropx_logo.png'),
                                      size=(int(width * 0.35), int(height * 0.35)))

        logo_label = customtkinter.CTkLabel(self.buttons_frame,
                                            text="",
                                            image=logo)
        logo_label.grid(row=0, column=0, padx=210, pady=10, sticky="ws")

        self.country_input = customtkinter.CTkEntry(self.buttons_frame,
                                                    placeholder_text="Country Name",
                                                    width=200,
                                                    height=30,
                                                    font=customtkinter.CTkFont(size=20, weight='bold'),
                                                    justify="center")
        self.country_input.grid(row=1, column=0, padx=10, pady=2)
        self.country_input.bind("<Return>", self.on_scan)

        bg_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
        tree_style = ttk.Style()
        tree_style.theme_use('default')
        tree_style.configure("Treeview",
                             background=bg_color,
                             foreground='white',
                             fieldbackground=bg_color,
                             borderwidth=0,
                             font=11)

        tree_style.configure("Treeview.Heading",
                             background=bg_color,
                             foreground='white',
                             fieldbackground=bg_color,
                             borderwidth=0,
                             font=(None, 13))

        tree_style.map('Treeview',
                       background=[('selected', '#507ca3')],
                       foreground=[('selected', 'black')])

        self.bind("<<TreeviewSelect>>", lambda event: self.focus_set())

    def create_table(self, data, row, frame_attr, treeview_attr, label_text, more_info_command):
        columns = tuple(data[0])
        frame = customtkinter.CTkFrame(self)
        setattr(self, frame_attr, frame)
        frame.grid(row=row, column=0, padx=20, sticky="nsew")

        sim_type_label = customtkinter.CTkLabel(frame,
                                                text=label_text,
                                                text_color='#2d498a',
                                                font=customtkinter.CTkFont(size=20, weight='bold'))
        sim_type_label.grid(row=0, column=1, padx=10, pady=5)

        more_info_btn = customtkinter.CTkButton(frame,
                                                text="More_Info",
                                                fg_color="#2d498a",
                                                width=80,
                                                command=more_info_command)
        more_info_btn.grid(row=0, column=2, padx=10, pady=5)

        tree_scroll = customtkinter.CTkScrollbar(frame)
        tree_scroll.grid(row=1, column=0, sticky="w")

        treeview = ttk.Treeview(frame,
                                yscrollcommand=tree_scroll.set,
                                columns=columns,
                                height=6,
                                selectmode='browse',
                                show='headings')
        setattr(self, treeview_attr, treeview)

        for x in range(len(columns) + 1):
            if x == 2:
                treeview.column(f"#{x}", anchor="c", minwidth=260, width=260)
            elif x == 1 or x == 2:
                treeview.column(f"#{x}", anchor="c", minwidth=180, width=180)
            else:
                treeview.column(f"#{x}", anchor="c", minwidth=80, width=80)

        for column_name in columns:
            treeview.heading(column_name, text=str(column_name))

        treeview.grid(row=1, column=0, sticky='nsew', padx=20, pady=5, columnspan=3)

    def create_table_next(self, data):
        self.create_table(data, 3, 'tree_frame_1', 'treeview_1', 'Telit Next Profile 2', self.more_info_next_msg)

    def create_table_tele_2(self, data):
        self.create_table(data, 4, 'tree_frame_2', 'treeview_2', 'Telit Type  I - Tele 2', self.more_info_tele2_msg)

    def get_picture_hologram(self, result_hologram):  # [country, result_hologram]
        width, height = result_hologram[1].size

        self.picture_frame = customtkinter.CTkFrame(self)
        self.picture_frame.grid(row=5, column=0, sticky="nsew")
        hologram_label = customtkinter.CTkLabel(self.picture_frame, text="Hologram", text_color='#2d498a',
                                                font=customtkinter.CTkFont(size=20, weight='bold'))
        hologram_label.grid(row=0, column=0, padx=20, pady=5, columnspan=2)
        self.hologram_pic = customtkinter.CTkImage(dark_image=Image.open(f'countries\{result_hologram[0]}.png'),
                                                   size=(int(width * 0.8), int(height * 0.8)))
        self.hologram_pic = customtkinter.CTkLabel(self.picture_frame, text="", image=self.hologram_pic)
        self.hologram_pic.grid(row=1, column=0, padx=110, pady=2)

    def version_def(self) -> float:
        return self.version

    def clear_all(self):
        try:
            for widget in self.tree_frame_2.winfo_children():
                widget.destroy()
        except:
            print("missing children")
        try:
            for widget in self.tree_frame_1.winfo_children():
                widget.destroy()
        except:
            print("missing children")
        try:
            self.hologram_pic.configure(image=None)
            self.hologram_pic.image = None
            self.clear_frames = False
        except:
            print("missing hologram pic")

    def on_scan(self, event):
        if self.clear_frames:
            print("clear")
            self.clear_all()
        country = (self.country_input.get())
        if country:
            internal_counter = 0
            result_excel_next = read_ext_files.get_data(country, "next")
            if result_excel_next is not None:
                print(f'result {result_excel_next}')
                self.create_table_next(result_excel_next)
                result_excel_next.pop(0)
                self.treeview_1.tag_configure('oddrow', background='#4a4a48', font=(None, 10))

                for row in result_excel_next:
                    self.treeview_1.insert(parent='', index=internal_counter,
                                           values=row, tags='oddrow')
                    internal_counter += 1
                self.clear_frames = True

            internal_counter = 0
            result_excel_tele2 = read_ext_files.get_data(country, "tele2")
            if result_excel_tele2 is not None:
                self.create_table_tele_2(result_excel_tele2)
                self.treeview_2.tag_configure('oddrow', background='#4a4a48', font=(None, 10))
                result_excel_tele2.pop(0)
                for row in result_excel_tele2:
                    self.treeview_2.insert(parent='', index=internal_counter,
                                           values=row, tags='oddrow')
                    internal_counter += 1
                self.clear_frames = True

            result_hologram = read_ext_files.get_data(country, "hologram")
            print(f'result_hologram {result_hologram}')
            if result_hologram[1] is not None:
                self.get_picture_hologram(result_hologram)  # [country, result_hologram]
                self.clear_frames = True

    def more_info_tele2_msg(self):
        dialog = CTkMessagebox(title="More_Info",
                               message=("1 Please contact Sales for pricing and/or Access Fee charges.\n"
                                        "2 Permanent roaming is not allowed.\n"
                                        "3 Mobile Network Operators may not distinguish between LTE traffic types. "
                                        "Therefore LTE-M services may be\n"
                                        "   accessible via networks in which LTE-M has been deployed and this Coverage "
                                        "List indicates LTE availability. \n"
                                        "   Telit Cinterion does not guarantee the availability of such services.\n"
                                        "4. VoLTE – coverage for information only. Service availability will be "
                                        "announced."),
                               font=customtkinter.CTkFont(size=14), width=900, icon="info", wraplength=750)

    def more_info_next_msg(self):
        dialog = CTkMessagebox(title="More_Info",
                               message=("*  Mobile Network Operators generally do not distinguish between 4G traffic; "
                                        "therefore LTE-M should be accessible\n"
                                        "  via networks in which LTE-M has been deployed and the Coverage List"
                                        "includes 4G availability"),
                               font=customtkinter.CTkFont(size=14), width=900, icon="info", wraplength=750)
