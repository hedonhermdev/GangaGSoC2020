def mergefiles(file_list, output_file):
    sum = 0
    f_out = open(output_file, "w")
    for f in file_list:
        f_in = open(f, "r")
        sum += int(f_in.read().strip())
        f_in.close()
    f_out.write(str(sum))
    f_out.close()
    return True
