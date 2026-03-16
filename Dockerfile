# 1. Imagen base de Python
FROM python:3.12-slim

# 2. Variables de entorno para que Python no se guarde basura y muestre logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Instalamos dependencias del sistema necesarias
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# 5. Instalamos las librerías de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiamos el resto de tu código
COPY . /app/

# 7. Exponemos el puerto de Django
EXPOSE 8000

# 8. Comando para arrancar
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
