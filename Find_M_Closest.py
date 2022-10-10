import random
import math
import argparse
import Data_Structure as D
if __name__ == '__main__':
    parser = argparse.ArgumentParser()# Add an argument
    parser.add_argument('--file_path', type=str, required=True, help="The path of input file.")# Parse the argument
    parser.add_argument('--num', type=int, required=True, help="The Number of Closest Pair-points want to get.")
    parser.add_argument('--auto', action="store_true", help="Auto-create 100 randomized points.")
    args = parser.parse_args()
    file_path = args.file_path
    m = args.num

    if args.auto:
        D.create_100_random_points(file_path)
    P = D.read_input(file_path)

    result = D.M_Closest_Pair(P, m)
    for item in result:
        print(str(item.pair) + "\tdistance = " + str(item.distance))