# ✈️ Flight Delay Prediction API

API desarrollada con **FastAPI** que expone un **modelo de Machine Learning** (creado por el equipo de *Data Science*) para **predecir si un vuelo se retrasará o no**.

Esta API actúa como puente entre el **modelo ML** y el **backend**, permitiendo que el **frontend** consuma la predicción y la muestre al usuario final de forma clara y rápida.

---

## 🧠 Descripción general

El objetivo del proyecto es:

* Implementar un modelo de Machine Learning entrenado para la **predicción de retrasos de vuelos**.
* Exponer dicho modelo mediante una **API REST** usando **FastAPI**.
* Permitir que el backend consuma la API y el frontend muestre al usuario si su vuelo **se retrasará o no**.


## 🛠️ Tecnologías utilizadas

* **Python**
* **FastAPI**
* **Uvicorn**
* **Scikit-learn / modelo ML**
* **Virtualenv (venv)**



## 📋 Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

* **Python 3.9 o superior**
* **Git**

Puedes verificar tu versión de Python con:

```bash
python --version
```

---

## 📦 Clonar el repositorio

Clona el repositorio en tu máquina local usando Git:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git](https://github.com/GP-Core/microServicioML.git
```

Luego entra al directorio del proyecto


## 🧪 Configuración del entorno virtual

Para evitar conflictos de dependencias, se utiliza un **entorno virtual**.

### 1️⃣ Crear el entorno virtual

Desde el directorio raíz del proyecto:

```bash
python -m venv .venv
```

---

### 2️⃣ Activar el entorno virtual

#### 🪟 Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

#### 🍎 macOS / 🐧 Linux

```bash
source .venv/bin/activate
```

Cuando el entorno esté activo, se verá

```bash
(.venv)
```

---

### 3️⃣ Instalar dependencias

Con el entorno virtual activado, instala los requerimientos:

```bash
pip install -r requirements.txt
```

---

## 🚀 Levantar la API

Una vez instaladas las dependencias, ejecuta el siguiente comando para iniciar el servidor:

```bash
uvicorn app:app --reload
```

* `app`: archivo principal de la API
* `app`: instancia de FastAPI
* `--reload`: recarga automática al detectar cambios

---

## 🔍 Verificar que la API funciona

Abre tu navegador y entra a:

```
http://127.0.0.1:8000/docs
```

Aquí se podrá:

* Ver la documentación automática (Swagger UI)
* Probar el endpoint
* Enviar datos y obtener predicciones

