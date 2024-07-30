# README - E-commerce de Carros Elétricos Tesla

## Introdução

Bem-vindo ao e-commerce de carros elétricos da Tesla! Este projeto oferece uma plataforma completa para compra de veículos Tesla, proporcionando uma experiência personalizada e intuitiva para os usuários. O site inclui funcionalidades de login e cadastro, personalização de veículos durante o checkout, interação com cookies para melhorar a experiência do usuário e integração com a API do Google Tradutor para suporte multilíngue em português, inglês, francês e espanhol.

## Funcionalidades

### 1. Sistema de Login e Cadastro
- **Cadastro de Usuário**: Permite que novos usuários criem uma conta fornecendo informações básicas como nome, sobrenome, e-mail e senha.
- **Login de Usuário**: Usuários registrados podem fazer login com suas credenciais para acessar recursos exclusivos do site.

### 2. Compra de Veículos
- **Catálogo de Carros**: Lista completa de modelos de carros elétricos Tesla disponíveis para compra.
- **Detalhes do Veículo**: Página detalhada para cada modelo de carro, incluindo especificações técnicas, preços e opções de personalização.

### 3. Troca de Cor do Carro no Checkout
- **Personalização do Carro**: Durante o processo de checkout, os usuários podem escolher a cor desejada para o carro, visualizando as mudanças em tempo real.

### 4. Interação com Cookies
- **Cookies de Sessão**: Armazena informações de sessão do usuário para melhorar a navegação e experiência personalizada.

### 5. Integração com API do Google Tradutor
- **Tradução de Páginas**: O site pode ser traduzido para português, inglês, francês e espanhol utilizando a API do Google Tradutor, permitindo uma experiência de usuário mais acessível para falantes desses idiomas.

## Tecnologias Utilizadas
- **Framework**: Flask
- **Banco de Dados**: SQLite3
- **Autenticação**: Flask-Login
- **Integração com API**: Google Translate API

## Instalação e Configuração

### Pré-requisitos
- Python 3.x instalado
- Virtualenv instalado

### Passos para Instalação
1. Clone o repositório:
   ```sh
   git clone https://github.com/LuizHenrique21/E-commerce-Tesla.git
   ```
2. Navegue até o diretório do projeto:
   ```sh
   cd E-commerce-Tesla
   ```
3. Crie um ambiente virtual:
   ```sh
   python3 -m venv venv
   ```
4. Ative o ambiente virtual:
   - No Windows:
     ```sh
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
5. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

### Executando o Projeto
1. Inicie o servidor:
   ```sh
   python main.py
   ```
2. Abra o navegador e acesse:
   ```
   http://127.0.0.1:5000
   ```

## Estrutura do Projeto

```
E-commerce-Tesla/
│
├── main.py
├── form.py
├── requirements.txt
│
├── templates/
│   ├── tesla.html
│   ├── login.html
│   ├── cadastro.html
│   └── checkout.html
│
├── static/
│   ├── cadastroEstilo.css
│   ├── checkEstilo.css
│   ├── loginEstilo.css
│   ├── tesla.css
│   ├── scripts/
│   └── imagem/
│
├── instance/
│   ├── db.sqlite
│
└── venv/
```

## Espaço para Prints

# Página Inicial
##![tela inicial](https://github.com/user-attachments/assets/8f9423cd-b3bc-4437-a750-c8c53a94daf1)

### Página de Detalhes do Veículo
Model Y
![tela de veiculo](https://github.com/user-attachments/assets/9c9a7655-0405-4c50-9e33-dad79e3abaec)

Model 3
![tela de veiculo1](https://github.com/user-attachments/assets/e606bcb2-31be-4a46-a478-81e529695ad5)

Model X
![tela de veiculo2](https://github.com/user-attachments/assets/c1ed9307-fbfb-409c-a162-2308ac10c457)

Model S
![tela de veiculo3](https://github.com/user-attachments/assets/8b66c938-5dc4-4b7d-9681-9bc2c18b884d)

### Checkout com Personalização de Cor
![tela de checkout](https://github.com/user-attachments/assets/3d09c337-86dc-4547-8d3f-ed2a2f3b89a1)

### Página Traduzida
![tela traduzida](https://github.com/user-attachments/assets/f2c5c453-77bf-4369-9c39-cf4c0f87a613)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

---

<<<<<<< HEAD
Esperamos que você aproveite a experiência de compra de veículos Tesla em nosso e-commerce! Se tiver alguma dúvida ou sugestão, não hesite em nos contatar.
=======
Esperamos que você aproveite a experiência de compra de veículos Tesla em nosso e-commerce! Se tiver alguma dúvida ou sugestão, não hesite em nos contatar.
>>>>>>> 9e10266bfcd54809525cf57c7df782b91cc9e6f2
