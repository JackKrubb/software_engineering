import statistics
import sys

def main():
    if len(sys.argv) < 2:
        print("Give me a file name")
        return
    filename = sys.argv[1]
    try:
        file = open(filename, 'r')
    except:
        print("File not found\n")
        return
    
    data1 = file.read().split('\n')
    data = [int(x) for x in data1]

    print("Statistics Summary\n")
    print("mean: " , statistics.mean(data) , "\n")
    print("std: " , statistics.stdev(data) , "\n")
    print("min: " , min(data) , "\n")
    print("max: " , max(data) , "\n")

main()

