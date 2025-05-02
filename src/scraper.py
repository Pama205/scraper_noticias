import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os
from pathlib import Path

# Configuración inicial
BASE_DIR = Path(__file__).parent.parent  # Raíz del proyecto (donde está la carpeta 'data')
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)  # Crea la carpeta si no existe

def extraer_titulares():
    url = "https://www.aljazeera.com/news/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        print("🔍 Extrayendo titulares de Al Jazeera...")
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verifica errores HTTP

        soup = BeautifulSoup(response.text, "html.parser")
        titulares = []

        # Busca todos los elementos <article> y extrae el texto de los <h3>
        for articulo in soup.find_all("article"):
            titular = articulo.find("h3")
            if titular:
                titulares.append(titular.get_text(strip=True))

        if titulares:
            # Genera nombre de archivo con fecha
            fecha = datetime.now().strftime("%Y-%m-%d")
            archivo_csv = DATA_DIR / f"titulares_{fecha}.csv"

            # Guarda en CSV
            pd.DataFrame(titulares, columns=["Titular"]).to_csv(archivo_csv, index=False)
            print(f"✅ {len(titulares)} titulares guardados en: {archivo_csv}")

        else:
            print("⚠ No se encontraron titulares. Revisa los selectores HTML.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    extraer_titulares()