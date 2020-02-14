import argparse

parser = argparse.ArgumentParser("Reading Arguments")

parser.add_argument('--verbose', help="if you want to run program in verbose mode")
parser.add_argument('-a', help="reading a")

args = parser.parse_args()

print(args.a)

