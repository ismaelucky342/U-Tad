from data_extractor import DataExtractor
import os

# para facilitar la evalucación
# export RAPIDAPI_KEY="clave api"
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
