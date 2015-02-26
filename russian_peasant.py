import sys

def run(arg1, arg2):

	divider = arg1 if arg1 >= arg2 else arg2
	multiplier = arg2 if arg1 >= arg2 else arg1

	print 'running for {} {}'.format(divider, multiplier)

	total = 0
	while divider >= 1:
		if not divider % 2 == 0:
			total = total + multiplier
		divider = divider / 2
		multiplier = multiplier * 2

	print total
	print arg1 * arg2

if __name__ == '__main__':
	run(int(sys.argv[1]), int(sys.argv[2]))

