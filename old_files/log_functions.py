import datetime
import os
import cv2
from .log_for_frontend import Log

imageSaveLocation = r"C:\Users\Harun\Desktop\imagesave"
serverLogLocation = r"C:\Users\Harun\Desktop\serverlog"
log_frontend = Log()

def log_for_processed_image(image_orj, image_detected):
    image_name = str(datetime.datetime.now()).replace(" ", "_").replace(".",":") + '_detected' +'.jpg'
    image_name_orj = str(datetime.datetime.now()).replace(" ", "_").replace(".",":") +'.jpg'
    cv2.imwrite(os.path.join(imageSaveLocation, image_name_orj), image_orj)
    cv2.imwrite(os.path.join(imageSaveLocation, image_name), image_detected)
    # print(os.path.join(configs[50]['configValue'], image_name), 'olarak kaydedildi')
    path = str(datetime.date.today()) + '.txt'
    direction =  os.path.join(str(serverLogLocation), path)
    if not os.path.exists(direction):
        with open( direction , 'w+') as f:
            f.write(str(os.path.join(imageSaveLocation, image_name_orj)) + ' olarak kaydedildi')
            f.write('\n')
            f.write(str(os.path.join(imageSaveLocation, image_name)) + ' olarak kaydedildi')
            f.write('\n')
            f.close()
    else:
        with open( direction , 'a') as f:
            f.write(str(os.path.join(imageSaveLocation, image_name_orj)) + ' olarak kaydedildi')
            f.write('\n')
            f.write(str(os.path.join(imageSaveLocation, image_name)) + ' olarak kaydedildi')
            f.write('\n')
            f.close()

def log_for_plc_bit_change(log_array):
    path = str(datetime.date.today()) + '.txt'
    direction =  os.path.join(str(serverLogLocation), path)
    # for keys in log_array:
    for item in range(len(log_array["type"])):
        # print(log_array["type"][item])
        # print(log_array["content"][item])
        if not os.path.exists(direction):
            with open( direction , 'w+') as f:
                f.write('{:<10}'.format("Type"))
                f.write('{:<150}'.format("Log"))
                f.write("Date")
                f.write('\n')
                f.write('{:-^190}'.format("-"))
                f.write("\n")
                f.write('{:<10}'.format(log_array["type"][item]))
                f.write('{:<150}'.format(log_array["content"][item]))
                time = str(datetime.datetime.now()).replace(" ", "_").replace(".",":")
                f.write(time)
                f.write('\n')
                f.close()
            if log_array["type"][item] != "debug":
                log_frontend.log_for_frontend(log_array["type"][item], log_array["content"][item], time)
        else:
            with open( direction , 'a') as f:
                f.write('{:<10}'.format(log_array["type"][item]))
                f.write('{:<150}'.format(log_array["content"][item]))
                time = str(datetime.datetime.now()).replace(" ", "_").replace(".",":")
                f.write(time)
                f.write('\n')
                f.close()
                f.close()
            if log_array["type"][item] != "debug":
                log_frontend.log_for_frontend(log_array["type"][item], log_array["content"][item], time)
    return log_frontend.get_()

# import datetime
# import os
# import cv2
# from .log_for_frontend import Log

# imageSaveLocation = r"C:\Users\Harun\Desktop\imagesave"
# serverLogLocation = r"C:\Users\Harun\Desktop\serverlog"
# log_frontend = Log(log_array = {'type': [], 'content': [], 'time': []})

# class Log():
#     def __init__(self):
#         self.log_array = {"type": [],"content": [], "time": []}
    
#     def log_for_frontend(self, log_array_type, log_array_content, time):
#         self.log_array["type"].append(log_array_type)
#         self.log_array["content"].append(log_array_content)
#         self.log_array["time"].append(time)

#     def log_for_processed_image(image_orj, image_detected):
#         image_name = str(datetime.datetime.now()).replace(" ", "_").replace(".",":") + '_detected' +'.jpg'
#         image_name_orj = str(datetime.datetime.now()).replace(" ", "_").replace(".",":") +'.jpg'
#         cv2.imwrite(os.path.join(imageSaveLocation, image_name_orj), image_orj)
#         cv2.imwrite(os.path.join(imageSaveLocation, image_name), image_detected)
#         # print(os.path.join(configs[50]['configValue'], image_name), 'olarak kaydedildi')
#         path = str(datetime.date.today()) + '.txt'
#         direction =  os.path.join(str(serverLogLocation), path)
#         if not os.path.exists(direction):
#             with open( direction , 'w+') as f:
#                 f.write(str(os.path.join(imageSaveLocation, image_name_orj)) + ' olarak kaydedildi')
#                 f.write('\n')
#                 f.write(str(os.path.join(imageSaveLocation, image_name)) + ' olarak kaydedildi')
#                 f.write('\n')
#                 f.close()
#         else:
#             with open( direction , 'a') as f:
#                 f.write(str(os.path.join(imageSaveLocation, image_name_orj)) + ' olarak kaydedildi')
#                 f.write('\n')
#                 f.write(str(os.path.join(imageSaveLocation, image_name)) + ' olarak kaydedildi')
#                 f.write('\n')
#                 f.close()

#     def log_for_plc_bit_change(self, log_array):
#         path = str(datetime.date.today()) + '.txt'
#         direction =  os.path.join(str(serverLogLocation), path)
#         # for keys in log_array:
#         for item in range(len(log_array["type"])):
#             # print(log_array["type"][item])
#             # print(log_array["content"][item])
#             if not os.path.exists(direction):
#                 with open( direction , 'w+') as f:
#                     f.write('{:<10}'.format("Type"))
#                     f.write('{:<150}'.format("Log"))
#                     f.write("Date")
#                     f.write('\n')
#                     f.write('{:-^190}'.format("-"))
#                     f.write("\n")
#                     f.write('{:<10}'.format(log_array["type"][item]))
#                     f.write('{:<150}'.format(log_array["content"][item]))
#                     time = str(datetime.datetime.now()).replace(" ", "_").replace(".",":")
#                     f.write(time)
#                     f.write('\n')
#                     f.close()
#                 if log_array["type"][item] != "debug":
#                     self.log_for_frontend(log_array["type"][item], log_array["content"][item], time)
#             else:
#                 with open( direction , 'a') as f:
#                     f.write('{:<10}'.format(log_array["type"][item]))
#                     f.write('{:<150}'.format(log_array["content"][item]))
#                     time = str(datetime.datetime.now()).replace(" ", "_").replace(".",":")
#                     f.write(time)
#                     f.write('\n')
#                     f.close()
#                     f.close()
#                 if log_array["type"][item] != "debug":
#                     self.log_for_frontend(log_array["type"][item], log_array["content"][item], time)

#     def get_(self):
#         return self.log_array
