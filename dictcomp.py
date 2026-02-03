import re

def simple_compress(input_text):
    # Regex to separate words and punctuation tokens
    #tokens = re.findall(r"[\w']+|[.,!?;:\"\-()\[\]\n]", input_text)
    tokens = input_text.split()

    print(f"Tokens: {tokens}")
    dictionary = {}
    compressed_data = []
    current_id = 0

    for token in tokens:
        if token not in dictionary:
            dictionary[token] = current_id
            current_id += 1
        compressed_data.append(dictionary[token])
    
    print(f"Dictionary: {dictionary}")

    return dictionary, compressed_data

def save_compressed_files(dictionary, data, dict_path, data_path):
    # Save the dictionary (Key: ID)
    with open(dict_path, 'w', encoding='utf-8') as f:
        for word, idx in dictionary.items():
            f.write(f"{idx}:{word}\n")
            
    # Save the compressed numeric data
    with open(data_path, 'w', encoding='utf-8') as f:
        f.write(",".join(map(str, data)))

# --- Execution Example ---
#text_input = """Hello world! Hello again. This is a test, world."""
text_input = """Hello world Hello again This is a test world"""
print(f"Text input: {text_input}")
# 1. Compress
word_dict, numeric_sequence = simple_compress(text_input)

# 2. Save to files
save_compressed_files(word_dict, numeric_sequence, 'dictionary.txt', 'compressed.dat')

print("Compression Complete.")
print(f"Dictionary Size: {len(word_dict)} entries")
print(f"Compressed Sequence: {numeric_sequence}")