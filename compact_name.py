full_name = input()
if len(full_name.split()) == 2:
    full_name = full_name.upper()
    full_name = full_name.split()
    print(full_name[0][0] + "." + full_name[1][0])