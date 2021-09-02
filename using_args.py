import argparse


parser = argparse.ArgumentParser()

parser.add_argument('dogname', help="Your dog's name")
parser.add_argument('-f', '--fetch', help="What should your dog fetch?")
parser.add_argument('--sleep', help="Use this if your dog is asleep", action='store_true', default=False)
args = parser.parse_args()

print(args)


if args.fetch:
    print(f"{args.dogname}! Go get the {args.fetch}!")

if args.sleep:
    print("sleepy poochy")
