FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Imagen Ejecutable
FROM python:3.11-slim AS runner

WORKDIR /app

# Copiar las librerías instaladas desde la etapa de compilación
COPY --from=builder /root/.local /root/.local
COPY ./app ./app

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]