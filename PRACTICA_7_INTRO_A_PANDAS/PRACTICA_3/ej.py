import pandas as pd

personas = pd.read_csv("https://datasets.datos.mincyt.gob.ar/dataset/06ae9728-c376-47bd-9c41-fbdca68707c6/resource/11dca5bb-9a5f-4da5-b040-28957126be18/download/personas_2011.csv",sep=";")
ref_categoria_conicet = pd.read_csv("https://datasets.datos.mincyt.gob.ar/dataset/06ae9728-c376-47bd-9c41-fbdca68707c6/resource/c72c9f88-d9ef-4349-bb20-5c9a1aca5d67/download/ref_categoria_conicet.csv",sep=";")

personas_10mayores_provisorio=personas.sort_values(by=["edad"],ascending=False).head(10)
personas_10mayores = pd.concat([personas_10mayores_provisorio["persona_id"],personas_10mayores_provisorio["anio"],personas_10mayores_provisorio["edad"],personas_10mayores_provisorio["producciones_ult_4_anios"],personas_10mayores_provisorio["categoria_conicet_id"]],axis=1)
personas_10mayores_casi_final = pd.merge(personas_10mayores,ref_categoria_conicet)
personas_10mayores_final = pd.concat([personas_10mayores_casi_final["persona_id"],personas_10mayores_casi_final["categoria_conicet_descripcion"]],axis=1)
