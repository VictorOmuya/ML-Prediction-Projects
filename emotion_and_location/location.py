from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit, QMessageBox

import pandas as pd
import pickle

from exif import Image
import webbrowser
from time import sleep
import datetime
import reverse_geocoder as rg
import pycountry

def messages(title, message):
    mess = QMessageBox()
    mess.setWindowTitle(title)
    mess.setText(message)
    mess.setStandardButtons(QMessageBox.Ok)
    mess.exec_()
    
def predict(imagePath):
    try:
        img_path = imagePath
        
        with open(img_path, "rb") as palm_1_file:
            palm_1_image = Image(palm_1_file)
            images = [palm_1_image]
            
        for index, image in enumerate(images):
            if image.has_exif:
                status = "contains exif"
            else:
                status = "does not contain any EXIF information."
            
           
        image_members = []

        for image in images:
            image_members.append(dir(image))

        for index, image_member_list in enumerate(image_members):
            pass
            #print(f"Image {index} contains {len(image_member_list)} members:")
            #print(f"{image_member_list}\n")
            
            if  "gps_longitude" not in image_member_list:
                
                messages("location", "cant get the location of this image")
                res1 = ''
                res2 = ''
                res3 = ''
                url = ''
            else:
                
                for index, image in enumerate(images):
                    if "datetime_original" not in image_member_list:
                        res1 = "date/time: "+ datetime.today()
                    
                    else:
                    
                        res1 = "date/time: "+image.datetime_original
                        
                for index, image in enumerate(images):
                    decimal_latitude = dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)
                    decimal_longitude = dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)
                    coordinates = (decimal_latitude, decimal_longitude)
                    location_info = rg.search(coordinates)[0]
                    location_info['country'] = pycountry.countries.get(alpha_2=location_info['cc'])
                    #print(f"{location_info}\n")
                    res2 = " town: "+ location_info['name']
                    res3 = " state: "+ location_info['admin1']
                    
                
                for index, image in enumerate(images):
                    sleep(10)
                    url = draw_map_for_location(image.gps_latitude, 
                          image.gps_latitude_ref, 
                          image.gps_longitude,
                          image.gps_longitude_ref)
                    
        
    except: 
        messages("error", "ensure you have an image uploaded")
        
    return res1, res2, res3, url
    



def format_dms_coordinates(coordinates):
    pass
    return f"{coordinates[0]}° {coordinates[1]}\' {coordinates[2]}\""
        
def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
    
    decimal_degrees = coordinates[0] + \
                  coordinates[1] / 60 + \
                  coordinates[2] / 3600

    if coordinates_ref == "S" or coordinates_ref == "W":
        decimal_degrees = -decimal_degrees

    return decimal_degrees


def draw_map_for_location(latitude, latitude_ref, longitude, longitude_ref):
    decimal_latitude = dms_coordinates_to_dd_coordinates(latitude, latitude_ref)
    decimal_longitude = dms_coordinates_to_dd_coordinates(longitude, longitude_ref)
    url = f"https://www.google.com/maps?q={decimal_latitude},{decimal_longitude}"
    webbrowser.open_new_tab(url)
    
    return url