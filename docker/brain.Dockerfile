# Usamos una imagen ligera de Python para arquitectura ARM64 (Pi 4)
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalamos dependencias del sistema necesarias para sensores y comunicación
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libgpiod-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiamos los requerimientos primero para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# El código se montará como un volumen para facilitar el desarrollo,
# pero dejamos la estructura lista.
CMD ["python", "-u", "src/utils/watchdog.py"]