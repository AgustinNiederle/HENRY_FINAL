from google.cloud import storage
from google.oauth2 import service_account
bucket_name = 'review_main_cities'
archivo_dict = {
            'New York': {'positivos': 'comentarios_positivos_NY.csv', 'negativos': 'comentarios_negativos_NY.csv'},
            'California': {'positivos': 'comentarios_positivos_CA.csv', 'negativos': 'comentarios_negativos_CA.csv'},
            'Florida': {'positivos': 'comentarios_positivos_FL.csv', 'negativos': 'comentarios_negativos_FL.csv'},
            'Texas': {'positivos': 'comentarios_positivos_TX.csv', 'negativos': 'comentarios_negativos_TX.csv'}
        }

credentials = service_account.Credentials.from_service_account_file(
    'env/utopian-honor-438417-u7-5b7f84fcfd25.json'
)

client = storage.Client(project='utopian-honor-438417-u7', credentials=credentials)

def descargar_archivo(ciudad_seleccionada, opinion):
    ciudad = archivo_dict[ciudad_seleccionada]
    archivo_name = ciudad[opinion]

    try:
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(archivo_name)
        archivo_local = f"./{archivo_name}"
        blob.download_to_filename(archivo_local)
        return archivo_local
    except Exception as e:
        raise ValueError(f"Error al descargar el archivo {archivo_name}: {e}")