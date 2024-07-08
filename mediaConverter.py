import os
from pydub import AudioSegment
from tqdm import tqdm

def convertToMp3(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    files_to_convert = [f for f in os.listdir(input_directory) if f.lower().endswith(('.wav', '.ogg', '.flac', '.aac', '.m4a','.mp3','.mpeg'))]

    if not files_to_convert:
        print("Nenhum arquivo de áudio encontrado no diretório de entrada.")
        return

    for filename in tqdm(files_to_convert, desc="Converting files"):
        file_path = os.path.join(input_directory, filename)
        try:
            audio = AudioSegment.from_file(file_path)
        except Exception as e:
            print(f"Erro ao abrir o arquivo {file_path}: {e}")
            continue

        output_path = os.path.join(output_directory, os.path.splitext(filename)[0] + '.mp3')

        try:
            audio.export(output_path, format='mp3')
        except Exception as e:
            print(f"Erro ao exportar o arquivo {output_path}: {e}")

if __name__ == "__main__":
    input_directory = "./data"
    output_directory = "./output"
    
    convertToMp3(input_directory, output_directory)
