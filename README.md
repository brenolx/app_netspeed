# NET-SPEED v1.0

![Licença](https://img.shields.io/badge/licença-MIT-brightgreen) ![Python](https://img.shields.io/badge/python-3.10%2B-blue)

## Descrição

O **NET-SPEED** é uma aplicação desenvolvida em Python que permite medir a velocidade da sua conexão de internet, fornecendo as métricas de download, upload e ping. Uma ferramenta simples e eficaz para verificar a qualidade da sua conexão.

## Requisitos

- Python 3.10 ou superior
- Gerenciador de pacotes `pip`

## Instalação

Siga os passos abaixo para configurar o ambiente e instalar as dependências:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/brenolx/app_netspeed.git
   cd app_netspeed
   ```

2. **(Opcional) Crie um ambiente virtual:**

   ```bash
   python -m venv venv

   # Para Linux/Mac
   source venv/bin/activate

   # Para Windows
   venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para executar o programa, utilize o seguinte comando:

```bash
python main.py
```

### Comandos Disponíveis

- `--net-speed` ou `-ns`: Exibe a velocidade de DOWNLOAD, UPLOAD e o PING.
- `--help` ou `-h`: Exibe ajuda sobre a aplicação.
- `--exit` ou `-e`: Finaliza a instância atual da aplicação.

### Exemplo de Uso

1. Execute o programa.
2. Digite `--net-speed` ou `-ns` para iniciar o teste de velocidade.
3. O programa exibira a velocidade de download, upload e o ping.

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para colaborar:

1. Faça um fork do projeto.
2. Crie uma nova branch:

   ```bash
   git checkout -b feature/nova-funcionalidade
   ```

3. Realize suas alterações e faça commit:

   ```bash
   git commit -m "Adiciona nova funcionalidade"
   ```

4. Envie para o repositório remoto:

   ```bash
   git push origin feature/nova-funcionalidade
   ```

5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

## Contato

Para mais informações, entre em contato:

- **Breno Cavalcante**
- **GitHub:** https://github.com/brenolx

