# We'll need this library to randomly sample our outputs later
import random

#listing punctuation to remove
punc = '''!()-[]{};:"\, <>./?@#$%^&*_~'''
filename = "songs/songs70s.txt"

# This should store every sentence in our dataset
with open(filename, "r") as f:
	dataset = f.read().splitlines() 
# This (currently empty) dictionary will eventually map from N-1 words
# to a list of all the words we've seen follow it in our dataset
ngram_mapping = {}

N = 3


# Step through each of the sentences in our dataset
for sentence in dataset:
	# Convert the sentence (a string) into a list of lowercase words
	# We make them all lowercase so that "After" gets treated the same as "after", for instance
	words = [word.lower() for word in sentence.split(" ")]

	for i in range(len(words)):
		for character in words[i]:
			if character in punc:
				newWord = words[i].replace(character, "") 
				words[i] = newWord 

	# This seems complicated but it's not too bad. Basically what we want to do is slide a window
	# of size N over the list of words. The way we do that is by incrementing the starting position
	# of the window by 1, up to the point where it's three away from the end of the list
	for idx in range(len(words) - N + 1):
		# Then this line uses the slice (":") operator to ask for the window of our words list starting
		# at idx and going N-1 words after that (the endpoint of the slice isn't included, which is why we 
		# slice all the way to idx+N)

		#trying to use just one word
		mgram = words[idx:idx+N-1]
		keyMame = mgram[-2]
		if ngram_mapping.get(keyMame):
			existingKey = ngram_mapping.get(keyMame)
			existingKey.append(mgram[-1])
		else:
			ngram_mapping[keyMame] = []
			ngram_mapping[keyMame].append(mgram[-1])

		#for using two words
		# ngram = words[idx:idx+N]
		# keyName = " ".join(ngram[:-1])
		# if ngram_mapping.get(keyName):
		# 	existingKey = ngram_mapping.get(keyName)
		# 	existingKey.append(ngram[-1])
		# else:
		# 	ngram_mapping[keyName] = []
		# 	ngram_mapping[keyName].append(ngram[-1])

		# TODO: we need to take the first (N-1) words of our ngram and record in our dictionary one instance
		# of it being followed by the last word in our ngram. For instance, we would want to add one instance
		# of the word "ago" to our dictionary entry for "three days"
# print(ngram_mapping)
newSong = ['but', 'i']
song_len = 10

randomStart = []
randomKey = random.choice(list(ngram_mapping))

#for using two words
# randomWords = [word for word in randomKey.split(" ")] # split the key into two words separated by a comma
# randomStart = randomWords

#for using one word
randomStart.append(randomKey)

for _ in range(song_len):
	#for using two words
	# cur_context = " ".join(randomStart[-2:])
	
	#for using one word
	cur_m_context = randomStart[-1]

	#for using two words
	# if cur_context not in ngram_mapping:
	# 	break
	# randomStart.append(random.choice(ngram_mapping[cur_context]))

	#for using one word
	if cur_m_context not in ngram_mapping:
		break
	randomStart.append(random.choice(ngram_mapping[cur_m_context]))

# print(randomStart)
song = " ".join(randomStart)
print(song)
	

	