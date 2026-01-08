# python
Funcionalidades de python que vaya aprendiendo

Trabajamos sobre una maquina virtual. Si no la tenemos instalada hacemos los siguiente. 
- Para los sistemas windows debemos de tener wsl instalado para emular entornos linux.
-  Instalación del entorno virtual: python -m venv virtu
La activamos desde el root del proyecto:
PS C:\Users\f.gorgojo.marugan\workspace\PYTHON\python> .\virtual\Scripts\activate

Instalamos módulos adicionales al los de la librería standard
(virtual) PS C:\Users\f.gorgojo.marugan\workspace\PYTHON\python> pip install -r .\requirements.txt

# PEP (Python Enhancement Proposals) 
- PEP8 - Code Style
  Estrategia de `linting`a traves de la tool:  `pycodestyle script.py`
- PEP257 - Doc String 
  Validamos con `pydocstyle script.py`

# Instalacion de npm y node.js para algunos ejercicios:
Se nos pide la instalación de una app de `emojics` : npm install --global emoj@3.3.0
- Previamente en windows el instaladoro nvm:
    - nvm --version
    - mvm install lts --> Instala node.js y nmp a la vez
    - nvm use lts  , se activa desde una consola administrativa
    - node -v  y npm -v --> debe de mostrar version v24.12.2 y 11.6.2 resp.

# API y webs
https://home.openweathermap.org/ alta con cuenta de yahoo para pruebas
Token inicial:  45b3eb2041f2907d2468147fdbe76d5b   default Udacity

## Flask 
-  `pip install flask -U`
-  Levantar la variable de entorno;
    - Unix: `export FLASK_APP=app.py`
    - PowerShell: `$env:FLASK_APP = "app.py"`
- Ejecución del servicio: `flask run --host 0.0.0.0 --port 3000 --reload`
- Petición de servicio: `http://127.0.0.1:3000?city=madrid&country=esp`
- Ejecución habitual: `python app.py` especificando en app.py este arranque:
``` 
if __name__ == "__main__":
    app.run()
```
  Abre por defecto http://127.0.0.1:5000









   
