import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import cmudict
import os
import pandas as pd

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('cmudict')

def load_word_list(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        words = {word.strip().lower() for word in file.readlines()}
    return words

def create_sentiment_dict(positive_file, negative_file):
    positive_words = load_word_list(positive_file)
    negative_words = load_word_list(negative_file)
    return positive_words, negative_words

def get_positive_negative_words_in_text(text, positive_words, negative_words):
    words = text.lower().split()
    positive_in_text = {word for word in words if word in positive_words}
    negative_in_text = {word for word in words if word in negative_words}
    return positive_in_text, negative_in_text

def calculate_scores(text, positive_words, negative_words):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    total_words = len(tokens)

    # Positive Score
    positive_score = sum(1 for word in tokens if word in positive_words)

    # Negative Score
    negative_score = sum(1 for word in tokens if word in negative_words)

    # Polarity Score
    polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)

    # Subjectivity Score
    subjectivity_score = (positive_score + negative_score) / (total_words + 0.000001)

    # Average Sentence Length
    sentences = sent_tokenize(text)
    average_sentence_length = total_words / len(sentences)

    # Percentage of Complex Words
    cmu_dict = cmudict.dict()
    complex_words_count = sum(1 for word in tokens if syllable_count(word, cmu_dict) > 2)
    percentage_complex_words = (complex_words_count / total_words) * 100

    # Fog Index
    fog_index = 0.4 * (average_sentence_length + percentage_complex_words)

    # Average Number of Words Per Sentence
    average_words_per_sentence = total_words / len(sentences)

    # Word Count
    word_count = total_words

    # Syllable Count Per Word
    syllable_count_per_word = sum(syllable_count(word, cmu_dict) for word in tokens) / total_words

    # Personal Pronouns
    personal_pronouns = sum(1 for word in tokens if word.lower() in ['i', 'we', 'my', 'ours', 'us'])

    # Average Word Length
    average_word_length = sum(len(word) for word in tokens) / total_words

    return {
        'Filename' : file_name,
        'Positive Score': positive_score,
        'Negative Score': negative_score,
        'Polarity Score': polarity_score,
        'Subjectivity Score': subjectivity_score,
        'Average Sentence Length': average_sentence_length,
        'Percentage of Complex Words': percentage_complex_words,
        'Fog Index': fog_index,
        'Average Number of Words Per Sentence': average_words_per_sentence,
        'Word Count': word_count,
        'Syllable Count Per Word': syllable_count_per_word,
        'Personal Pronouns': personal_pronouns,
        'Average Word Length': average_word_length
    }

def syllable_count(word, cmu_dict):
    if word.lower() in cmu_dict:
        return max([len(list(y for y in x if y[-1].isdigit())) for x in cmu_dict[word.lower()]])
    else:
        # Simple syllable count heuristic
        count = 0
        vowels = 'aeiouy'
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith('e'):
            count -= 1
        if count == 0:
            count += 1
        return count

if __name__ == "__main__":
    positive_file = "Assignment/MasterDictionary/positive-words.txt"  # Path to positive words file
    negative_file = "Assignment/MasterDictionary/negative-words.txt"  # Path to negative words file
    dfs = []
    for file_name in os.listdir('Clean/'): # Path to cleaned text file
        file_path = os.path.join('Clean/', file_name)
        # Load positive and negative words
        positive_words = load_word_list(positive_file)
        negative_words = load_word_list(negative_file)

        # Read cleaned text
        with open(file_path, 'r', encoding='utf-8') as file:
            cleaned_text = file.read()

        # Calculate scores
        scores = calculate_scores(cleaned_text, positive_words, negative_words)
        data = pd.DataFrame([scores])
        dfs.append(data)
        # for key, value in scores.items():
        #     print(f"{key}: {value}")

        positive_words, negative_words = create_sentiment_dict(positive_file, negative_file)
        positive_in_text, negative_in_text = get_positive_negative_words_in_text(cleaned_text, positive_words, negative_words)

        # print("Positive Words Found in Text:")
        # print(positive_in_text)
        # print("\nNegative Words Found in Text:")
        # print(negative_in_text)

final_df = pd.concat(dfs, ignore_index=True)
# Save to Excel file
output_file = "analysis_results.xlsx"
final_df.to_excel(output_file, index=False)
print(f"Analysis results saved to {output_file}")