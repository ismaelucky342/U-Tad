from data_extractor import DataExtractor
import os

# Asegúrate de exportar tu clave antes de ejecutar:
# export RAPIDAPI_KEY="tu_clave_aqui"

def main():
    extractor = DataExtractor()
    try:
        df = extractor.load_data_api(query="#bitcoin", max_results=10, output_file="test_tweets.csv")
        print(df.head())
        print(f"Guardado en: test_tweets.csv, filas: {len(df)}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
