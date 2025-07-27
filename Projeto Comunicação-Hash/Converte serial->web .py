import serial
import json
import hashlib
import time

PORTA_SERIAL_ARDUINO = 'COM9'  # <-- MUDE AQUI
BAUD_RATE = 9600
JSON_FILE_PATH = 'dados.json'

def initialize_serial(port, baudrate):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"Conectado com sucesso à porta {port} a {baudrate} bps.")
        return ser
    except serial.SerialException as e:
        print(f"Erro ao conectar na porta {port}: {e}")
        print("Verifique se a porta está correta e se não está sendo usada por outro programa.")
        return None

def process_data(data_packet):

    original_data_str = data_packet.get('data')
    received_hash = data_packet.get('hash')

    recalculated_hash = hashlib.md5(original_data_str.encode('utf-8')).hexdigest()

    # Comparar os hashes para verificar a integridade
    if recalculated_hash == received_hash:
        integrity_status = "OK"
    else:
        integrity_status = "FALHA"
        
    print(f"Dados Recebidos: '{original_data_str}' | Hash Recebido: {received_hash} | Hash Calculado: {recalculated_hash} | Integridade: {integrity_status}")


    log_entry = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'data': original_data_str,
        'received_hash': received_hash,
        'integrity_status': integrity_status
    }
    return log_entry

def append_to_json_file(file_path, new_entry):

    try:
        with open(file_path, 'r+', encoding='utf-8') as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
            logs.append(new_entry)
            
            f.seek(0)
            json.dump(logs, f, indent=4)
            f.truncate() 

    except FileNotFoundError:
        # Se o arquivo não existe, cria um novo com o registro
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump([new_entry], f, indent=4)
    print(f"Dados salvos em '{file_path}'")


def main():
    ser = initialize_serial(PORTA_SERIAL_ARDUINO, BAUD_RATE)
    if not ser:
        return 

    while True:
        try:
            # Ler uma linha da porta serial
            if ser.in_waiting > 0:
                line = ser.readline()
                
                decoded_line = line.decode('utf-8').strip()

                if decoded_line:
                    try:
                        data_packet = json.loads(decoded_line)
                        log_entry = process_data(data_packet)
                        append_to_json_file(JSON_FILE_PATH, log_entry)

                    except json.JSONDecodeError:
                        print(f"Erro: Recebido dado mal formatado (não é JSON): '{decoded_line}'")

        except KeyboardInterrupt:
            print("\nPrograma encerrado pelo usuário.")
            break
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            break
    
    if ser and ser.is_open:
        ser.close()
        print("Conexão serial fechada.")

if __name__ == "__main__":
    main()
