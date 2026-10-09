# Ficha de entorno
Usa la versión de Python que tengas instalada. No se fija una versión de Python para el examen.

Instala estas dependencias, utilizadas para generar y verificar el modelo proporcionado:

```bash
uv add pydantic scikit-learn joblib numpy scipy pytest
```

Estas dependencias se utilizan para generar y verificar el modelo proporcionado.

Crea el proyecto con `uv init --package clasificador-paquetes`, organiza tú los archivos como indica B1 y conserva la configuración de empaquetado generada por uv. El archivo `src/clasificador_paquetes/__init__.py` puede estar vacío. Añade al pyproject.toml:

```toml
[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]
```

Desde la raíz del proyecto, en la terminal habitual (Git Bash en Windows):

```bash
uv sync
uv run python -m clasificador_paquetes.inference
uv run pytest
```

El programa genera resultados.csv. pytest comprueba los contratos y el flujo: todos los casos deben pasar. Si un caso falla, revisa el error y corrige tu código, sin borrar ni cambiar los tests. Al principio los tests fallan porque el starter no está resuelto.

Sube también RESPUESTAS_TEORIA.md al mismo repositorio con las respuestas A1-A6. No incluyas .venv, cachés ni credenciales.
