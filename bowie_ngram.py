# We'll need this library to randomly sample our outputs later
import random

#listing punctuation to remove
punc = '''!()-[]{};:"\, <>./?@#$%^&*_~'''

# This should store every sentence in our dataset

dataset = [
	"It's a God-awful small affair To the girl with the mousy hair But her mummy is yelling No! And her daddy has told her to go But her friend is nowhere to be seen Now she walks through her sunken dream To the seat with the clearest view And she's hooked to the silver screen But the film is a sadd'ning bore For she's lived it ten times or more She could spit in the eyes of fools As they ask her to focus on Sailors fighting in the dancehall Oh, man! Look at those cavemen go It's the freakiest show Take a look at the Lawman beating up the wrong guy Oh, man! Wonder if he'll ever know Who's in the best-selling show Is there life on Mars? It's on America's tortured brow That Mickey Mouse has grown up a cow Now the workers have struck for fame 'Cause Lennon's on sale again See the mice in their million hordes From Ibiza to the Norfolk Broads Rule Britannia is out of bounds To my mother, my dog, and clowns But the film is a sadd'ning bore 'Cause I wrote it ten times or more It's about to be writ again As I ask you to focus on Sailors fighting in the dancehall Oh, man! Look at those cavemen go It's the freakiest show Take a look at the Lawman beating up the wrong guy Oh, man! Wonder if he'll ever know Who's in the best-selling show Is there life on Mars?",
	"Still don't know what I was waiting for And my time was running wild A million dead-end streets and Every time I thought I'd got it made It seemed the taste was not so sweet So I turned myself to face me But I've never caught a glimpse How the others must see the faker I'm much too fast to take that test Ch-ch-ch-ch-changes Turn and face the strange Ch-ch-changes Don't want to be a richer man Ch-ch-ch-ch-changes Turn and face the strange Ch-ch-changes Just gonna have to be a different man Time may change me But I can't trace time Ooh yeah I watch the ripples change their size But never leave the stream Of warm impermanence and So the days float through my eyes But still, the days seem the same And these children that you spit on As they try to change their worlds Are immune to your consultations They're quite aware what they're going through Ch-ch-ch-ch-changes Turn and face the strange Ch-ch-changes Don't tell them to grow up and out of it Ch-ch-ch-ch-changes Turn and face the strange Ch-ch-changes Where's your shame? You've left us up to our necks in it Time may change me But you can't trace time Strange fascination fascinating me Oh, changes are taking the pace I'm going through Ch-ch-ch-ch-changes Turn and face the strange Ch-ch-changes Oh, look out you rock 'n' rollers Ch-ch-ch-ch-changes Turn and face the strange Ch-ch-changes Pretty soon now, you're gonna get older Time may change me But I can't trace time I said that time may change me But I can't trace time",
	"Wake up, you sleepy head Put on some clothes, shake up your bed Put another log on the fire for me I've made some breakfast and coffee I look out my window, what do I see? A crack in the sky and a hand reaching down to me All the nightmares came today And it looks as though they're here to stay What are we coming to No room for me, no fun for you I think about a world to come Where the books were found by the golden ones Written in pain, written in awe By a puzzled man who questioned what we work here for All the strangers came today And it looks as though they're here to stay Oh, you pretty things (Oh, you pretty things) Don't you know you're driving your mamas and papas insane Oh, you pretty things (Oh, you pretty things) Don't you know you're driving your mamas and papas insane Let me make it plain, you got to make way for the Homo superior Look out at your children See their faces in golden rays Don't kid yourself, they belong to you They're the start of a coming race The earth is a bitch, we've finished our news Homo sapiens have outgrown their use All the strangers came today And it looks as though they're here to stay Oh, you pretty things (Oh, you pretty things) Don't you know you're driving your mamas and papas insane Oh, you pretty things (Oh, you pretty things) Don't you know you're driving your mamas and papas insane Let me make it plain, you got to make way for the Homo superior",
	"I'm an alligator, I'm a mama-papa coming for you I'm a space invader, I'll be a rock 'n' rollin' bitch for you Keep your mouth shut, you're squawking like a pink monkey bird And I'm busting up my brains for the words Keep your 'lectric eye on me, babe Put your ray gun to my head Press your space face close to mine, love Freak out in a moonage daydream, oh yeah Don't fake it baby, lay the real thing on me The church of man love is such a holy place to be Make me, baby, make me know you really care Make me jump into the air Keep your 'lectric eye on me, babe Put your ray gun to my head Press your space face close to mine, love Freak out in a moonage daydream, oh yeah Keep your 'lectric eye on me, babe Put your ray gun to my head Press your space face close to mine, love Freak out in a moonage daydream, oh yeah Keep your 'lectric eye on me, babe Put your ray gun to my head Press your space face close to mine, love Freak out in a moonage daydream, oh yeah Freak out Far out In out"
	]

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
		ngram = words[idx:idx+N]

		keyName = " ".join(ngram[:-1])
		if ngram_mapping.get(keyName):
			existingKey = ngram_mapping.get(keyName)
			existingKey.append(ngram[-1])
		else:
			ngram_mapping[keyName] = []
			ngram_mapping[keyName].append(ngram[-1])

		# TODO: we need to take the first (N-1) words of our ngram and record in our dictionary one instance
		# of it being followed by the last word in our ngram. For instance, we would want to add one instance
		# of the word "ago" to our dictionary entry for "three days"

newSong = ['but', 'i']
song_len = 25

randomStart = []
randomKey = random.choice(list(ngram_mapping))
randomWords = [word for word in randomKey.split(" ")] # split the key into two words separated by a comma
randomStart = randomWords

for _ in range(song_len):
	cur_context = " ".join(randomStart[-2:])

	if cur_context not in ngram_mapping:
		break

	randomStart.append(random.choice(ngram_mapping[cur_context]))


print(randomStart)
	

	