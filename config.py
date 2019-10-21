def transfer_utf8(input_path, output_path, input_encoding = 'gb18030'):
    with open(input_path, encoding=input_encoding) as f1:
        data = f1.read()
        with open(output_path, 'w', encoding='utf8') as f2:
            f2.write(data)