import json 
def nolasit_un_drukat_treso_rindu(file_path):
  with open('3.uzdevums.py', 'r', encoding='utf8') as maja:
            rindu_saraksts = maja.readlines()
            if len(rindu_saraksts) >= 3:
                tresa_rinda = rindu_saraksts.strip()  
                print(tresa_rinda)