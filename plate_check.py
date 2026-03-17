def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if len(plate)>=2 and len(plate)<=6:
        for n in plate:
            if n==" " or n=="," or n==";" or n=="!" or n=="?" or n==".":
                return False
        if plate.isalnum():
            if '0'<= plate[0]<='9' or '0'<= plate[1]<='9':
                return False
            if 65<=ord(plate[len(plate)-1])<=90 or 97<=ord(plate[len(plate)-1])<=122 and 65<=ord(plate[len(plate)-2])<=90 or 97<=ord(plate[len(plate)-2])<=122:
                return False

main()
