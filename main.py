from automacao_paramiko import Huawei
import asyncio
import json


async def get_objects():
    with open('hosts.json') as f:
        hosts = json.load(f)
    # criar todos os objetos e retorna como lista
    objects = [Huawei(**host) for host in hosts['devices']]
    return objects


async def main():
    devices = await get_objects()
    # executa um comando especifico em todos os objetos da lista obtida de forma assincrona.
    await asyncio.gather(*[device.run_show_commands('display interface description') for device in devices])
    
if __name__ == '__main__':
    asyncio.run(main())