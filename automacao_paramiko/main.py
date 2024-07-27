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
    
    

    def __init__(self, device_type: str, host: str, username: str, password: str, commands: list | None | str = None) -> None:
        self.device_type = device_type
        self.host = host
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


    async def send_config_set(self, connection: ConnectHandler, commands: list | str = None)-> str:
        """
        Sends a set of configuration commands to the device.

        Args:
            connection (ConnectHandler): The connection object.
            commands (list, str): A list|str of commands for configuration.

        Returns:
            str: The output of the commands.

        """
        if commands:
            return connection.send_config_set(commands)
        else:
            return connection.send_config_set(self.commands)
        
    async def send_show_commands(self, connection: ConnectHandler, commands: str = None)-> str:
        """
        Sends a set of show commands to the device.

        Args:
            connection (ConnectHandler): The connection object.
            commands (str): A command for show especific configuration.

        Returns:
            str: The output of the commands.

        """
        if commands:
            return connection.send_command(commands)
        else:
            return connection.send_command(self.commands)
    

    async def run_config_commands(self, commands: list | str = None) -> None:
        """
        Executes the config commands.

        """
        connection = await self.create_connection()
        try:
            assert connection
            assert self.commands is list | str or commands != None, 'The commands must be a list or str'
            if commands:
                output = await self.send_config_set(connection, commands)
            else:
                output = await self.send_config_set(connection, self.commands)
        except AssertionError as e:
            print(f'CommandError, Detail: {e}')
        except Exception as e:
            print(f'Failed to send commands to {connection.host}')
        else:
            print(output)
    
    async def run_show_commands(self, commands: str = None) -> None:
        """
        Executes the show commands.

        """
        connection = await self.create_connection()
        try:
            assert connection
            assert self.commands is str or commands != None, 'The commands must be a string'
            if commands:
                output = await self.send_show_commands(connection, commands)
            else:
                output = await self.send_show_commands(connection, self.commands)
        except AssertionError as e:
            print('aqui')
            print(f'CommandError, Detail: {e}')
        else:
            print(output)
            

# Teste da classe Huawei com comandos de configuração
if __name__ == '__main__':
    try:
        with open('./hosts.json') as file:
            devices = json.load(file)
    except FileNotFoundError:
            print('File not found')
    else:
        huawei_instances = []
        for device in devices['devices']:
            # Cria uma instância da classe Huawei e define os comandos de configuração
            huawei_instances.append( 
                Huawei(
                    device_type=device['device_type'],
                    host=device['ip'],
                    username=device['username'],
                    password=device['password'],
                )
            )
        async def main():
            await asyncio.gather(*[huawei.run_config_commands(['system-view', 'interface xg 0/0/1', 'dis this']) for huawei in huawei_instances])
        asyncio.run(main())