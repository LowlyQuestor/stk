# this program subtracts 1 from 100 until it reaches 0 in the stack machine
1 100 sub # subtract 1 from 100
rpush # put the result to RSTK
0 fetch # grab the 1 (the first element in memory)
rpop # pop what's in RSTK
sub # subtract the 1 from that value
dup # duplicate the results
rpush # save the duplicate in RSTK
4 swap # prepare to jump back in the program
0 bne # jump back if the results are not equal to 0
