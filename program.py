import argparse
parser=argparse.ArgumentParser(description='random program',)
parser.add_argument("filename",help="The name of the file to process")
args=parser.parse_args()
print(args)
print(args.filename)

try:
    file = open(args.filename,'r')
    print(file)
    data=file.readlines()
    for idx, line in enumerate(data, 1):
        print(f"Line {idx}: {line}")
except FileNotFoundError:
    print("File couldn't be opened")
else:
    file.close()
    print("File closed successfully")
finally:
    print("Execution completed")
