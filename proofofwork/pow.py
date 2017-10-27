import hashlib
import time

max_nonce = 2**32 # 2^32, or approx. 4 billion

def proof_of_work(header, difficulty_num):
	# If difficulty is 1, target = max target, otherwise it's smaller
	target = 2**(256-difficulty_num)
	# 224 is actually the maximum number for Bitcoin, but that takes too long
	# to mine for this basic proof-of-concept program so I increased the number

	# for each nonce value until you reach the max nonce:
	for nonce in xrange(max_nonce):
		# combine the block header and the nonce and hash that
		hash_result = hashlib.sha256(str(header)+str(nonce)).hexdigest()

		# this long() function constructs a long integer w/the hash result in base-16
		# if it's less than the target:
		if long(hash_result, 16) < target:
			# you found a block hash! yay!!!
			print "Success with nonce %d" % nonce
			print "Hash: %s" % hash_result
			return (hash_result, nonce)

if __name__ == '__main__':

	nonce = 0;
	hash_result = ''

	# 2**32 is the max nonce, so increment this number until it reaches 32
	# The difficulty is 2^0, 2^1, 2^2, ... 2^32... so it keeps getting harder
	for difficulty_num in xrange(32):
		difficulty = 2**difficulty_num

		# Print the difficulty for this current round
		print ""
		print "Difficulty: %ld (current num %d)" % (difficulty, difficulty_num)
		print "Starting search..."
		start = time.time()

		new_block = 'test block header' + hash_result
		# The hash result and nonce are given values once the proof of work
		# algorithm has been completed
		(hash_result, nonce) = proof_of_work(new_block, difficulty_num)
		# Once the proof of work algorithm has been completed, you are done
		# with this round. Print the elapsed time and start over with a new
		# difficulty
		end = time.time()
		elapsed_time = end - start
		# %.2f means to convert to floating point + consider only the first 2
		# digits
		print "Elapsed time: %.2f seconds" % elapsed_time
