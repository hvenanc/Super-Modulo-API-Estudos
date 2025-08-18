# Configuração do Ambiente de Desenvolvimento Python

Este guia descreve como configurar um ambiente virtual para este projeto, garantindo que as dependências sejam gerenciadas de forma isolada. Siga as instruções para o seu sistema operacional (Windows ou Linux/macOS).

## Sumário

- [Pré-requisitos](#pré-requisitos)
- [O que é um Ambiente Virtual?](#o-que-é-um-ambiente-virtual)
- [Configuração do Ambiente Virtual](#configuração-do-ambiente-virtual)
- [Para Usuários de Windows (usando PowerShell)](#para-usuários-de-windows-usando-powershell)
- [Para Usuários de Linux e macOS (usando Bash)](#para-usuários-de-linux-e-macos-usando-bash)
- [Instalando as Dependências](#instalando-as-dependências)
- [Desativando o Ambiente Virtual](#desativando-o-ambiente-virtual)
- [Bibliotecas Utilizadas no Projeto](#bibliotecas-utilizadas-no-projeto)

## Pré-requisitos

Antes de começar, certifique-se de que você tem o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://python.org).

Para verificar se o Python está instalado, abra seu terminal (PowerShell ou Bash) e digite:

```bash
python --version
```

```bash
python3 --version
```

# O que é um Ambiente Virtual?
Um ambiente virtual é um diretório que contém uma instalação Python de uma versão específica, além de uma série de pacotes adicionais. O uso de ambientes virtuais permite isolar as dependências de diferentes projetos, evitando conflitos entre as versões das bibliotecas.

# Configuração do Ambiente Virtual
Recomendamos nomear o ambiente virtual como .venv para que ele seja automaticamente reconhecido por ferramentas de desenvolvimento como o VS Code. O ponto no início também o torna um diretório oculto em sistemas baseados em Unix.

## Para Usuários de Windows (usando PowerShell)

### 1. Abra o PowerShell:
Navegue até a pasta raiz do seu projeto.

### 2. Crie o ambiente virtual:
Execute o seguinte comando para criar um ambiente virtual chamado .venv:

```
python -m venv .venv
```

### 3. Ative o ambiente virtual:
Para começar a usar o ambiente virtual, você precisa ativá-lo:

```
.venv\Scripts\Activate
```

#### Nota: Se você encontrar um erro sobre a execução de scripts estar desabilitada, talvez seja necessário alterar a política de execução do PowerShell. Você pode fazer isso para o usuário atual com o seguinte comando e, em seguida, tentar ativar o ambiente novamente:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Após a ativação, você verá (.venv) no início do seu prompt do terminal.

## Para Usuários de Linux e macOS (usando Bash)
### 1. Abra o Terminal:
Navegue até a pasta raiz do seu projeto.

### 2. Crie o ambiente virtual:
Execute o seguinte comando para criar um ambiente virtual chamado .venv:

```
python3 -m venv .venv
```
Dependendo da sua instalação, você pode precisar usar python em vez de python3.

### 3. Ative o ambiente virtual:
Para começar a usar o ambiente virtual, você precisa ativá-lo:

```
source .venv/bin/activate
```
Após a ativação, você verá (.venv) no início do seu prompt do terminal.


## Instalando as Dependências
Com o ambiente virtual ativado, você pode instalar todas as bibliotecas necessárias para o projeto, que estão listadas no arquivo requirements.txt.

Execute o seguinte comando:

```
pip install -r requirements.txt
```

Este comando irá ler o arquivo requirements.txt e instalar todas as bibliotecas listadas com suas versões especificadas.

## Desativando o Ambiente Virtual
Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual com o seguinte comando:

```
deactivate
```

Isso removerá o (.venv) do seu prompt do terminal e retornará ao ambiente global do Python do seu sistema.

## Bibliotecas Utilizadas no Projeto

Flask:
```
pip install Flask
```

Firebase:
```
pip install firebase-admin
```

Dotenv:
```
pip install python-dotenv
```




