import random
import string

ASCII = string.ascii_letters + string.digits
INPUT_FILE = "test.txt"
OUTPUT_FILE = "cmd.txt"



def main():
    with open(INPUT_FILE, "r") as file:
        script = []
        for line in file:
            script.append(line)
        file.close()
        chars = []
        for item in script:
            for ch in item:
                chars.append(ch)
    with open(OUTPUT_FILE, "w") as file:
        for ch in chars:
            file.write(ch)
            file.write(random.choice(ASCII))



main()