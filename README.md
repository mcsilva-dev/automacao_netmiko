# Projeto de Automação de Redes

Este projeto contém um script Python (`main.py`) para automação de redes, permitindo a conexão a dispositivos de rede e o envio de comandos de configuração.

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

### Conectar a um dispositivo

O script permite conectar a um dispositivo de rede usando as credenciais fornecidas.

```python
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}
try: 
    connection = ConnectHandler(**device)
    print(f'Connected to {device["host"]}')
except Exception as e:
    print(f'Failed to connect to {device["host"]}')