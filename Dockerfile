# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Cria um ambiente virtual
RUN python -m venv /ambiente-django

# Define permissões para o ambiente virtual
RUN chmod -R 755 /ambiente-django

# Define o PATH para usar o ambiente virtual
ENV PATH="/ambiente-django/bin:$PATH"

# Ativa o ambiente virtual usando o shell bash
RUN /bin/bash -c "source /ambiente-django/bin/activate"

WORKDIR /SintoniaMental
COPY  requirements.txt .

# Instala as dependências do projeto
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copia o código do projeto para o contêiner
COPY . /SintoniaMental

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /SintoniaMental
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found. Please enter the Python path to wsgi file.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "--bind",

# criar arquivo requiriements.txt automaticamente
# pip freeze > requirements.txt
