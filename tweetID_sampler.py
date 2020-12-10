import random

quantity = input("How many IDs do you want to sample?\n")
quantity = int(quantity)
sourcefile = input("Enter the filename containing the tweet IDs\n")
destfile = input("Enter filename to save to\n")

with open(sourcefile) as f:
	lines = random.sample(f.readlines(), quantity)

with open(destfile, "w") as f:
	for i in lines:
		f.write(i)
