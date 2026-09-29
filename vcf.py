vcf_data = """##fileformat=VCFv4.2
#CHROM  POS  ID  REF  ALT  QUAL  FILTER  INFO
chr1    100  rs1  A  G  99  PASS  DP=30
chr1    250  rs2  C  T  85  PASS  DP=20
chr2    500  rs3  G  A  92  PASS  DP=40"""

# Create VCF file
with open("sample.vcf", "w") as file:
    file.write(vcf_data)

# Read VCF file
file = open("sample.vcf", "r")
lines = file.readlines()

variant_count = 0
high_quality_count = 0
total_quality = 0

for line in lines:

    # Skip header lines
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

    # Add quality to total
    total_quality += quality

    # Check quality
    if quality >= 90:
        high_quality_count += 1
        print("High quality variant:", columns[2])
    else:
        print("Low quality variant:", columns[2])

    # Extract read depth
    depth = info.split("=")[1]

    print("Read depth:", depth)
    print("Chromosome:", chromosome)
    print("Position:", position)
    print("Mutation:", reference, "→", alternate)
    print("Quality:", quality)
    print("Filter:", filter_status)
    print("Info:", info)
    print()

# Calculate average quality
average_quality = total_quality / variant_count

print("Total variants:", variant_count)
print("High quality variants:", high_quality_count)
print("Average quality:", round(average_quality, 2))

file.close()
