from fastapi import FastAPI
import os
import socket

app = FastAPI(
    title="Microservicio de Maestría en Arquitectura de Software - UNISABANA",
    version="1.0.0",
    description="API básica en Python para despliegue en Kubernetes con Helm y ArgoCD"
)

# Variables de Entorno
ENTORNO = os.getenv("APP_ENV", "Desarrollo")
VERSION = "1.0.1"

@app.get("/")
def read_root():
    return {
        "mensaje": "¡Hola desde el Microservicio 2.0 GitOps!",
        "entorno": ENTORNO,
        "version": VERSION,
        "hostname": socket.gethostname()  # Muestra qué pod específico de K8s responde
    }

@app.get("/healthz", status_code=200)
def health_check():
    """Endpoint de salud para los Probes de Kubernetes"""
    return {"status": "healthy", "version": VERSION}