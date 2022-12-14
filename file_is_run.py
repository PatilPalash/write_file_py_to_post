# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 23:17:35 2022

@author: admin
"""

import psycopg2  
import subprocess 
import os


#Set up input path and a loop that goes through all TIFs in the directory:

input_path = r'D:/raster/sentinel_data'

for raster in os.listdir(input_path):    
    if raster.endswith(".tif"):
       name = raster.split(".tif")[0]
       raster = os.path.join(input_path, raster)
#Connect to the PostgreSQL server:

       os.environ['PATH'] = r'C:\Program Files\PostgreSQL\14\bin'
       os.environ['PGHOST'] = 'localhost'
       os.environ['PGPORT'] = '5432'
       os.environ['PGUSER'] = 'postgres'
       os.environ['PGPASSWORD'] = 'Abcd@1234'
       os.environ['PGDATABASE'] = 'forraster'
     
       rastername = str(name)
       rasterlayer = rastername.lower()
  
       conn = psycopg2.connect(database="forraster", user="postgres", host="localhost", password="Abcd@1234") 
       cursor = conn.cursor()
       
       cmds = 'raster2pgsql -s 32643 -t 2000x2000 "' + raster + '" |psql'
       subprocess.call(cmds, shell=True)
       
       
       conn.commit()
       
       
       conn.close()