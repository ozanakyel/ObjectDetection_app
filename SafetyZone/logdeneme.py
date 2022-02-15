import datetime
import os
import cv2

imageSaveLocation = r"C:\Users\Harun\Desktop\imagesave"
serverLogLocation = r"C:\Users\Harun\Desktop\serverlog"

def log_for_plc_bit_change(log_array):
    path = str(datetime.date.today()) + '.txt'
    direction =  os.path.join(str(serverLogLocation), path)
    for item in log_array:
        print(item)
        if not os.path.exists(direction):
            with open( direction , 'w+') as f:
                f.write('{:<35}'.format("Log"))
                f.write("Date")
                f.write('\n')
                f.write('{:-^70}'.format("-"))
                f.write("\n")
                f.write('{:<35}'.format(item))
                f.write(str(datetime.datetime.now()).replace(" ", "_").replace(".",":"))
                f.write('\n')
                f.close()
        else:
            with open( direction , 'a') as f:
                f.write('{:<35}'.format(item))
                f.write(str(datetime.datetime.now()).replace(" ", "_").replace(".",":"))
                f.write('\n')
                f.close()

log_array = []
log_array.append(str("Sonuç degisti -**- "))
log_array.append(str("PLC'den okunan deger: " + str(True)))
log_array.append(str("Detection sonucu : " + str(False)))
#LOG
log_for_plc_bit_change(log_array)
###########