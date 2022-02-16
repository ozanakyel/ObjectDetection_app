"""import snap7

PlcIp = '10.15.221.254'
PlcRack = 0
PlcSlot = 0
PlcCpu = 30
IstasyonDB = 'DB90'
IstasyonDB = int(IstasyonDB[2:])
OperasyonBasladiDB = 'DBX0.0'
OperasyonTamamlandiDB = 'DBX0.1'

plc = snap7.client.Client()
plc.connect(PlcIp, PlcRack, PlcSlot)
reading = plc.db_read(90, 0, 2)
name = reading[0:256].decode('UTF-8').strip('\x00')
print(reading)"""
import time
import threading
import snap7.util
from .log_functions import log_for_plc_bit_change
# LOG
log_array = {"type": [],"content": []}
log_array["type"].append("debug")
log_array["content"].append(str("plc.py Kutuphaneleri Yuklendi"))
log_for_plc_bit_change(log_array)
####################
class Plc(object):
    def __init__(self, PlcIP, PlcRack, PlcSlot):
        self.bit_value = True
        self.client = snap7.client.Client()
        self.client.connect(PlcIP, PlcRack, PlcSlot)
        if self.client.get_connected():
            # LOG
            log_array = {"type": [],"content": []}
            log_array["type"].append("info")
            log_array["content"].append(str(f"IP: {PlcIP} . Rack{PlcRack} . Slot{PlcSlot} PLC sine basariyla baglandi."))
            log_for_plc_bit_change(log_array)
            print(f"IP: {PlcIP} . Rack{PlcRack} . Slot{PlcSlot} PLC sine basariyla baglandi.")
            ####################
        else:
            # LOG
            log_array = {"type": [],"content": []}
            log_array["type"].append("error")
            log_array["content"].append(str(f"IP: {PlcIP} . Rack{PlcRack} . Slot{PlcSlot} PLC sine baglanirken hata olustu."))
            log_for_plc_bit_change(log_array)
            print(f"IP: {PlcIP} . Rack{PlcRack} . Slot{PlcSlot} PLC sine baglanirken hata olustu.")
            ####################

    def Read_Byte(self, DB, DBX):
        try:
            buffer = self.client.db_read(DB, DBX, 1)
            # buffer -> type= byte array -> ascii -> string
            buffer_value = ord(buffer[0:256].decode('UTF-8'))  # only client.db_read(X, X, count) count =1
            return buffer_value , buffer     # string list
        except:
            # LOG
            log_array = {"type": [],"content": []}
            log_array["type"].append("error")
            log_array["content"].append(str(f"DB{DB}.DBX{DBX} adresinden byte okunurken hata verdi."))
            log_for_plc_bit_change(log_array)
            print(f"DB{DB}.DBX{DBX} adresinden byte okunurken hata verdi.")
            ####################
        # def write_byte(db_num, start_byte, byte_value):  # Byte yazma
        #     data = bytearray(1)
        #     snap7.util.set_byte(data, 0, byte_value)
        #     plc.db_write(db_num, start_byte, data)

    def Set_Byte(self, DB, DBX, value):
        try:
            data = bytearray(1)
            snap7.util.set_byte(data, 0, value)
            self.client.db_write(DB, DBX, data)
            # LOG
            log_array = {"type": [],"content": []}
            log_array["type"].append("info")
            log_array["content"].append(str(f"DB{DB} . DBX{DBX} adresine {value} yazilmistir."))
            log_for_plc_bit_change(log_array)
            print(f"DB{DB} . DBX{DBX} adresine {value} yazilmistir.")
            ####################
            result = True
        except:
            # LOG
            log_array = {"type": [],"content": []}
            log_array["type"].append("error")
            log_array["content"].append(str(f"DB{DB} . DBX{DBX} adresine yazma islemi basarisiz oldu."))
            log_for_plc_bit_change(log_array)
            print(f"DB{DB} . DBX{DBX} adresine yazma islemi basarisiz oldu.")
            ####################
            result = False
        return result


    def Read_Bit(self, DB, DBX, DB_X,pause):
        while True:
            try:
                buffer = self.client.db_read(DB, DBX, 1)
                byte_value = snap7.util.get_bool(buffer, 0, DB_X)
                self.bit_value = byte_value   # bool
                time.sleep(pause)
            except:
                # LOG
                log_array = {"type": [],"content": []}
                log_array["type"].append("error")
                log_array["content"].append(str(f"DB{DB}.DBX{DBX}.{DB_X} adresinden bit okunurken hata verdi."))
                log_for_plc_bit_change(log_array)
                print(f"DB{DB}.DBX{DBX}.{DB_X} adresinden bit okunurken hata verdi.")
                ####################


    def Set_bit(self, DB, DBX, DB_X, value):
        try:
            _,data = self.Read_Byte(DB,DBX)
            snap7.util.set_bool(data, 0, DB_X, value)
            self.client.db_write(DB, DBX, data)
            # LOG
            log_array = {"type": [],"content": []}
            log_array["type"].append("info")
            log_array["content"].append(str(f"DB{DB}.DBX{DBX}.{DB_X} {value} olarak adresi setlenmistir."))
            log_for_plc_bit_change(log_array)
            print(f"DB{DB}.DBX{DBX}.{DB_X} {value} olarak adresi setlenmistir.")
            ####################
            result = True
        except:
            # LOG
            log_array = {"type": [],"content": []}
            log_array["type"].append("error")
            log_array["content"].append(str(f"DB{DB}.DBX{DBX}.{DB_X} adresine setleme yapilamadi."))
            log_for_plc_bit_change(log_array)
            print(f"DB{DB}.DBX{DBX}.{DB_X} adresine setleme yapilamadi.")
            ####################
            result = False
        return result


if __name__ =="__main__":
    PLC = Plc('10.15.221.254', PlcRack=0, PlcSlot=1)
    time.sleep(2)
    PLC.Set_bit( DB=90, DBX=4, DB_X = 1, value=True)

