def file_line_printer(file):
    with open(file, "r") as f:  # Use 'f' as the file object
        for file_line in f:
            # print(line.strip())
            yield file_line


file_path = "generator_sample_file.txt"

for line in file_line_printer(file_path):
    print(line.strip())
