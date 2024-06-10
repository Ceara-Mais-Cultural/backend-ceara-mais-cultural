# Use a imagem oficial do Python como base
FROM python:3.8-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala as ferramentas de compilação necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    libc-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de requerimentos para o diretório de trabalho
COPY requirements.txt /app/

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o conteúdo do projeto para o diretório de trabalho
COPY . /app/

# Expõe a porta que a aplicação usará
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "CearaMaisCultural.wsgi:application"]
