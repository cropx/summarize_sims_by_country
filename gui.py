import customtkinter
from PIL import Image
from tkinter import ttk
import read_excel_next
import read_excel_tele_2



class Gui(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap("icon.ico")
        self.version = 0.1
        self.title(f"SimBa          Ver: {self.version}")
        self.geometry(f"{750}x{900}")
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.grid(row=0, column=0, sticky="e")

        logo = customtkinter.CTkImage(dark_image=Image.open('picture_logo.png'), size=(555*0.8, 203*0.8))
        logo_label = customtkinter.CTkLabel(self.buttons_frame, text="", image=logo)
        logo_label.grid(row=0, column=0, padx=(150, 180), pady=2)

        self.country_input = customtkinter.CTkEntry(self.buttons_frame,
                                                    placeholder_text="Country Name", width=200, height=30,
                                                    font=customtkinter.CTkFont(size=20, weight='bold'),
                                                    justify="center")
        self.country_input.grid(row=1, column=0, padx=10, pady=2)
        self.country_input.bind("<Return>", self.on_scan)

        # self.clear_all_button = customtkinter.CTkButton(self.buttons_frame, text="Clear Results", fg_color="#2d498a", width=160,
        #                                                 command=self.clear_all_units)
        # self.clear_all_button.grid(row=2, column=0, padx=(10, 2), pady=10, columnspan=3)

        bg_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
        tree_style = ttk.Style()
        tree_style.theme_use('default')
        tree_style.configure("Treeview", background=bg_color, foreground='white', fieldbackground=bg_color,
                             borderwidth=0, font=11)
        tree_style.configure("Treeview.Heading", background=bg_color, foreground='white', fieldbackground=bg_color,
                             borderwidth=0, font=(None, 13))
        tree_style.map('Treeview', background=[('selected', '#507ca3')], foreground=[('selected', 'black')])
        self.bind("<<TreeviewSelect>>", lambda event: self.focus_set())

    def create_table_next(self, data):
        columns = tuple(data[0])
        self.tree_frame_1 = customtkinter.CTkFrame(self)
        self.tree_frame_1.grid(row=4, column=0, sticky="nsew")
        logo_label = customtkinter.CTkLabel(self.tree_frame_1, text="Telit Next Profile 2 - Global - Tele 2", text_color='green', font=customtkinter.CTkFont(size=20, weight='bold'))
        logo_label.grid(row=0, column=0, padx=20, pady=5, columnspan=2)
        self.treeview_1 = ttk.Treeview(self.tree_frame_1, columns=columns, height=7, selectmode='browse',
                                       show='headings')
        for x in range(len(columns) + 1):
            if x == 1 or x == 2:
                self.treeview_1.column(f"#{x}", anchor="c", minwidth=200, width=200)
            elif x == 9:
                self.treeview_1.column(f"#{x}", anchor="c", minwidth=300, width=300)
            else:
                self.treeview_1.column(f"#{x}", anchor="c", minwidth=80, width=80)
        for column_name in columns:
            self.treeview_1.heading(column_name, text=str(column_name))

        self.treeview_1.grid(row=1, column=1, sticky='nsew', padx=10, pady=2)

    def create_table_tele_2(self, data):
        columns = tuple(data[0])
        self.tree_frame_2 = customtkinter.CTkFrame(self)
        self.tree_frame_2.grid(row=6, column=0, sticky="nsew")
        pdf_label = customtkinter.CTkLabel(self.tree_frame_2, text="Telit Type  I - NEXT", text_color='green', font=customtkinter.CTkFont(size=20, weight='bold'))
        pdf_label.grid(row=0, column=0, padx=20, pady=5, columnspan=2)
        self.treeview_2 = ttk.Treeview(self.tree_frame_2, columns=columns, height=7, selectmode='browse',
                                       show='headings')
        for x in range(len(columns) + 1):
            if x == 1 or x == 2:
                self.treeview_2.column(f"#{x}", anchor="c", minwidth=200, width=200)
            elif x == 9 or x == 10:
                self.treeview_2.column(f"#{x}", anchor="c", minwidth=150, width=150)
            else:
                self.treeview_2.column(f"#{x}", anchor="c", minwidth=80, width=80)
        for column_name in columns:
            self.treeview_2.heading(column_name, text=str(column_name))

        self.treeview_2.grid(row=1, column=1, sticky='nsew', padx=10, pady=2)

    def paste_picture_hologram(self, country):
        im = Image.open(f'countries\{country}.png')
        width, height = im.size

        self.picture_frame = customtkinter.CTkFrame(self)
        self.picture_frame.grid(row=7, column=0, sticky="nsew")
        hologram_label = customtkinter.CTkLabel(self.picture_frame, text="Hologram", text_color='green', font=customtkinter.CTkFont(size=20, weight='bold'))
        hologram_label.grid(row=0, column=0, padx=20, pady=5, columnspan=2)
        self.hologram_pic = customtkinter.CTkImage(dark_image=Image.open(f'countries\{country}.png'), size=(width*0.8, height*0.8))
        self.hologram_label = customtkinter.CTkLabel(self.picture_frame, text="", image=self.hologram_pic)
        self.hologram_label.grid(row=1, column=0, padx=(60, 60), pady=2)



    def version_def(self):
        return self.version

    def on_scan(self, event):
        country = (self.country_input.get()).capitalize()
        if country:
            self.internal_counter = 0
            result_excel = read_excel_next.find_country(country)
            self.create_table_next(result_excel)
            result_excel.pop(0)
            self.treeview_1.tag_configure('oddrow', background='#4a4a48', font=(None, 10))

            for row in result_excel:
                self.treeview_1.insert(parent='', index=self.internal_counter,
                                       values=row, tags='oddrow')
                self.internal_counter += 1


            self.internal_counter = 0
            result_pdf = read_excel_tele_2.find_country(country)
            self.create_table_tele_2(result_pdf)
            self.treeview_2.tag_configure('oddrow', background='#4a4a48', font=(None, 10))
            result_pdf.pop(0)
            for row in result_pdf:
                self.treeview_2.insert(parent='', index=self.internal_counter,
                                       values=row, tags='oddrow')
                self.internal_counter += 1

            self.paste_picture_hologram(country)
            # self.paste_picture_hologram()



gui_start = Gui()
gui_start.mainloop()
