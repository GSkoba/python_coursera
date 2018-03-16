import sys
num_steps = int(sys.argv[1])

count_of_lattice = 1
count_of_blob = num_steps-1

while num_steps > 0:
    print(" "*count_of_blob+"#"*count_of_lattice)
    count_of_blob-=1
    count_of_lattice+=1
    num_steps-=1