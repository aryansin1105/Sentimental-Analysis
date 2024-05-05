import os

def load_stop_words(stop_words_folder):
    stop_words = set()
    for file_name in os.listdir(stop_words_folder):
        with open(os.path.join(stop_words_folder, file_name), 'r', encoding='utf-8', errors='ignore') as file:
            stop_words.update(word.strip() for word in file)
    return stop_words

def clean_text(input_file, output_file, stop_words):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile:
        text = infile.read()

    cleaned_text = ' '.join(word for word in text.split() if word.lower() not in stop_words)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(cleaned_text)

if __name__ == "__main__":
    stop_words_folder = "Assignment/StopWords"  # Change this to the folder containing your stop word files
    for file_name in os.listdir('Files/'):
        file_path = os.path.join('Files/', file_name)
        stop_words = load_stop_words(stop_words_folder)
        output_file = f'Clean/{file_name}'
        clean_text(file_path, output_file , stop_words)
        

