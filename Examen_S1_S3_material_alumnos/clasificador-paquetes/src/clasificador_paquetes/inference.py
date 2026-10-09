import csv
from pathlib import Path
import joblib
from .contracts import Entrada, Salida


def leer_csv(ruta: Path) -> list[Entrada]:
    with open(ruta, mode = 'r', encoding="utf-8", newline="") as archivo:
        rows = list(csv.DictReader(archivo))
        paquetes = []
        if not rows:
            raise ValueError(f"El archivo csv no tiene filas")
        for row in rows:
            request = Entrada.model_validate(row)
            paquetes.append(request)
    return paquetes


def preprocesar(entrada: Entrada) -> list[float]:
    peso_redondeado = round(entrada.peso_kg, 1)
    
    return [
        peso_redondeado,
        float(entrada.distancia_km)
    ]


def cargar_modelo(ruta: Path):
    return joblib.load(ruta)



def predecir(entrada: Entrada, modelo) -> Salida:
    data = preprocesar(entrada)
    categoria = modelo.predict([data])[0]
    probabilidades = modelo.predict_proba([data])[0]
    confianza = max(probabilidades)
    return Salida(
            id_paquete=entrada.id_paquete,
            categoria=categoria,
            confianza=confianza
    )


def guardar_csv(resultados: list[Salida], ruta: Path) -> None:
    columnas_salida = ["id_paquete", "categoria", "confianza"]

    with ruta.open(mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas_salida)
        escritor.writeheader()

        for resultado in resultados:
            escritor.writerow(resultado.model_dump())

def ejecutar(entrada: Path, modelo: Path, salida: Path) -> None:
    paquetes = leer_csv(entrada)
    modelo = cargar_modelo(modelo)
    predicciones = []

    for paquete in paquetes:
        prediccion = predecir(paquete, modelo)
        predicciones.append(prediccion)
    guardar_csv(predicciones, salida)

if __name__ == "__main__":
    ejecutar(
        Path("data/raw/paquetes.csv"),
        Path("models/modelo.joblib"),
        Path("resultados.csv"),
    )
