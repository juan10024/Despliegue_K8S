from fastapi import FastAPI
import os
import socket

app = FastAPI(
    title="Microservicio de Maestría",
    version="1.0.0",
    description="API básica en Python para despliegue en Kubernetes con Helm y ArgoCD"
)

# Variables de Entorno
ENTORNO = os.getenv("APP_ENV", "Desarrollo")
VERSION = "1.0.0"

@app.get("/")
def read_root():
    return {
        "mensaje": "¡Hola desde el Microservicio Funcional de la Unisabana!",
        "entorno": ENTORNO,
        "version": VERSION,
        "hostname": socket.gethostname()  # Muestra qué pod específico de K8s responde
    }

@app.get("/healthz", status_code=200)
def health_check():
    """Endpoint vital para los Probes de Kubernetes"""
    return {"status": "healthy", "version": VERSION}