# Documentación del Proyecto: Registro de Créditos

## Descripción General

Aplicación web desarrollada con **Python (Flask)** y **SQLite**, que permite registrar, editar, eliminar y visualizar créditos otorgados a clientes. Además, genera una visualización en gráfica de dona de la distribución de créditos por cliente utilizando **Chart.js**.

---

## Estructura del Proyecto

```
proyecto_creditos/
│
├── app.py                      # Aplicación principal Flask
├── database.db                 # Base de datos SQLite
├── requirements.txt            # Lista de dependencias
│
├── templates/
│   ├── index.html              # Vista principal con formulario y tabla
│   └── editar.html             # Vista para editar créditos
│
├── static/
│   ├── css/
│   │   └── style.css           # Estilos CSS personalizados
│   └── js/
│       └── chart.js           # Lógica de la gráfica con Chart.js
```

---

## Tecnologías Usadas

- **Backend:** Python 3.x, Flask
- **Frontend:** HTML, CSS, Chart.js
- **Base de Datos:** SQLite
- **ORM:** SQLAlchemy

---

## Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone git@github.com:nanecorner/proyecto_creditos.git
cd proyecto_creditos
```

### 2. Crear y activar entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# o
venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python app.py
```
ó
```bash
python3 app.py
```

La aplicación estará disponible en: [http://localhost:8800](http://localhost:8800)

---

## Funcionalidades

- Registrar nuevo crédito (cliente, monto, tasa, plazo, fecha).
- Listar todos los créditos registrados en una tabla.
- Editar crédito existente.
- Eliminar crédito.
- Visualizar una gráfica de dona con los créditos por cliente.

---

## Requisitos (requirements.txt)

```txt
blinker==1.8.2
click==8.1.8
flask==3.0.3
flask-sqlalchemy==3.1.1
greenlet==3.1.1
importlib-metadata==8.5.0
itsdangerous==2.2.0
jinja2==3.1.6
MarkupSafe==2.1.5
sqlalchemy==2.0.40
typing-extensions==4.13.2
werkzeug==3.0.6
zipp==3.20.2
```

---

## Capturas de Pantalla

![ejemplo-creditos](https://github.com/user-attachments/assets/c1133cb2-e313-40f0-957e-bf9fef99bfe8)

---

## Autor

**Daniel Rincón Méndez**\
Ingeniero de Software\
📧 Contacto: [daniel2000rincon@gmail.com](mailto\:daniel2000rincon@gmail.com)\

---

## Créditos

- Diseño original y desarrollo: Daniel Rincón Méndez
- Frameworks y librerías: Flask, Chart.js

