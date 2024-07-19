import os
import PyPDF2
import hashlib

def pdf_to_txt(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
    
    return text

def concatenate_txt_files(txt_contents):
    return "\n\n".join(txt_contents)

def generate_md5(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def main():
    current_directory = os.getcwd()
    all_txt_contents = []
    
    for filename in os.listdir(current_directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(current_directory, filename)
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_path = os.path.join(current_directory, txt_filename)
            
            print(f"Convertendo {filename} in {txt_filename}...")
            txt_content = pdf_to_txt(pdf_path, txt_path)
            all_txt_contents.append(txt_content)
            print(f"Conversione completata: {txt_filename}")
    
    # Concatena tutti i contenuti TXT
    concatenated_content = concatenate_txt_files(all_txt_contents)
    
    # Genera l'hash MD5 del contenuto concatenato
    md5_hash = generate_md5(concatenated_content)
    
    # Crea il file concatenato con il nome hash
    concatenated_filename = f"{md5_hash}.txt"
    with open(concatenated_filename, 'w', encoding='utf-8') as concat_file:
        concat_file.write(concatenated_content)
    
    print(f"\nCreato il file concatenato: {concatenated_filename}")

if __name__ == "__main__":
    main()
