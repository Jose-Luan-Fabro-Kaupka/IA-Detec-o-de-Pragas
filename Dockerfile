# Imagem base com Python e suporte a ciência de dados
FROM python:3.10-slim

# Cria e define diretório de trabalho
WORKDIR /app

# Copia arquivos do projeto para dentro da imagem
COPY . .

# Instala dependências
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expõe a porta padrão do Flask
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
