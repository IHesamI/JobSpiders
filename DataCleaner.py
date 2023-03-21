# def ReadFiles():
#     Data=[]
#     filespath=os.path.join('Jobfinder')
#     CSVfiles=[f for f in os.listdir(filespath) if f.endswith('csv') ]
#     for eachfile in CSVfiles:
#         path=os.path.join(filespath,eachfile)
#         with open(path,'r',encoding="utf-8") as file:
#             Data.extend(file.readlines())
#     return Data

from googletrans import Translator
import nltk
from sklearn.cluster import KMeans
import pandas as pd
from  deep_translator import GoogleTranslator
translator=GoogleTranslator(source='auto',target='en')
# Reading from the Source file
raw_data=pd.read_csv('TotalData.csv',header=None).iloc[:,0]
# Translating Data and save it on the source file

# TotalData=[]

# with open('TotalData.csv','r',encoding="utf-8") as file:
#     TotalData.extend(file.readlines())


# 
# # fullstackRegex=r'full-*\s*stack'
# DotNetRegex =((asp|Asp|ASP|VB)?\.?(Net|net|NET)\.?(\s*core)?($|\s|\)))


for text in raw_data:
    english_text=translator.translate(text=text)
    with open('EnTotalData.txt','a') as file:
        file.write(english_text+'\n')

# Read from Translated Source
English_data=pd.read_csv('EnTotalData.txt',sep='\n',header=None).iloc[:,0].to_list()
English_data[:2]
