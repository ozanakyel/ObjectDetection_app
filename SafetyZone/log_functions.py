import datetime
import os
import cv2

imageSaveLocation = r"C:\Users\Harun\Desktop\imagesave"
serverLogLocation = r"C:\Users\Harun\Desktop\serverlog"
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
