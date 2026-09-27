vcf_data = """##fileformat=VCFv4.2
#CHROM  POS  ID  REF  ALT  QUAL  FILTER  INFO
chr1    100  rs1  A  G  99  PASS  DP=30
chr1    250  rs2  C  T  85  PASS  DP=20
chr2    500  rs3  G  A  92  PASS  DP=40"""

with open("sample.vcf", "w") as file:
    file.write(vcf_data)

file = open("sample.vcf", "r")
lines = file.readlines()
variant_count = 0

for line in lines:

    if line.startswith("#"):
        continue
    variant_count += 1
    columns = line.split()

    chromosome = columns[0]
    position = columns[1]
    reference = columns[3]
    alternate = columns[4]
    quality = float(columns[5])
    filter_status = columns[6]
    info = columns[7]
    if quality >= 90:
      print("High quality variant",columns[2])
    else:
      print("Low quality variant",columns[2])  
    depth = info.split("=")[1]

    print("Read depth:", depth)
    print("Chromosome:", chromosome)
    print("Position:", position)
    print("Mutation:", reference, "→", alternate)
    print("Quality:", quality)
    print("Filter:", filter_status)
    print("Info:", info)
    print()
print("Total variants:",variant_count)    
