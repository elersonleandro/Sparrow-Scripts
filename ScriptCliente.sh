#!/bin/bash

GREEN='\033[0;32m'

NC='\033[0m'

echo -e "${GREEN}Atualizando o Linux${NC}"
sudo apt update > /dev/null 2>&1 -y && sudo apt upgrade -y > /dev/null 2>&1

echo -e "${GREEN}Fazendo instalação do Java${NC}"
sudo apt install openjdk-17-jdk -y > /dev/null 2>&1

echo -e "${GREEN}Fazendo pull do Kotlin e Python (GitHub)${NC}"
git clone https://github.com/elersonleandro/Sparrow-Scripts.git > /dev/null 2>&1
cd Sparrow-Scripts

echo -e "${GREEN}Verificando se a máquina já está cadastrada${NC}"
sudo screen java -jar cadastrar-1.0-SNAPSHOT-jar-with-dependencies.jar 

echo -e "${GREEN}Inicializando a captura pelo kotlin"
sudo java -jar teste-1.0-SNAPSHOT-jar-with-dependencies.jar &

echo -e "${GREEN}Fazendo instalação do Python${NC}"
sudo apt install python3  -y > /dev/null 2>&1

echo -e "${GREEN}Baixando e criando ambiente virtual venv${NC}"
sudo apt install python3-venv -y > /dev/null 2>&1

python3 -m venv venv > /dev/null 2>&1
source venv/bin/activate

echo -e "${GREEN}Baixando dependências${NC}"
pip install psutil > /dev/null 2>&1
pip install mysql-connector-python > /dev/null 2>&1

echo -e "${GREEN}Inicializando a captura pelo Python${NC}"
python3 CapturaPython.py

