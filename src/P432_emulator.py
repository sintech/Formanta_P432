# Formanta P432 Emulator
#
# Software emulation of Formanta P432 wavetable synthesizer
# The original Formanta P432 synthesizer was created by
# engineer Alexander Reunov and designer Andrey Petukhov
#
# Copyright (c) 2019 Konstantin Fedorov <sintechs@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

from tkinter import Tk, Toplevel, Button, Label, Frame, Canvas, EventType
from tkinter import messagebox, ttk
from threading import Thread
import pyaudio, struct, time
from P432 import P432

try:
    import rtmidi, rtmidi.midiutil
    no_midi = False
except ImportError:
    no_midi = True
    print("no midi :(")

p432 = P432()


class P432GUI:
    t1 = None
    prog = 0
    unison = False
    dig1 = 0
    dig2 = 0
    
    filter = False
    keypressed = []
    """ high:
        q2w3er5t6y7ui9o0p[=]\-
        c+d+ef+g+a+bc+d+ef+g+a
        low:
        zsxdcvgbhnjm,l.;/
        c+d+ef+g+a+bc+d+e"""
    key2piano = {'low': "zsxdcvgbhnjm,l.;/", 'high': "q2w3er5t6y7ui9o0p[=]\\-"}
    stop = False
    
    def __init__(self, master):
        self.master = master
        master.title("Форманта П-432 Emulator by SinTech 2019 v0.3")
        master.resizable(False, False)
        
        # root.geometry("640x480")
        self.l1 = Label(bg="lightgreen", height=2, text="Форманта П-432 emulator", font=("Arial", 15))
        self.l1.pack(expand=1, fill='x', anchor='n')
        
        f1 = Frame(root, bd=5, height=40)
        f1.pack(fill='x', side='top', padx=10, anchor='nw')
        for i in range(4):
            Button(f1, text=f" {i} ", command=lambda c=i: self.progbutton(f"1:{c}")).pack(side='left')
        self.progl = Label(f1, font=("Arial Rounded MT", 40), text="00", fg='red', bg='black')
        self.progl.pack(side='left', padx=10)
        for i in range(8):
            Button(f1, text=f" {i} ", command=lambda c=i: self.progbutton(f"2:{c}")).pack(side='left')
        
        self.unib = Button(f1, text="Унисон", command=lambda: self.progbutton("3:U"))
        self.unib.pack(padx=(20, 20), side='left')
        
        self.filtb = Button(f1, text="Фильтр", command=lambda: self.progbutton("3:F"))
        self.filtb.pack(padx=(20, 20), side='left')
        
        if not no_midi:
            self.midi_button = Button(f1, text="Midi In", command=lambda: self.select_midi_in_dialog())
            self.midi_button.pack(side='left')
        
        # Button(f1, text="Start", command=lambda: self.startplay()).pack(side='left')
        # Button(f1, text="Stop", command=lambda: self.stopplay()).pack(side='left')
        
        f3 = Frame(root)
        f3.pack(fill='x', side='top', padx=10)
        
        toolbar_frame = Frame(root)
        toolbar_frame.pack(side='top', fill='x', padx=5)
        # Button(toolbar_frame, text="Клавиатура", command=lambda: [self.key_help.pack(),self.prog_table.pack_forget() ]).pack(side=RIGHT,padx=5)
        # Button(toolbar_frame, text="Тембры", command=lambda: [self.prog_table.pack(),self.key_help.pack_forget()] ).pack(side=RIGHT, padx=(90,5))
        
        self.prog_table = Frame(root)
        self.draw_timbres()
        self.prog_table.pack(pady=10)
        # self.prog_table.pack_forget()
        
        self.key_help = Canvas(root, height=180, width=580)
        self.key_help.pack(fill='x')
        self.draw_keys()
        # self.key_help.pack_forget()
        
        self.progbutton('3:F')
        self.changeprog(0)
        root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.startplay()
    
    def draw_timbres(self):
        # program table
        prognum = p432.data.prognum
        blank = [3, 5, 17, 23, 27, 35, 37]
        box = 0
        for num in prognum:
            proginfo = p432.data.program[num]
            if box % 8 == 0:
                f = Frame(self.prog_table)
                f.pack(fill='x', side='left')
            Label(f, width=15, text=f"{num:02d}   {proginfo['title']}", borderwidth=1, relief="solid",
                  anchor='w', ).pack(side='top')  # highlightbackground='red',highlightcolor='green',highlightthickness=2
            
            if num in blank:
                Label(f, width=15, text=f" ", borderwidth=1, relief="solid", anchor='w').pack(side='top')
                box += 1
                if num == 37:
                    Label(f, width=15, text=f" ", borderwidth=1, relief="solid", anchor='w').pack(side='top')
            box += 1
    
    def draw_keys(self):
        x = 46
        y = 135
        note_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        
        black_keys = [1, 3, 6, 8, 10, 13, 15, 18, 20]
        octave = p432.proginfo["config"]['FREQ_1'] - 2
        octaves = {'low': octave - 1, 'high': octave}
        for manual, keys in self.key2piano.items():
            for n, key in enumerate(keys):
                note = (note_list[n] if n < len(note_list) else note_list[n - 12])
                octave_num = (octaves[manual] if n < len(note_list) else octaves[manual] + 1)
                if n in black_keys:
                    posy = y - 42
                    posx = x - 22
                    # x += 3
                    fill = 'black'
                    fg = 'white'
                    note_txt = f"{note[0]}{octave_num}{note[1]}"
                else:
                    posy = y
                    posx = x
                    x += 45
                    fill = 'white'
                    fg = 'black'
                    note_txt = f" {note[0]}{octave_num}"
                if key == '-':
                    posx -= 112
                    posy -= 42
                self.key_help.create_rectangle(posx, posy, posx + 37, posy + 37, fill=fill)
                self.key_help.create_text(posx + 8, posy + 10, text=f"{key}", font=("Arial", 11), fill=fg)
                self.key_help.create_text(posx + 21, posy + 27, text=f"{note_txt}", font=("Arial", 13), fill='red')
            x = 10
            y = 50
    
    def key2midinote(self, key):
        midi_c = {'high': 48, 'low': 36}
        for manual in midi_c.keys():
            if key in self.key2piano[manual]:
                key_num = self.key2piano[manual].index(key)
                midi_note = midi_c[manual] + key_num
                # print(f"{key} -> {midi_note}")
                return midi_note
        return False
    
    def keyevent_cb(self, event):
        if not (event.char in self.key2piano['low'] or event.char in self.key2piano['high']):
            return
        if event.type is EventType.KeyPress and len(self.keypressed) < 4:
            if event.char not in self.keypressed:
                self.keypressed.append(event.char)
                p432.key_press(self.key2midinote(event.char))
                # print(f"Key {event.char} pressed")
                # print(self.keypressed)
        elif event.type is EventType.KeyRelease:
            if event.char in self.keypressed:
                self.keypressed.remove(event.char)
                p432.key_release(self.key2midinote(event.char))
                # print(f"Key {event.char} depressed")
                # print(self.keypressed)
    
    def on_closing(self):
        if messagebox.askokcancel("Выход", "Уже хотите выйти?"):
            self.stopplay()
            root.destroy()
    
    def switch_unison(self, unison):
        if unison:
            self.unib['bg'] = 'red'
        else:
            self.unib['bg'] = 'SystemButtonFace'
        p432.unison = unison
    
    def changeprog(self, prog):
        # global p432
        print("changed")
        p432.setprog(prog, (True if len(self.keypressed) == 0 else False))
        print(f"Uni={p432.unison}")
        self.unison = p432.unison
        self.switch_unison(self.unison)
        p432.filter_en = self.filter
        
        self.draw_keys()
        
        # self.filt_comm(1)
    
    def progbutton(self, button):
        (dig, num) = button.split(":")
        
        if dig == '1':
            self.dig1 = int(num)
        if dig == '2':
            self.dig2 = int(num)
        if dig == '3':
            if num == 'U':
                self.unison = 1 - self.unison
                self.switch_unison(self.unison)
                return
            if num == 'F':
                self.filter = 1 - self.filter
                if self.filter:
                    self.filtb['bg'] = 'green'
                else:
                    self.filtb['bg'] = 'SystemButtonFace'
                p432.filter_en = self.filter
                return
        
        old_prog = self.progl['text']
        self.prog = self.dig1 * 10 + self.dig2
        self.progl['text'] = f"{self.prog:02d}"
        if old_prog != self.prog:
            self.changeprog(self.prog)
    
    def startplay(self):
        self.l1['text'] = "Играйте клавишами клавиатуры!"
        self.t1 = Thread(target=self.play)
        self.t1.start()
        print("Started")
        root.bind("<KeyPress>", self.keyevent_cb)
        root.bind("<KeyRelease>", self.keyevent_cb)
    
    def stopplay(self):
        self.l1['text'] = "Форманта П-432 emulator"
        root.unbind("<KeyPress>")
        root.unbind("<KeyRelease>")
        self.stop = True
        if self.t1:
            self.t1.join()
        print("Stopped")
    
    def pyaudio_cb(self, in_data, frame_count, time_info, status):
        # print(f"fram count={frame_count}")
        data = bytearray()
        samples = p432.gen_samples(frame_count)
        for word in samples:
            data += (struct.pack('<h', (word - 2048) << 4))
        if self.stop:
            flag = pyaudio.paComplete
        else:
            flag = pyaudio.paContinue
        return bytes(data), flag
    
    def play(self):
        print("Playing")
        self.stop = False
        p = pyaudio.PyAudio()
        
        stream = p.open(format=pyaudio.paInt16, channels=1,
                        frames_per_buffer=200,
                        rate=33000,
                        output=True,
                        stream_callback=self.pyaudio_cb)
        
        stream.start_stream()
        while stream.is_active():
            time.sleep(0.1)
        stream.stop_stream()
        stream.close()
        p.terminate()
    
    def select_midi_in_dialog(self):
        top = Toplevel()
        top.transient(root)
        top.grab_set()
        top.title('Выберите MIDI вход')
        midiinput = rtmidi.MidiIn()
        ports = midiinput.get_ports()
        # print(ports)
        input = ttk.Combobox(top, state='readonly', values=['None'] + ports)
        input.current(0)
        input.pack(padx=20, pady=20)
        Button(top, justify="center", text="Okay", command=lambda: self.select_midi_in(top, input.get())).pack()
        self.windows_to_center(top)
    
    def select_midi_in(self, dialog, input):
        dialog.destroy()
        if input != "" and input != "None":
            try:
                self.midiin, port_name = rtmidi.midiutil.open_midiinput(input)
                print(f"Midi port '{port_name}' openend")
            except (EOFError, KeyboardInterrupt):
                print("Midi port Error")
                return
            self.midiin.set_callback(self.midi_handler(port_name))
            self.midi_button['bg'] = 'green'
            self.l1['text'] = "Играйте клавишами клавиатуры и MIDI!"
        else:
            try:
                if self.midiin.is_port_open():
                    print("Closing midi port")
                    self.l1['text'] = "Играйте клавишами клавиатуры!"
                    self.midiin.close_port()
            except AttributeError:
                pass
            self.midi_button['bg'] = 'SystemButtonFace'
    
    class midi_handler(object):
        def __init__(self, port):
            self.port = port
            self._wallclock = time.time()
        
        def __call__(self, event, data=None):
            message, deltatime = event
            self._wallclock += deltatime
            # print("[%s] @%0.6f %r" % (self.port, self._wallclock, message))
            midi_msg = message[0] >> 4
            midi_ch = (message[0] & 0B1111) + 1
            # Note-On
            if midi_msg == 9:
                if message[1] <= 83:
                    p432.key_press(message[1])
            # Note-Off
            elif midi_msg == 8:
                p432.key_release(message[1])
            # Program Change
            elif midi_msg == 12:
                if message[1] in p432.data.prognum:
                    print("Midi changed prog to {}".format(message[1]))
                    p432.setprog(message[1], True)
    
    def windows_to_center(self, thiswindow, pw=0, ph=0):
        if pw != 0 and ph != 0:
            thiswindow.geometry('{}x{}+{}+{}'.format(pw, ph, int(thiswindow.winfo_screenwidth() // 2 - (pw / 2)),
                                                     int(thiswindow.winfo_screenheight() // 2 - (ph / 2))))
        else:
            self.master.eval('tk::PlaceWindow {} center'.format(thiswindow))


root = Tk()
# root.eval('tk::PlaceWindow . center')
gui = P432GUI(root)
gui.windows_to_center(root)
root.mainloop()
