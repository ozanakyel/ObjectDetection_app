import datetime
import os
import cv2

imageSaveLocation = r"C:\Users\Harun\Desktop\imagesave"
serverLogLocation = r"C:\Users\Harun\Desktop\serverlog"

def log_for_plc_bit_change(log_array):
    path = str(datetime.date.today()) + '.txt'
    direction =  os.path.join(str(serverLogLocation), path)
    # for keys in log_array:
    for item in range(len(log_array["type"])):
        print(log_array["type"][item])
        print(log_array["content"][item])
        if not os.path.exists(direction):
            with open( direction , 'w+') as f:
                f.write('{:<35}'.format("Type"))
                f.write('{:<35}'.format("Log"))
                f.write("Date")
                f.write('\n')
                f.write('{:-^105}'.format("-"))
                f.write("\n")
                f.write('{:<35}'.format(log_array["type"][item]))
                f.write('{:<35}'.format(log_array["content"][item]))
                f.write(str(datetime.datetime.now()).replace(" ", "_").replace(".",":"))
                f.write('\n')
                f.close()
        else:
            with open( direction , 'a') as f:
                f.write('{:<35}'.format(log_array["type"][item]))
                f.write('{:<35}'.format(log_array["content"][item]))
                f.write(str(datetime.datetime.now()).replace(" ", "_").replace(".",":"))
                f.write('\n')
                f.close()
                f.close()

# log_array = {"type": [],"content": []}
# log_array["type"].append("info")
# log_array["content"].append(str("Sonuç degisti -**- "))
# log_array["type"].append("info")
# log_array["content"].append(str("PLC'den okunan deger: " + str(True)))
# log_array["type"].append("info")
# log_array["content"].append(("Detection sonucu: " + str(False)))
# #LOG
# log_for_plc_bit_change(log_array)
# ###########
DB = 90
DBX = 4
value = True
log_array = {"type": [],"content": []}
log_array["type"].append("info")
log_array["content"].append(str(f"DB{DB} . DBX{DBX} adresine {value} yazılmıştır."))
print(log_array)