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
class Plc(object):
    def __init__(self, PlcIP, PlcRack, PlcSlot, PlcCpu=None):
        self.bit_value = None
        self.client = snap7.client.Client()
        self.client.connect(PlcIP, PlcRack, PlcSlot)
        self.client.get_connected()
        # threading.Thread(target=self.Read_Bit, args=(90, 4, 1,1), daemon=True).start()

    def Read_Byte(self, DB, DBX):
        buffer = self.client.db_read(DB, DBX, 1)
        # buffer -> type= byte array -> ascii -> string
        buffer_value = ord(buffer[0:256].decode('UTF-8'))  # only client.db_read(X, X, count) count =1

        return buffer_value     # string list

        # def write_byte(db_num, start_byte, byte_value):  # Byte yazma
        #     data = bytearray(1)
        #     snap7.util.set_byte(data, 0, byte_value)
        #     plc.db_write(db_num, start_byte, data)

    def Set_Byte(self, DB, DBX, value):
        try:
            data = bytearray(1)
            snap7.util.set_byte(data, 0, value)
            self.client.db_write(DB, DBX, data)
            print(f"DB{DB} . DBX{DBX} adresine {value} yazılmıştır.")
            result = True
        except:
            print('PLC Byte yazma işlemi gerçekleştirilemedi')
            result = False
        return result


    def Read_Bit(self, DB, DBX, DB_X,pause):
        while True:
            buffer = self.client.db_read(DB, DBX, 1)
            byte_value = snap7.util.get_bool(buffer, 0, DB_X)
            self.bit_value =  byte_value   # bool
            time.sleep(pause)
            break

    def Set_bit(self, DB, DBX, DB_X, value):
        try:
            data = bytearray(1)
            snap7.util.set_bool(data, 0, DB_X, value)
            self.client.db_write(DB, DBX, data)
            print(f"DB{DB}.DBX{DBX}.{DB_X} {value} olarak adresi setlenmiştir.")

            result = True
        except:
            result = False
            print("PLC'ye setleme işlemi yapılamadı")
        return result

if __name__ =="__main__":
    PLC = Plc('10.15.221.254', PlcRack=0, PlcSlot=1,PlcCpu=30)
    while True:
        # #value = PLC.bit_value
        # PLC.Read_Bit( DB=90, DBX=4, DB_X = 1, pause=1)
        # value = PLC.bit_value
        # print(value)
        # time.sleep(1)
        PLC.Set_bit( DB=90, DBX=4, DB_X = 1, value=1)
        break

    # print(PLC.Set_Byte(90, 3, 78))
    # print(PLC.Read_Byte(90, 3))

    # client = snap7.client.Client()
    # client.connect('10.15.221.254', 0, 0)
    # client.get_connected()
    #
    # buffer = client.db_read(90, 3, 1)
    # # buffer -> type= byte array -> ascii -> string
    # value = ord(buffer[0:256].decode('UTF-8'))  # only client.db_read(X, X, count) count =1
    # print(value)