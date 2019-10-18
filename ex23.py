import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip() # string.strip("str"): delate "str" which is at the begining or end of the string
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding = "utf-8")

main(languages, input_encoding, error)

0b1011010
ord('Z')
chr(0b1011010)

languages.seek(0)
print(languages.read().encode("utf-8"))

raw_bytes = b'\xe6\x96\x87\xe8\xa8\x80'
raw_bytes.decode()

utf_string = "文言\n"
c=utf_string.encode()
print(c.strip())


raw_bytes == utf_string.encode()
utf_string == raw_bytes.decode()
