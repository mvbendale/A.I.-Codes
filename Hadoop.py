import os 

chunk_size = 10 

input_file = "upload/hello.txt"

with open(input_file, "rb") as f:

    i=0

    while True:

        chunk = f.read(chunk_size)

        if not chunk:
            break 
        
        chunk_name = f"storage/chunk{i}"

        with open(chunk_name, "wb") as c:
            c.write(chunk)

        print(f"Created {chunk_name}")
        i +=1

output_file = "download/final.txt"

with open(output_file, "wb") as outfile:

    for j in range(i):

        chunk_name = f"storage/chunk{j}"

        with open(chunk_name, "rb") as infile:
            outfile.write(infile.read())

print("File merged successfully")