# 📰 Extractor de Titulares de Al Jazeera

Script en Python que extrae los últimos titulares de noticias de [Al Jazeera](https://www.aljazeera.com/news/) y los guarda en un archivo CSV con fecha.

## 🚀 Características
- Extracción automática de titulares usando **BeautifulSoup**.
- Guardado en CSV con **Pandas**.
- Estructura organizada en carpetas (`data/` para los archivos generados).
- Compatible con Windows, macOS y Linux.

## 📁 Estructura del Proyecto

```bash
proyecto_noticias/
├── venv/              # Entorno virtual (ignorado por Git)
├── data/              # CSVs generados (ignorados)
├── src/
│   └── scraper.py     # Script principal
├── requirements.txt   # Dependencias (en raíz)
├── README.md          # Documentación
└── .gitignore         # Archivos ignorados
```

## ⚙️ Requisitos
- Python 3.8+
- Librerías especificadas en `requirements.txt`

## 🛠️ Instalación
Clona el repositorio:

```bash
   git clone https://github.com/Pama205/scraper_noticias.git
   cd carpeta-proyecto
```

🛠️ Comandos para configurar el entorno (ejecuta en orden)

1. Desde la raíz del proyecto (proyecto_noticias/):

```bash
   pip install -r requirements.txt
```
2. Activa el entorno:

   Windows:
   ```bash
      .\venv\Scripts\activate
   ```

   Mac/Linux:
   ```bash
      source venv/bin/activate
   ```
3. Instala dependencias:

```bash
   pip install -r requirements.txt
```
4. Ejecuta el script (con el entorno activado):

```bash
   python src/scraper.py
```

🖥️ Uso

Ejecuta el script desde la raíz del proyecto:

```bash
   python src/scraper.py
```

Salida esperada:

```bash
    🔍 Extrayendo titulares de Al Jazeera...
    ✅ 14 titulares guardados en: scraper_noticias/data/titulares_2025-05-03.csv
```

📝 Archivos Generados
Los CSV se guardan en data/ con el formato:

```bash
   titulares_YYYY-MM-DD.csv
```

Contenido ejemplo del CSV:

```bash
   Titular
   "Israel approves new illegal West Bank settlements"
   "Ukraine recaptures 20% of territory near Kharkiv"
   "Global climate summit ends with mixed results"
```

🤝 Contribuir

Si deseas mejorar el proyecto:

1. Haz un fork

2. Crea una rama (git checkout -b feature/mejora)

3. Haz commit de tus cambios (git commit -m 'Agrega X funcionalidad')

4. Haz push a la rama (git push origin feature/mejora)

5. Abre un Pull Request

⚠️ Limitaciones

1. Los selectores HTML pueden cambiar si Al Jazeera actualiza su sitio.

2. Solo se extraen titulares (no fechas, enlaces o contenido completo).

⚠️ Solución de problemas:

1. Verifica que el entorno esté activado

2. Reinstala dependencias:
   ```bash
      pip install --force-reinstall -r requirements.txt
   ```

📄 Licencia
MIT

## 📌 Información del Proyecto

**Desarrollador:**  
Pedro Alexander Martinez Arthur  

**Correo electrónico:**  
[pama205@gmail.com](mailto:pama205@gmail.com)  

**Fecha de desarrollo:**  
Abril 2025  

**Última actualización:**  
3 de mayo de 2025    