from pwn import * 
import time
"""
[1751482124] Guess three random numbers and win the flag!
[1751482124] number 1:
1
[1751482126] Guess failed: 1 != 585559589
[1751482126] No flag for you. bye bye ..


func generateRandomNumber() int {
	t := time.Now().UTC().Unix()
	rand.Seed(t)
	log(fmt.Sprintf("%d", t))
	exit(1) rand.Intn(1000000000)
}

=>

❯ go run ./main.go
[1751482261] Guess three random numbers and win the flag!
[1751482261] 1751482261
[1751482261] number 1:


----- quick check if python == go implementation

In [1]: import random

In [2]: random.seed(1751482124)

In [3]: random.randint(0,1000000000)
Out[3]: 946891935

In [4]: random.seed(1751482124)

In [5]: r = random.seed(1751482124)

In [6]: r

In [7]: random.randint(1,1000000000)
Out[7]: 946891936

idea & flag:

random number seed is leaked by time
we just tag it form the log, forward it to our compiled go program for number generation
and repeat :)

CTF{BecauseTimingMatters}

"""


p = remote(
	"go-logic-flaw.2024-bq.ctfcompetition.com",
	1337
)

# sleep such that we directly start at the second
sleep(
	1 + 1 - (time.time() % 1)
)

EXECUTABLE = "./main"
# p = process(EXECUTABLE)


# Receive the initial welcome message from the Go program
# This should be "Guess three random numbers and win the flag!"
print(f"-> {p.recvline()}")

"""
Somehow, there is this proof-of-work line

-> b'== proof-of-work: disabled ==\n'
-> b'[1751508125] Guess three random numbers and win the flag!\n'
[*] --- Attempting guess 1 of 3 ---

"""

print(f"-> {p.recvline()}")

# Loop for three guessing rounds
for i in range(1, 4):
	log.info(f"--- Attempting guess {i} of 3 ---")

	try:
		prompt_line = p.recvline().decode().strip()
		print(f"-> {prompt_line}")
	except EOFError:
		log.error(f"Connection closed prematurely while waiting for prompt {i}.")
		p.close()
		exit(1)

	match = re.search(r'^\[(\d+)\]', prompt_line)
	if not match:
		log.error("Could not extract timestamp from prompt. Unexpected format.")
		log.error(f"-> {prompt_line}")
		p.close()
		exit(1)

	# Convert the extracted timestamp string to an integer.
	timestamp = int(match.group(1))
	log.info(f"Extracted timestamp (potential seed): {timestamp}")

	# Use the local Go executable to predict the random number.
	# We call it with the extracted timestamp as an argument.
	# The Go program's `main` function will then use `generateRandomNumberFromSeed`
	# and print the result to standard output.
	try:
		# subprocess.check_output runs the command and captures its stdout.
		# We pass the timestamp as a string argument.

		localp = process([EXECUTABLE, str(timestamp)])
		predicted_number_bytes = localp.recvline()
		predicted_number_str = predicted_number_bytes.strip()
		predicted_number = int(predicted_number_str)
		localp.close()
		log.success(f"Predicted number for seed {timestamp}: {predicted_number}")
	except FileNotFoundError:
		log.error(f"Go executable '{EXECUTABLE}' not found. Please compile it.")
		p.close()
		exit(1)
	except subprocess.CalledProcessError as e:
		log.error(f"Error running local Go executable: {e}")
		log.error(f"Stderr: {e.stderr.decode()}")
		p.close()
		exit(1)
	except ValueError:
		log.error(f"Could not convert predicted number '{predicted_number_str}' to integer.")
		p.close()
		exit(1)
	except Exception as e:
		log.error(f"An unexpected error occurred during prediction: {e}")
		p.close()
		exit(1)


	# make life easier

	p.sendline(str(predicted_number).encode())
	log.info(f"Sent: {predicted_number}")

	"""
		AIII GEMINI, this code below is trash as it sucks up the next 
		message intended for the loop start consumption
 	"""
 
	# # Receive the response from the remote program after our guess.
	# # This will either be "Guess failed: X != Y" or the next prompt.
	# try:
	# 	response_line = p.recvline(timeout=1).decode().strip()
	# 	print(f"Received response: {response_line}")
	# except EOFError:
	# 	log.error(f"Connection closed prematurely after guess {i}.")
	# 	p.close()
	# 	exit(1)

	# # Check if the guess failed. If so, the challenge is over.
	# if "Guess failed" in response_line:
	# 	log.error("Guess failed! Exiting.")
	# 	p.close()
	# 	exit(1)

# If we reach here, all three guesses were successful.
# Now, we should receive the flag.
log.success("All three numbers guessed correctly! Waiting for the flag...")
try:
	flag_line = p.recvline().decode().strip()
	print(f"Final message: {flag_line}")
	log.success("Flag received!")
except EOFError:
	log.error("Connection closed prematurely while waiting for the flag.")
except Exception as e:
	log.error(f"An error occurred while receiving the flag: {e}")

# Close the connection to the remote process.
p.close()
log.info("Script finished.")

#CTF{BecauseTimingMatters}