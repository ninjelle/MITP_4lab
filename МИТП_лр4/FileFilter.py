def filter_file_lines(filename, condition_func):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if condition_func(line.strip()):
                yield line.strip()

def is_long_line(line):
    return len(line) > 20

with open('data.txt', 'w', encoding='utf-8') as f:
    f.write("Short line\n")
    f.write("This is a very long line for example\n")
    f.write("Another one\n")
    f.write("And one more very long line for testing\n")

print("Long lines:")
for line in filter_file_lines('data.txt', is_long_line):
    print(f" - {line}")