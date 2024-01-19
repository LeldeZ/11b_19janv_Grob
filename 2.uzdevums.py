import json
import csv

def nolasit_un_drukat_otro_kolonnu(csv_fails):
  with open('2.uzdevums.py', 'r', encoding='utf8') as csv:


             lasitajs = csv.reader(csv)
            
              # izdrukā otro kolonnu
             for rinda in lasitajs: 
                if len(rinda) >= 2: 
                    otra_kolonna = rinda
                    print(otra_kolonna)