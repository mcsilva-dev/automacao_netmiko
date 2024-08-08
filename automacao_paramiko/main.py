from netmiko import ConnectHandler
import asyncio
import json

# Classe Huawei que representa um dispositivo Huawei
class Huawei:
    """
    Represents a Huawei device for automation.

    Args:
        device_type (str): The type of the device.
        host (str): The IP address or hostname of the device.
        username (str): The username for authentication.
        password (str): The password for authentication.
        commands (list, str, None, optional): A list|str of commands for configuration. Defaults to None.

    Attributes:
        device_type (str): The type of the device.
        host (str): The IP address or hostname of the device.
        username (str): The username for authentication.
        password (str): The password for authentication.
        commands (list): A list|str of commands for configuration.

    Methods:
        create_connection: Creates a connection to the device.
        send_config_set: Sends a set of configuration commands to the device.
        run_commands: Executes the automation.

    """
    
    

    def __init__(self, name: str, device_type: str, ip: str, username: str, password: str, commands: list | None | str = None) -> None:
        self.name = name
        self.device_type = device_type
        self.ip = ip
        self.username = username
        self.password = password
        self.commands = commands
    
    
    async def create_connection(self) -> ConnectHandler:
        """
        Creates a connection to the device.

        Returns:
            ConnectHandler: The connection object.

        """
        device = {
            'device_type': self.device_type,
            'host': self.host,
            'username': self.username,
            'password': self.password,
        }
        try: 
            connection = ConnectHandler(**device)
        except Exception as e:
            print(f'Failed to connect to {device["host"]}')
            return None
        return connection
    

    async def run_config_commands(self, commands: list | str = None) -> None:
        """
        Executes the config commands.

        """
        connection = await self.create_connection()
        try:
            assert connection
            assert self.commands is list | str or commands != None, 'The commands must be a list or str'
            if commands:
                output = connection.send_config_set(commands)
            else:
                output = connection.send_config_set(self.commands)
        except AssertionError as e:
            print(f'CommandError, Detail: {e}')
        except Exception as e:
            print(f'Failed to send commands to {connection.host}')
        else:
            # Pode alterar para return
            print(output)
    
    async def run_show_commands(self, commands: str = None) -> None:
        """
        Executes the show commands.

        """
        connection = await self.create_connection()
        try:
            assert connection
            assert self.commands is str or list, 'The commands must be a string'
            if commands:
                output = connection.send_command(commands)
            else:
                output = connection.send_command(self.commands)
        except AssertionError as e:
            print(f'CommandError, Detail: {e}')
        else:
            # Pode alterar para return
            print(output)
            

# Teste da classe Huawei com comandos de configuração
if __name__ == '__main__':
    # Cria um objeto Huawei
    huawei = Huawei(
        device_type='huawei',
        host='192.168.0.1',
        commands= 'dis int des',
        username='admin',
        password='admin'
    )
    asyncio.run(huawei.run_show_commands())