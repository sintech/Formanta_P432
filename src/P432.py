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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import wave, struct
import logging


# logging.basicConfig(level=logging.DEBUG)

class P432data:
    unitlen = 100  # base envelope unit len (100 R pulses)
    prognum = list(range(8)) + list(range(10, 18)) + list(range(20, 28)) + list(range(30, 38))
    
    program = {}
    for n in prognum:
        program[n] = {}
    
    # program[0]["tone"] = {"A4": 0x658, "A4u": 0x657 } # left=0x508, Right=0x788
    program[0]['title'] = 'ЭЛ. ПИАНО'
    # program[1]["tone"] = {"A4": 0x4d8, "A4u": 0x657} # sust decr
    program[1]['title'] = 'ДЖ. ПИАНО'
    # program[2]["tone"] = {"A4": 0x659, "A4u": 0x656} # long decay + sust decr
    program[2]['title'] = 'Ф. ПИАНО'
    # program[3]["tone"] = {"A4": 0x598, "A4u": 0x657} # syst decr
    program[3]['title'] = 'ПИАНО'
    # program[4]["tone"] = {"A4": 0x659, "A4u": 0x656} # const
    program[4]['title'] = 'ГАРМОНИКА'
    # program[5]["tone"] = {"A4": 0x597, "A4u": 0x599} # const
    program[5]['title'] = 'АККОРДЕОН'
    # program[6]["tone"] = {"A4": 0x598, "A4u": 0x597} # const
    program[6]['title'] = 'ОРГАН'
    # program[7]["tone"] = {"A4": 0x4d8, "A4u": 0x657} # const
    program[7]['title'] = 'ДУХ. ОРГАН'
    
    # program[10]["tone"] = {"A4": 0x598, "A4u": 0x597} # const sust at D1 / T=100
    program[10]['title'] = 'ДЖ. ОРГАН'
    # program[11]["tone"] = {"A4": 0x658, "A4u": 0x659} # const sust at E1 / T=100 / Filter ???
    program[11]['title'] = 'Ф. ОРГАН'
    # program[12]["tone"] = {"A4": 0x658, "A4u": 0x657} # const sust at D1 / AT/RT=100 DT=400 / Filter ???
    program[12]['title'] = 'ХАММОНД 1'
    # program[13]["tone"] = {"A4": 0x4d8, "A4u": 0x657} # const / AT/RT=100
    program[13]['title'] = 'ХАММОНД 2'
    # program[14]["tone"] = {"A4": 0x4d8, "A4u": 0x4d7} # const sust at D1 / AT/RT=100 DT=400
    program[14]['title'] = 'СИНТ. ОРГАН'
    # program[15]["tone"] = {"A4": 0x598, "A4u": 0x597} # const sust at E1 / T=100 / Filter const=h60
    program[15]['title'] = 'БРАСС ОРГАН'
    # program[16]["tone"] = {"A4": 0x658, "A4u": 0x657}  # const sust at E1 / T=100 / Filter const=h60
    program[16]['title'] = 'БРАСС'
    # program[17]["tone"] = {"A4": 0x598, "A4u": 0x597} # const sust at E1 / AT/RT=100 DT=200 / Filter const=h08
    program[17]['title'] = 'ВАЛТОРНА'
    
    # program[20]["tone"] = {"A4": 0x658, "A4u": 0x657} # const
    program[20]['title'] = 'ФЛЕЙТА'
    # program[21]["tone"] = {"A4": 0x658, "A4u": 0x657} # const
    program[21]['title'] = 'ПИККОЛО'
    # program[22]["tone"] = {"A4": 0x658, "A4u": 0x657} # const E1
    program[22]['title'] = 'КЛАРНЕТ'
    # program[23]["tone"] = {"A4": 0x598, "A4u": 0x597} # const
    program[23]['title'] = 'ГОБОЙ'
    # program[24]["tone"] = {"A4": 0x598, "A4u": 0x599} # const
    program[24]['title'] = 'КОСМИК'
    # program[25]["tone"] = {"A4": 0x4d6, "A4u": 0x659} # const E1
    program[25]['title'] = 'ФАНТАСТИК'
    # program[26]["tone"] = {"A4": 0x659, "A4u": 0x657} # decr
    program[26]['title'] = 'СЛАПСИНТ'
    # program[27]["tone"] = {"A4": 0x598, "A4u": 0x659} # const E1
    program[27]['title'] = 'БЛЮЗСИНТ'
    
    # program[30]["tone"] = {"A4": 0x4d8, "A4u": 0x597} # decr
    program[30]['title'] = 'КЛАВЕСИН'
    # program[31]["tone"] = {"A4": 0x4d8, "A4u": 0x598} # decr
    program[31]['title'] = 'КЛАВИНЕТ'
    # program[32]["tone"] = {"A4": 0x4d8, "A4u": 0x659} # decr
    program[32]['title'] = 'ХАРПСИ'
    # program[33]["tone"] = {"A4": 0x4d9, "A4u": 0x4d7} # decr
    program[33]['title'] = 'ЭЛ. БАС'
    # program[34]["tone"] = {"A4": 0x4d8, "A4u": 0x4d7} # decr
    program[34]['title'] = 'ДЖ. БАС'
    # program[35]["tone"] = {"A4": 0x4d9, "A4u": 0x4d7} # decr
    program[35]['title'] = 'БАС'
    # program[36]["tone"] = {"A4": 0x659, "A4u": 0x657} # no sustain
    program[36]['title'] = 'МУЗ. БОКС'
    # program[37]["tone"] = {"A4": 0x598, "A4u": 0x597} # decr
    program[37]['title'] = 'СИНТ. БАС'
    
    def __init__(self, prog):
        self.prog = prog
        try:
            self.load_progconfig()
            self.loadroms()
        except FileNotFoundError:
            print("""The following P432 binary ROMs have to be in roms/ dir!
1. DD1.BIN, DD2.BIN - freq
2. DD13.BIN, DD14.BIN, DD18.BIN, DD19.BIN - wavetables
3. DD27.BIN, DD28.BIN - scaling
4. DD16.BIN - cpu""")
            exit()
    
    def loadroms(self):
        dd1 = open("roms/DD1.BIN", "rb")
        dd2 = open("roms/DD2.BIN", "rb")
        freq_rom = []
        for byte in range(2048):
            freq_rom.append(
                int.from_bytes(dd2.read(1), byteorder='big') << 8 | int.from_bytes(dd1.read(1), byteorder='big'))
        # print(freq_rom)
        self.freq_rom = freq_rom
        
        # wave rom
        waveroms = {0: ["DD13.BIN", "DD14.BIN"], 1: ["DD18.BIN", "DD19.BIN"]}
        wave_rom = []
        for (rom1, rom2) in waveroms.values():
            rom1_data = open('roms/' + rom1, "rb")
            rom2_data = open('roms/' + rom2, "rb")
            for byte in range(2048):
                byte1 = int.from_bytes(rom1_data.read(1), byteorder='big')
                byte2 = int.from_bytes(rom2_data.read(1), byteorder='big')
                wave_rom.append(byte2 << 8 | byte1)
        # print(sample_rom)
        
        offset = self.getwaveoffset(self.prog)
        self.wave_rom = wave_rom[offset:offset + 2049]
        
        # scaling rom
        dd27 = open("roms/DD27.BIN", "rb")
        dd28 = open("roms/DD28.BIN", "rb")
        self.volume_rom27 = list(dd27.read())
        self.volume_rom28 = list(dd28.read())
    
    def load_progconfig(self):
        rom = open("roms/DD16.BIN", "rb")
        rom.seek(0x400)
        bytename = {}
        
        bytename[0] = "FA_min"
        bytename[1] = "FA_dt"
        bytename[2] = "FA_max"
        bytename[4] = "FD_ft"  # ???
        bytename[5] = "FD_dt"
        bytename[6] = "FS_lvl"
        bytename[8] = "FS_ft"  # roughly 00=?, 10=*16, 40=*4
        bytename[9] = "FS_dt"  # ==0=-1dt, >0=-ndt
        bytename[10] = "FR_ft"
        bytename[11] = "FR_dt"  # 0=-1?
        
        bytename[15] = "Ctrl"
        bytename[16] = "A_min"  # TA
        bytename[17] = "A_dt"  # TA
        bytename[18] = "A_max"  # TA
        bytename[20] = "D_ft"  # 00=100, 0x80=200, 0x40=400, 0x20=800 Rs
        bytename[21] = "D_dt"  # TD 0=-1? (A_max<>Sustain)
        bytename[22] = "S_lvl"  # or D_end?,  sustain decrease always? = 1
        bytename[24] = "S_ft"  # 00=const, 40=400, 20=800 Rs
        bytename[27] = "R_dt"
        
        bytename[7] = "FREQ_u1"
        bytename[14] = "FREQ_u2"
        bytename[30] = "FREQ_1"
        bytename[31] = "FREQ_2"
        
        for prog in self.prognum:
            params = list(rom.read(32))
            # print names
            self.program[prog]['config'] = {}
            for (n, byte) in enumerate(params):
                if n in bytename:
                    self.program[prog]['config'][bytename[n]] = byte
    
    @classmethod
    def getprog(self, prog):
        return self.program[prog]
    
    @classmethod
    def getwaveoffset(self, prog):
        # Bank
        S0 = self.program[prog]['config']["Ctrl"] & 1
        S1 = self.program[prog]['config']["Ctrl"] >> 1 & 1
        S2 = self.program[prog]['config']["Ctrl"] >> 2 & 1
        
        wave_rom_offset = S2 * 2048 + S1 * 1024 + S0 * 512
        return wave_rom_offset
    
    @classmethod
    def getA4freq(self, prog):
        config = self.program[prog]['config']
        # delta between config value and A4 note value
        freq_offset = {4: 0xd0, 5: 0x90, 6: 0x50}
        # fundamental freq
        freq = (config['FREQ_1'] << 8) + freq_offset[config['FREQ_1']] + config['FREQ_2']
        # unison freq
        freq_u = (config['FREQ_u1'] << 8) + freq_offset[config['FREQ_u1']] + config['FREQ_u2']
        return freq, freq_u


