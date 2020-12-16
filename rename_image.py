# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:12:19 2020

@author: zhangkerou
"""
import os

directory_PATH = r'C:\Users\zhangkerou\Desktop\R\vehicle_dataset\cons_vehcl_dataset\jpgimages'
os.chdir(directory_PATH)
start_index=0

def rename_img(directory_PATH,start_index):
    directory_name = os.listdir(directory_PATH)
    
   
    for filename in directory_name:
        os.rename(filename,str(start_index) +'.jpg')
        start_index+=1
     

rename_img(directory_PATH)
