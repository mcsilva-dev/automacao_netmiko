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

	Attributes:
		device_type (str): The type of the device.
		host (str): The IP address or hostname of the device.
		username (str): The username for authentication.
		password (str): The password for authentication.

	Methods:
		send_config_set: Sends a set of configuration commands to the device.
		run_commands: Executes the automation.

	"""
	
	

	def __init__(self, device_type: str, ip: str, username: str, password: str) -> None:
		self.params = {
			'device_type': device_type,
			'host': ip,
			'username': username,
			'password': password,
		}
	

	async def run_config_commands(self, commands: list | str = None) -> None:
		"""
		Executes the config commands.

		"""

		try:
			with ConnectHandler(**self.params) as connection:
				assert commands, 'The commands must be a list or str'
				output = connection.send_config_set(commands)
		except AssertionError as e:
			return f'CommandError, Detail: {e}'
		except Exception as e:
			return f'Failed to send commands to {connection.host}'
		else:
			return output
	
	async def run_show_commands(self, commands: str = None) -> None:
		"""
		Executes the show commands.

		"""
		try:
			with ConnectHandler(**self.params) as connection:
				assert commands, 'The commands must be a string'
				output = connection.send_command(commands)
		except AssertionError as e:
			return f'CommandError, Detail: {e}'
		except Exception as e:
			return f'Failed to send commands to {connection.host}'
		else:
			return output
			

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