class P432:
    """P432 emu"""
    filt_freq = 0.99
    filt_q = 0.8
    finetune = -5
    
    def __init__(self):
        self.setprog(00)
    
    def midi2freq(self, note):
        # left=36, right=76, A4=57
        freq = P432data.getA4freq(self.prog)[0] - (57 - note) * 16 + self.finetune
        freq_uni = P432data.getA4freq(self.prog)[1] - (57 - note) * 16 + self.finetune
        return freq, freq_uni
    
    def setprog(self, prog, clean=True):
        self.prog = prog
        self.proginfo = P432data.program[self.prog]
        self.data = P432data(prog)
        if clean:
            self.freq_in = [0] * 8
            self.keystate = [{'note': 0, 'state': 0}] * 4  # note: midinote; state: 0-mute, 1-playing, 2-release
        else:
            self.recalculate_freqs()
        # gen envelopes
        self.ADSenvelope = self.getADS()
        self.FADSenvelope = self.getFADS()
        if clean:
            self.env = [{'env': self.ADSenvelope, 'pos': 0} for n in range(4)]
            self.fenv = {'env': self.FADSenvelope, 'pos': 0}
            self.buffer = [0] * 8
            self.filt_buf = [0] * 5
        self.unison = 1 - (self.proginfo["config"]['Ctrl'] >> 7 & 1)
        self.filter_en = True
    
    def getftu(self, ft):
        """
        Calculate number of data units based on *_ft config parameter.
        Output already multiplied by unitlen.
        :param ft: *_ft config value
        :return:
        """
        ftunits = 1 if ft == 0 else int(256 / ft)
        return ftunits * self.data.unitlen
    
    @staticmethod
    def getRange(from_, to, delta):
        list = [from_]
        while (from_ < to and delta > 0) or (from_ > to and delta < 0):
            if (from_ + delta > to and delta > 0) or (from_ + delta < to and delta < 0):
                list.append(to)
                break
            list.append(from_ + delta)
            from_ += delta
        return list
    
    def getADS(self):
        config = self.proginfo["config"]
        # print(config)
        envelope = []
        # Attack
        logging.info(f"Attack: {config['A_min']} to {config['A_max']} by {config['A_dt']}")
        for vol in range(config['A_min'], config['A_max'], config['A_dt']):
            envelope.extend([vol] * self.getftu(0))
        # Decay
        if config['A_max'] != config['S_lvl']:
            D_dt = 1 if config['D_dt'] == 0 else config['D_dt']
            logging.info(
                f"Decay: {config['A_max']} to {config['S_lvl']} by {-D_dt} every {self.getftu(config['D_ft'])} units")
            for vol in range(config['A_max'], config['S_lvl'] - D_dt, -D_dt):
                envelope.extend([vol] * self.getftu(config['D_ft']))
        else:
            logging.info(f"Decay: none")
        # Sustain
        if config['S_ft'] > 0:
            # decrease
            logging.info(f"Sustain: {config['S_lvl'] - 1} to {0} by {-1}")
            for vol in range(config['S_lvl'] - 1, -1, -1):
                envelope.extend([vol] * self.getftu(config['S_ft']))
        else:
            # const
            logging.info(f"Sustain: const={config['S_lvl']}")
            envelope.extend([config['S_lvl']] * self.getftu(0))
        
        return envelope
    
    def getFADS(self):
        config = self.proginfo["config"]
        envelope = []
        
        # hardcode
        if self.prog == 2:
            return [config['FA_max']] * self.getftu(0)
        if self.prog in [6, 7, 15, 16]:
            config['FS_lvl'] = config['FA_max']
        if self.prog == 35:
            config['FS_ft'] = 0
        # prefix
        if self.prog in [5, 6, 7] + [10, 15, 17] + list(range(20, 28)) + [33]:
            envelope.extend([0] * self.getftu(0))
        
        # Attack
        if config['FA_max'] > 0:
            logging.info(f"F-Attack: {config['FA_min']} to {config['FA_max']} by {config['FA_dt']}")
            for filt in range(config['FA_min'], config['FA_max'], config['FA_dt']):
                envelope.extend([filt] * self.getftu(0))
        else:
            envelope.extend([0] * self.getftu(0))
            return [0]
        # Decay
        if config['FA_max'] != config['FS_lvl']:
            FD_dt = 1 if config['FD_dt'] == 0 else config['FD_dt']
            logging.info(
                f"F-Decay: {config['FA_max']} to {config['FS_lvl']} by {-FD_dt} every {self.getftu(config['FD_ft'])} units")
            for filt in self.getRange(config['FA_max'], config['FS_lvl'], -FD_dt):
                envelope.extend([filt] * self.getftu(config['FD_ft']))
        else:
            logging.info(f"F-Decay: none")
        # Sustain
        if config['FS_ft'] > 0 or config['FS_dt'] > 0:
            # decrease
            FS_lvl = config['FS_lvl']
            FS_dt = 1 if config['FS_dt'] == 0 else config['FS_dt']
            logging.info(f"F-Sustain: {FS_lvl - 1} to {0} by {-FS_dt}")
            for filt in self.getRange(FS_lvl - FS_dt, 0, -FS_dt):  # range(FS_lvl-1,-1,-FS_dt)
                envelope.extend([filt] * self.getftu(config['FS_ft']))
        else:
            # const
            logging.info(f"F-Sustain: const={config['FS_lvl']}")
            envelope.extend([config['FS_lvl']] * self.getftu(0))
        
        return envelope
    
    def getR(self, level):
        config = self.proginfo["config"]
        envelope = []
        
        # Release
        logging.info(f"Release: {level} to {0} by {config['R_dt']}")
        for vol in range(level - config['R_dt'], 0, -config['R_dt']):
            envelope.extend([vol] * self.getftu(0))
        envelope.extend([0] * self.getftu(0))
        return envelope
    
    def getFR(self, level):
        config = self.proginfo["config"]
        envelope = []
        
        # hardcode
        if self.prog == 2:
            return [config['FA_max']] * self.getftu(0)
        
        # Release
        logging.info(f"F-Release: {level} to {0} by {config['FR_dt']}")
        FR_dt = 1 if config['FR_dt'] == 0 else config['FR_dt']
        for filt in range(level - FR_dt, 0, -FR_dt):
            envelope.extend([filt] * self.getftu(config['FR_ft']))
        envelope.extend([0] * self.getftu(0))
        return envelope
    
    def key_press(self, midi_note):
        idx = -1
        note_info = next(((n, item) for n, item in enumerate(self.keystate) if item["note"] == midi_note), False)
        if note_info:
            # old key
            idx = note_info[0]
        else:
            # new keypress
            for n, item in enumerate(self.keystate):
                if item['state'] != 1:
                    idx = n
                    break
            if idx == -1:
                logging.info("no free note slots :((")
                return False
        self.keystate[idx] = {'note': midi_note, 'state': 1}
        self.env[idx]['env'] = self.ADSenvelope
        self.env[idx]['pos'] = 0
        self.fenv['env'] = self.FADSenvelope
        self.fenv['pos'] = 0
        
        self.recalculate_freqs()
    
    def recalculate_freqs(self):
        # recalculate freq table
        for n, info in enumerate(self.keystate):
            # print(n, info)
            if info['state'] in [1, 2]:
                self.freq_in[n * 2] = self.midi2freq(info['note'])[0]
                # print(f"{self.midi2freq(info['note'])[0]:X}")
                if self.unison:
                    self.freq_in[n * 2 + 1] = self.midi2freq(info['note'])[1]
    
    def key_release(self, midi_note):
        # note release
        n = next((n for (n, item) in enumerate(self.keystate) if item["note"] == midi_note), False)
        if n is not False:
            self.keystate[n] = {'note': midi_note, 'state': 2}
            # get current volume for release
            if self.env[n]['pos'] < len(self.env[n]['env']):
                volume = self.env[n]['env'][self.env[n]['pos']]
            else:
                volume = self.env[n]['env'][-1]
            self.env[n]['env'] = self.getR(volume)
            self.env[n]['pos'] = 0
        
        # filter release (last key has released)
        if not next((item for item in self.keystate if item["state"] == 1), False):
            # get current filter level for release
            if self.fenv['pos'] < len(self.fenv['env']):
                freq = self.fenv['env'][self.fenv['pos']]
            else:
                freq = self.fenv['env'][-1]
            self.fenv['env'] = self.getFR(freq)
            self.fenv['pos'] = 0
    
    def gen_samples(self, sample_count):
        # Steps:
        # 1. phase accumulator
        # 2. read wavetable
        # 3. add volume
        # 4. sum voices
        # 5. DAC out
        
        freq_data_out = 0
        
        samples_out = []
        dac_data_out_sum = 0
        for sample in range(sample_count):
            for addr, freq in enumerate(self.freq_in):
                # freq = self.freq_in[addr]
                freq_data_in = self.data.freq_rom[freq]
                # phase accumulator
                if addr % (1 if self.unison else 2) == 0:
                    data_buff = self.buffer[addr]
                    self.buffer[addr] = (freq_data_in + data_buff) & ((1 << 20) - 1)
                    freq_data_out = self.buffer[addr] >> 11
                    # print(cycle)
                    # print(buffer)
                # print(f"Out= {(buffer[buffer_idx] >> 11):x}")
                
                # read wavetable
                wave_out = self.data.wave_rom[freq_data_out]
                wave_data = wave_out & ((1 << 10) - 1)
                bit10 = wave_out >> 10
                # print(freq_data_out,wave_out)
                
                # volume calculation
                # note>0
                # env_pos<len(envelope) else if envelope[-1]>0 then vol=envelope[-1]
                #
                if self.freq_in[addr]:
                    voice = int(addr / 2)
                    # print(voice, len(self.env[voice]['env']),self.env[voice]['pos'])
                    if self.env[voice]['pos'] < len(self.env[voice]['env']):
                        volume_in = self.env[voice]['env'][self.env[voice]['pos']]
                    elif self.env[voice]['env'][-1] > 0:
                        volume_in = self.env[voice]['env'][-1]
                    else:
                        # if self.keystate[voice]['state']==2:
                        #     self.keystate[voice]['state']=0
                        volume_in = 0
                    # print(voice,volume_in)
                    self.env[voice]['pos'] += 1
                else:
                    volume_in = 0
                
                # add voulume
                plus_volume = wave_data + (volume_in << 2)
                plus_volume2 = plus_volume & ((1 << 11) - 1)
                
                # scaling
                if bit10:
                    scaled_data_out = self.data.volume_rom28[plus_volume2] + 256
                else:
                    scaled_data_out = self.data.volume_rom27[plus_volume2] + 1
                # print(f"{wave_data}, bit:{bit10}, plusv:{plus_volume}, v_out:{volume_data_out}")
                
                # sum voices
                dac_data_out = dac_data_out_sum + scaled_data_out
                dac_data_out_sum = dac_data_out & ((1 << 12) - 1)
                if addr == 7:
                    dac_data_out_sum = 0
                    if self.filter_en:
                        filter_out = self.res_filter(dac_data_out - 2048, self.filt_freq, self.filt_q) + 2048
                        samples_out.append(filter_out & ((1 << 12) - 1))
                    else:
                        samples_out.append(dac_data_out)
        
        return samples_out
    
    def res_filter(self, finput, freq, q_res):
        prog_f = self.proginfo["config"]['Ctrl'] >> 3 & 0b11
        f = 1 / 3 * prog_f
        if self.fenv['pos'] < len(self.fenv['env']):
            freq_in = self.fenv['env'][self.fenv['pos']]
        elif self.fenv['env'][-1] > 0:
            freq_in = self.fenv['env'][-1]
        else:
            freq_in = 0
        self.fenv['pos'] += 1
        f = f + (1 - f) / 255 * freq_in
        # scale
        f = (1 - freq) + (f * freq) + 0.042
        # clipping
        if f > 0.99:
            f = 0.99
        prog_q = self.proginfo["config"]['Ctrl'] >> 5 & 0b11
        q = 1 / 3 * prog_q
        # scale
        q = q * q_res
        # protection
        if prog_q > 0:
            q -= 0.01
        fb = q + q / (1.0 - f)
        # load
        buf0 = self.filt_buf[0]
        buf1 = self.filt_buf[1]
        buf0 = buf0 + f * (finput - buf0 + fb * (buf0 - buf1))
        buf1 = buf1 + f * (buf0 - buf1)
        # save
        self.filt_buf[0] = buf0
        self.filt_buf[1] = buf1
        return round(buf1)
    
    def write_wav(self, filename, samples):
        w = wave.open(filename, 'w')
        w.setparams((1, 2, 33000, 8000, 'NONE', 'not compressed'))
        w.setnframes(len(samples))
        for word in samples:
            packed_word = struct.pack('<h', (word - 2048) << 4)
            w.writeframesraw(packed_word)
        w.close()


# if __name__ == "__main__":
    # p432 = P432()
    # p432.setprog(00)
    # p432.unison = False
    # p432.filter_en = False
    # p432.key_press(57)
    # samples = p432.gen_samples(33000 * 4)
    # p432.key_release(57)
    # p432.write_wav('sound_00.wav',samples)
