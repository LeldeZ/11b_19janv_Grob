import json
def ievadit_un_ierakstit_faila(lietotaja_vards):
        with open('lietotajs', 'a', encoding='utf-8') as lv:
            lv.write(lietotaja_vards)
        
        print("Lietotājs'{lietotaja_vards}' .")
   