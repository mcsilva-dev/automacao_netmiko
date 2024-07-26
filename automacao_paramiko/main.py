from netmiko import ConnectHandler
import asyncio
import json

# Classe Huawei que representa um dispositivo Huawei
class Huawei:
    def __init__(self, device_type: str, host: str, username: str, password: str, commands: list = list()) -> None:
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password
        self.commands = commands
        
    # Método assíncrono para criar uma conexão com o dispositivo
    async def create_connection(self) -> ConnectHandler:
        device = {
            'device_type': self.device_type,
            'host': self.host,
            'username': self.username,
            'password': self.password,
        }
        try: 
            connection = ConnectHandler(**device)
            print(f'Connected to {device["host"]}')
        except Exception as e:
            print(f'Failed to connect to {device["host"]}')
        return connection

    # Método assíncrono para enviar um conjunto de comandos de configuração para o dispositivo
    async def send_config_set(self, connection: ConnectHandler, commands:list)-> str:
        try:
            output = connection.send_config_set(self.commands)
        except Exception as e:
            print(f'Failed to send commands to {connection.host}')
        else:
            return output

    # Método assíncrono para executar a automação
    async def run_commands(self) -> None:
        connection = await self.create_connection()
        output = await self.send_config_set(connection, self.commands)
        print(output)
            
if __name__ == '__main__':
    try:
        with open('./hosts.json') as file:
            devices = json.load(file)
    except FileNotFoundError:
            print('File not found')
    else:
        device = devices['devices'][0]
        # Cria uma instância da classe Huawei e define os comandos de configuração
        huawei = Huawei(
            device_type=device['device_type'],
            host=device['ip'],
            username=device['username'],
            password=device['password'],
        )
        # Comandos de configuração a serem enviados ao dispositivo Huawei
        huawei.commands =[ 
            'command1',
            'command2',
            'command3',
        ]
        asyncio.run(huawei.run_commands())
    