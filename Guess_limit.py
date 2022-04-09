# Guess the number limit 

guess = ''

secret = '13'     # the secret number
guess_con = 0        #Guess counter 
guess_limit = 3    # guess limit 
out_guess = False # to break the loop
while guess_con < guess_limit and not (out_guess):
	guess = input('Guess the number 1-20: ')
	guess_con +=1 # guess counter update 
	if guess == secret:
		out_guess = True   # Breaking the loop
	else:
		pass

if out_guess == False:  # if out_guess = False still not get it the correcr answer
	print('You lose!')
else:
	print('you win!') # else get it and it will be True 