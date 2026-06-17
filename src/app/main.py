from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI(
    title="FinTech UniSabana Risk Evaluator API",
    version="1.0.0",
    description="Microservicio de evaluación de riesgo e identidad para la validación de clientes."
)

# Modelo de datos de entrada 
class KYCRequest(BaseModel):
    document_id: str
    fullname: str
    country: str
    transaction_amount: float

@app.get("/")
def read_root():
    env = os.getenv("APP_ENV", "Desarrollo")
    return {
        "api_name": "FinTech UniSabana Core",
        "environment": env,
        "status": "Operational",
        "docs_path": "/docs"
    }

@app.get("/healthz")
def health_check():
    """ Endpoint crítico para Liveness y Readiness Probes en Kubernetes """
    return {"status": "healthy", "service": "kyc-evaluator"}

@app.post("/api/v1/kyc/evaluate")
def evaluate_kyc_risk(payload: KYCRequest):
    """ Lógica simulada de matriz de riesgo AML para el proyecto """
    risk_score = 0
    flags = []
    
    # Validación de jurisdicciones de alto riesgo 
    high_risk_countries = ["Simulistan", "TaxHaven", "JurisdiccionRestringida"]
    if payload.country in high_risk_countries:
        risk_score += 45
        flags.append("Jurisdicción con alertas internacionales de lavado de activos")
        
    # Control de umbrales transaccionales elevados
    if payload.transaction_amount > 10000:
        risk_score += 45
        flags.append("Monto transaccional supera el umbral de reporte automático (>10,000 USD)")
        
    # Validación de consistencia en ID
    if len(payload.document_id) < 6:
        risk_score += 10
        flags.append("Longitud de documento de identidad inusual o sospechosa")

    # Clasificación del estado del cliente
    if risk_score >= 80:
        decision = "REJECTED_HIGH_RISK"
    elif risk_score >= 40:
        decision = "SUSPENDED_MANUAL_REVIEW"
    else:
        decision = "APPROVED_LOW_RISK"

    return {
        "transaction_id": os.getenv("HOSTNAME", "local-pod"),
        "document_id": payload.document_id,
        "risk_score": risk_score,
        "evaluation": decision,
        "flags_triggered": flags,
        "processed_by_env": os.getenv("APP_ENV", "Desarrollo")
    }