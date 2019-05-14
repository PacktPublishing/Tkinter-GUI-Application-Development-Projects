import os
from tkinter import *
from tkinter import filedialog


PROGRAM_NAME = ' Explosion Drum Machine '
MAX_NUMBER_OF_PATTERNS = 10
MAX_NUMBER_OF_DRUM_SAMPLES = 5
MAX_NUMBER_OF_UNITS = 5
MAX_BPU = 5
INITIAL_NUMBER_OF_UNITS = 4
INITIAL_BPU = 4
INITIAL_BEATS_PER_MINUTE = 240
MIN_BEATS_PER_MINUTE = 80
MAX_BEATS_PER_MINUTE = 360
COLOR_1 = 'grey55'
COLOR_2 = 'khaki'
BUTTON_CLICKED_COLOR = 'green'


class DrumMachine:

    def __init__(self, root):
        self.root = root
        self.root.title(PROGRAM_NAME)
        self.all_patterns = [None] * MAX_NUMBER_OF_PATTERNS
        self.current_pattern = IntVar()
        self.number_of_units = IntVar()
        self.bpu = IntVar()
        self.to_loop = BooleanVar()
        self.beats_per_minute = IntVar()

        self.drum_load_entry_widget = [None] * MAX_NUMBER_OF_DRUM_SAMPLES

        self.init_all_patterns()
        self.init_gui()

    def get_current_pattern_dict(self):
        return self.all_patterns[self.current_pattern.get()]

    def get_bpu(self):
        return self.get_current_pattern_dict()['bpu']

    def set_bpu(self):
        self.get_current_pattern_dict()['bpu'] = self.bpu.get()

    def get_number_of_units(self):
        return self.get_current_pattern_dict()['number_of_units']

    def set_number_of_units(self):
        self.get_current_pattern_dict(
        )['number_of_units'] = self.number_of_units.get()

    def get_list_of_drum_files(self):
        return self.get_current_pattern_dict()['list_of_drum_files']

    def get_drum_file_path(self, drum_index):
        return self.get_list_of_drum_files()[drum_index]

    def set_drum_file_path(self, drum_index, file_path):
        self.get_list_of_drum_files()[drum_index] = file_path

    def get_is_button_clicked_list(self):
        return self.get_current_pattern_dict()['is_button_clicked_list']

    def set_is_button_clicked_list(self, num_of_rows, num_of_columns):
        self.get_current_pattern_dict()['is_button_clicked_list'] = [
            [False] * num_of_columns for x in range(num_of_rows)]

    def get_beats_per_minute(self):
        return self.get_current_pattern_dict()['beats_per_minute']

    def set_beats_per_minute(self):
        self.get_current_pattern_dict(
        )['beats_per_minute'] = self.beats_per_minute.get()

    def init_all_patterns(self):
        self.all_patterns = [
            {
                'list_of_drum_files': [None] * MAX_NUMBER_OF_DRUM_SAMPLES,
                'number_of_units': INITIAL_NUMBER_OF_UNITS,
                'bpu': INITIAL_BPU,
                'beats_per_minute': INITIAL_BEATS_PER_MINUTE,
                'is_button_clicked_list':
                self.init_is_button_clicked_list(
                    MAX_NUMBER_OF_DRUM_SAMPLES,
                    INITIAL_NUMBER_OF_UNITS * INITIAL_BPU
                )
            }
            for k in range(MAX_NUMBER_OF_PATTERNS)]

    def init_is_button_clicked_list(self, num_of_rows, num_of_columns):
        return [[False] * num_of_columns for x in range(num_of_rows)]

    def on_pattern_changed(self):
        pass

    def on_number_of_units_changed(self):
        self.set_number_of_units()
        self.set_is_button_clicked_list(MAX_NUMBER_OF_DRUM_SAMPLES,
                                        self.find_number_of_columns())
        self.create_right_button_matrix()

    def on_bpu_changed(self):
        self.set_bpu()
        self.set_is_button_clicked_list(MAX_NUMBER_OF_DRUM_SAMPLES,
                                        self.find_number_of_columns())
        self.create_right_button_matrix()

    def on_open_file_button_clicked(self, drum_index):
        def event_handler():
            file_path = filedialog.askopenfilename(defaultextension=".wav",
                                                   filetypes=[("Wave Files", "*.wav"), ("OGG Files", "*.ogg")])
            if not file_path:
                return
            self.set_drum_file_path(drum_index, file_path)
            self.display_all_drum_file_names()
        return event_handler

    def display_all_drum_file_names(self):
        for i, drum_name in enumerate(self.get_list_of_drum_files()):
            self.display_drum_name(i, drum_name)

    def display_drum_name(self, text_widget_num, file_path):
        if file_path is None:
            return
        drum_name = os.path.basename(file_path)
        self.drum_load_entry_widget[text_widget_num].delete(0, END)
        self.drum_load_entry_widget[text_widget_num].insert(0, drum_name)

    def on_play_button_clicked(self):
        pass

    def on_stop_button_clicked(self):
        pass

    def on_loop_button_toggled(self):
        pass

    def on_beats_per_minute_changed(self):
        pass

    def get_button_value(self, row, col):
        return self.all_patterns[self.current_pattern.get()][
            'is_button_clicked_list'][row][col]

    def find_number_of_columns(self):
        return self.number_of_units.get() * self.bpu.get()

    def process_button_clicked(self, row, col):
        self.set_button_value(row, col, not self.get_button_value(row, col))
        self.display_button_color(row, col)

    def set_button_value(self, row, col, bool_value):
        self.all_patterns[self.current_pattern.get()][
            'is_button_clicked_list'][row][col] = bool_value

    def on_button_clicked(self, row, col):
        def event_handler():
            self.process_button_clicked(row, col)
        return event_handler

    def display_all_button_colors(self):
        number_of_columns = self.find_number_of_columns()
        for r in range(MAX_NUMBER_OF_DRUM_SAMPLES):
            for c in range(number_of_columns):
                self.display_button_color(r, c)

    def display_button_color(self, row, col):
        bpu = self.bpu.get()
        original_color = COLOR_1 if ((col//bpu) % 2) else COLOR_2
        button_color = BUTTON_CLICKED_COLOR if self.get_button_value(
            row, col) else original_color
        self.buttons[row][col].config(background=button_color)

    def create_play_bar(self):
        playbar_frame = Frame(self.root, height=15)
        start_row = MAX_NUMBER_OF_DRUM_SAMPLES + 10
        playbar_frame.grid(row=start_row, columnspan=13,
                           sticky=W + E, padx=15, pady=10)
        self.play_icon = PhotoImage(file="images/play.gif")
        self.play_button = Button(playbar_frame, text='Play',  image=self.play_icon,
                                  compound='left', command=self.on_play_button_clicked)
        self.play_button.grid(row=start_row, column=1, padx=2)
        Button(playbar_frame, text='Stop', command=self.on_stop_button_clicked).grid(
            row=start_row, column=3, padx=2)
        self.to_loop.set(True)
        Checkbutton(playbar_frame, text='Loop', variable=self.to_loop,
                    command=self.on_loop_button_toggled).grid(row=start_row, column=16, padx=5)
        Label(playbar_frame, text='Beats Per Minute').grid(
            row=start_row, column=25)
        self.beats_per_minute.set(INITIAL_BEATS_PER_MINUTE)
        Spinbox(playbar_frame, from_=MIN_BEATS_PER_MINUTE, to=MAX_BEATS_PER_MINUTE, width=5,
                textvariable=self.beats_per_minute, increment=5.0, command=self.on_beats_per_minute_changed).grid(row=start_row, column=30)
        photo = PhotoImage(file='images/signature.gif')
        label = Label(playbar_frame, image=photo)
        label.image = photo
        label.grid(row=start_row, column=50, padx=1, sticky='w')

    def create_right_button_matrix(self):
        right_frame = Frame(self.root)
        right_frame.grid(row=10, column=6, sticky=W +
                         E + N + S, padx=15, pady=4)
        self.buttons = [[None for x in range(
            self.find_number_of_columns())] for x in range(MAX_NUMBER_OF_DRUM_SAMPLES)]
        for row in range(MAX_NUMBER_OF_DRUM_SAMPLES):
            for col in range(self.find_number_of_columns()):
                self.buttons[row][col] = Button(
                    right_frame, command=self.on_button_clicked(row, col))
                self.buttons[row][col].grid(row=row, column=col)
                self.display_button_color(row, col)

    def create_left_drum_loader(self):
        left_frame = Frame(self.root)
        left_frame.grid(row=10, column=0, columnspan=6, sticky=W + E + N + S)
        open_file_icon = PhotoImage(file='images/openfile.gif')
        for i in range(MAX_NUMBER_OF_DRUM_SAMPLES):
            open_file_button = Button(left_frame, image=open_file_icon,
                                      command=self.on_open_file_button_clicked(i))
            open_file_button.image = open_file_icon
            open_file_button.grid(row=i, column=0,  padx=5, pady=4)
            self.drum_load_entry_widget[i] = Entry(left_frame)
            self.drum_load_entry_widget[i].grid(
                row=i, column=4, padx=7, pady=4)

    def create_top_bar(self):
        topbar_frame = Frame(self.root, height=25)
        topbar_frame.grid(row=0, columnspan=12, rowspan=10, padx=5, pady=5)

        Label(topbar_frame, text='Pattern Number:').grid(row=0, column=1)
        self.current_pattern.set(0)
        Spinbox(topbar_frame, from_=0, to=MAX_NUMBER_OF_PATTERNS - 1, width=5,
                textvariable=self.current_pattern, command=self.on_pattern_changed).grid(row=0, column=2)

        self.current_pattern_name_widget = Entry(topbar_frame)
        self.current_pattern_name_widget.grid(row=0, column=3, padx=7, pady=2)

        Label(topbar_frame, text='Number of Units:').grid(row=0, column=4)
        self.number_of_units.set(INITIAL_NUMBER_OF_UNITS)
        Spinbox(topbar_frame, from_=1, to=MAX_NUMBER_OF_UNITS, width=5,
                textvariable=self.number_of_units, command=self.on_number_of_units_changed).grid(row=0, column=5)

        Label(topbar_frame, text='BPUs:').grid(row=0, column=6)
        self.bpu.set(INITIAL_BPU)
        Spinbox(topbar_frame, from_=1, to=MAX_BPU, width=5, textvariable=self.bpu,
                command=self.on_bpu_changed).grid(row=0, column=7)

    def init_gui(self):
        self.create_top_bar()
        self.create_left_drum_loader()
        self.create_right_button_matrix()
        self.create_play_bar()


if __name__ == '__main__':
    root = Tk()
    DrumMachine(root)
    root.mainloop()
