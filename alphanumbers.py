#!/usr/bin/python

#Paul Croft
#September 16, 2014

import sys

#reserved numbers
numbers = {
	0:"zero",
	1:"one",
	2:"two",
	3:"three",
	4:"four",
	5:"five",
	6:"six",
	7:"seven",
	8:"eight",
	9:"nine",
	10:"ten",
	11:"eleven",
	12:"twelve",
	13:"thirteen",
	14:"fourteen",
	15:"fifteen",
	16:"sixteen",
	17:"seventeen",
	18:"eighteen",
	19:"nineteen",
	20:"twenty",
	30:"thirty",
	40:"fourty",
	50:"fifty",
	60:"sixty",
	70:"seventy",
	80:"eighty",
	90:"ninety"}

places = (
	(1000000000000,"trillion ",),
	(1000000000,"billion ",),
	(1000000,"million ",),
	(1000,"thousand ",),
	(100,"hundred ",),
#	(10,""),
	)

def stringnumber(inint):
	if inint < 0:
		return "%s %s" % ("negative",stringnumber(inint * -1),)
	if inint in numbers:
		return numbers[inint]
	for value, place in places:
		if inint > value:
			return "%s %s%s" % (stringnumber(inint / value),place, stringnumber(inint % value),)
	#special case for unreserved numbers under 100
	return "%s %s" % (stringnumber(inint - (inint % 10)),numbers[inint % 10],)


def main():
    if not sys.argv[1:]:
        sys.stderr.write("Must pass at least one number\n")
        exit(1)
    #Test for integerability
    try:
        inputs = map(int,sys.argv[1:])
    except ValueError:
        sys.stderr.write("That's not an integer\n")
        exit(2)

    for i in inputs:
         print stringnumber(i)

    return 0

if __name__ == "__main__":
    exit(main())
