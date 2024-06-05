import json
import pandas as pd

def crear_csv(direccion):
  with open(direccion,'r', encoding='utf-8') as f:
    datos_entrenamiento = json.load(f)

  reclamos = [i['reclamo'] for i in datos_entrenamiento]
  etiquetas = [i['etiqueta'] for i in datos_entrenamiento]

  return pd.DataFrame({'reclamo':reclamos, 'etiqueta':etiquetas})