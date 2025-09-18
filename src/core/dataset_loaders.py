def load_raw_text_data(file_path: str) -> list[str]:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()