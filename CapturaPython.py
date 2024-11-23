import psutil
import time
from mysql.connector import connect, Error

config = {
  'user': 'root',
  'password': 'urubu100',
  'host': '52.71.94.239',
  'database': 'Sparrow'
}

                                                                                    
def get_mac_address(interface_name='enX0'):
    addrs = psutil.net_if_addrs()
    if interface_name in addrs:
        for addr in addrs[interface_name]:
            if addr.family == psutil.AF_LINK:
                return addr.address
    return None

mac_address = get_mac_address('enX0')  # ou 'wlan0' para Wi-Fi
print(f"MAC Address: {mac_address}")




try:
        db = connect(**config)
        if db.is_connected():
            db_info = db.get_server_info()
                    
            with db.cursor() as cursor:
                query1 = (f"SELECT * FROM maquina WHERE endereco_mac = '{mac_address}'")
                        
                cursor.execute(query1)
                    
                
                result = cursor.fetchone()
                print(result)
                    
            cursor.close()
            db.close()

except Error as e:
    print('Error to connect with MySQL -', e) 

tamanho = len(result)


if(tamanho > 0):
    i = 0
    a = 0
    while i < 10: 
        while a < 10:
            cpu = psutil.cpu_percent(interval=None, percpu=False)        

            ram = psutil.virtual_memory()[2]
        
            print(f"Uso da CPU: {cpu}%")
            print(f"Uso da RAM: {ram}%")

            try:
                db = connect(**config)
                if db.is_connected():
                    db_info = db.get_server_info()
                
                with db.cursor() as cursor:
                    query1 = ("INSERT INTO Sparrow.dado_capturado VALUES "
                            f"(default, {cpu}, current_timestamp(),{result[1}, {result[0]}, 1)")
                    query2 = ("INSERT INTO Sparrow.dado_capturado VALUES "
                            f"(default, {ram}, current_timestamp(),{result[1}, {result[0]}, 2)")
                    
                    cursor.execute(query1)
                    cursor.execute(query2)
                    db.commit()
                    print("Inserido no banco de dados com sucesso")
                
                cursor.close()
                db.close()

            except Error as e:
                print('Error to connect with MySQL -', e) 

            a += 1
            i = 0
            time.sleep(1)

        disk = psutil.disk_usage("/")[3]

        print(f"Espaço de disco disponível: {disk}%")

        try:
                db = connect(**config)
                if db.is_connected():
                    db_info = db.get_server_info()
                
                with db.cursor() as cursor:
                    query1 = ("INSERT INTO Sparrow.dado_capturado VALUES "
                            f"(default, {disk}, current_timestamp(),{result[1}, {result[0]}, 3)")
                    
                    cursor.execute(query1)
                    db.commit()
                    print("Inserido no banco de dados com sucesso")
                
                cursor.close()
                db.close()

        except Error as e:
            print('Error to connect with MySQL -', e) 
        i += 1
        a = 0
