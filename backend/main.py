from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import csv
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LeadData(BaseModel):
    nombre: str
    telefono: str
    correo: str
    interes: str
    fecha: str
    origen: dict

# Nombre del archivo donde se guardará tu base de datos
ARCHIVO_CSV = "base_de_datos_leads.csv"

@app.post("/webhook/lead")
async def recibir_lead(lead: LeadData):
    lead_dict = lead.model_dump()
    
    # 1. Imprimir en la terminal (lo que ya tenías)
    print("--------------------------------------------------")
    print(f"🔥 ¡NUEVO LEAD CAPTURADO!")
    print(f"👤 Nombre: {lead_dict['nombre']}")
    print(f"📱 WhatsApp: {lead_dict['telefono']}")
    print(f"🏠 Interés: {lead_dict['interes']}")
    print("--------------------------------------------------")

    # 2. Guardar en el archivo CSV (Excel)
    archivo_existe = os.path.isfile(ARCHIVO_CSV)
    
    # Abrimos el archivo en modo 'a' (append) para añadir sin borrar lo anterior
    with open(ARCHIVO_CSV, mode='a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        
        # Si el archivo es nuevo, le ponemos los encabezados de las columnas
        if not archivo_existe:
            writer.writerow(['Fecha', 'Nombre', 'WhatsApp', 'Correo', 'Interés', 'Fuente_UTM', 'Campaña_UTM'])
        
        # Guardamos la fila con los datos del lead
        writer.writerow([
            lead_dict['fecha'], 
            lead_dict['nombre'], 
            lead_dict['telefono'], 
            lead_dict['correo'], 
            lead_dict['interes'], 
            lead_dict['origen'].get('fuente', 'N/A'), 
            lead_dict['origen'].get('campana', 'N/A')
        ])

    return {"status": "success", "message": "Lead guardado en base de datos"}