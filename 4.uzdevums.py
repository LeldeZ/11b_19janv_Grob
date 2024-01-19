def nolasit_un_drukat_faila_saturs():
        
        faila_nosaukums = input("4.uzdevums.py: ")
        paplasinajums = input("4.uzdevums.py): ")
        file_path = "{'4.uzdevums.py'}.{paplasinajums}"

        with open(file_path, 'r', encoding='utf-8') as tu:
            saturs = tu.read()

 
