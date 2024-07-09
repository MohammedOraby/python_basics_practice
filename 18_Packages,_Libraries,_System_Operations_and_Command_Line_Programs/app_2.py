import sys
sys.argv

if len(sys.argv) < 3:
    print("plz enter at least 2 numbers")

else:
    total = 0
    for number in sys.argv[1:]:
        total += float(number)
    print(f"total : {total}")