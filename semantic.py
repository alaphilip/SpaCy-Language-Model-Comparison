# This program uses two different language models to compare the similarity of words
# It includes comments on the differences between the two models
# These experiments with NLP via SpaCy will be hosted on GitHub as part of my bootcamp
# Its point is to demonstrate my understanding of NLP and the SpaCy library
# And also to question the differences between the two language models

# First, the medium language model is used

# Import spacy library
import spacy

# Define colours so that the results are easier to read
R = '\033[31m' # red - for medium model
O = '\033[33m' # orange - for smaller model

# Load the slightly more advanced language model
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(f"{R}Here are the similarities according to the medium model: ")
# This is the similarity between cat and monkey
print("The similarity between cat and monkey is: ")
print(word1.similarity(word2)) 
# Print my notes on this example
print(f"The similarity is high; expected as they're both animals.")
# This is the similarity between banana and monkey
print("The similarity between banana and monkey is: ")
print(word3.similarity(word2))
print("The similarity is lower; expected as they're not the same category but monkeys and bananas are often collocated.")
# This is the similarity between banana and cat
print("The similarity between banana and cat is: ")
print(word3.similarity(word1))
print("As expected, the similarity here is the lowest of the three.\n")

# Using two for loops to compare a series of words with one another
# First, the example from the documentation
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
 
 for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))
# Second, my own example
print("\nHere is an example of my own: ")
tokens = nlp('bicycle bike motorbike car cab taxi truck aeroplane')
for token1 in tokens:

 for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))
# Print my notes on this example
print("Some of the similarities are interesting - e.g. truck/cab is higher than truck/taxi, which makes sense as big trucks have 'cabs'.")
print("I wonder if car/cab are 'more similar' than car/taxi because they're made up of similar letters.")
print("It was interesting that bike/bicylce are much more similar than bike/motorbike given 'bike' is a component of 'motorbike' and sometimes a synonym for it.")

# Using the similarity function to compare a sentence with a series of other sentences
print("\nNow, the medium model will compare sentences to 'Why is my cat on the car': ")
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ",  similarity)
# Print my notes on the sentence comparison exercise, as done using the first model (medium)
print("I'm surprised the last example sentence is 'more similar' to the original than the first.")
print("The first is also a question wondering about the location of an animal. "
      "But the last is a statement about naming a dog.")

# Second, the small language model is used

# Load the slightly less advanced language model
# I have ordered this program medium then small as requested by my bootcamp
#  To differentiate, I will print the results in a 'less intense' colour
nlp = spacy.load('en_core_web_sm')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(f"{O}\nHere are the similarities according to the small model: ")
# This is the similarity between cat and monkey
print("The similarity between cat and monkey is: ")
print(word1.similarity(word2)) 
# Print my notes on this example
print(f"The similarity is similar to the medium model; expected as they're both animals. "
      "\nThere is a warning message suggesting I use the medium model instead.")
# This is the similarity between banana and monkey
print("The similarity between banana and monkey is: ")
print(word3.similarity(word2))
print("The similarity is actually higher than the previous comparison, which is unusual and unexpected!")
# This is the similarity between banana and cat
print("The similarity between banana and cat is: ")
print(word3.similarity(word1))
print("The similarity of the logically 'least similar' pair is the same as the first comparison. "
      "\nThis is unexpected and suggests the small model is not helpful for this task.")

# Using two for loops to compare a series of words with one another
print("\nNow, onto comparing words within a series within one another.")
# First, the example from the documentation
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
 
 for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))
# Print my notes
print("The results are very different to the medium model, immediately: why is cat more similar to apple than monkey?")
# Second, my own example
print("\nHere is (the same) example of my own: ")
tokens = nlp('bicycle bike motorbike car cab taxi truck aeroplane')
for token1 in tokens:

 for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))
# Print my notes on this example
print("Compared to the previous model (medium) there are some similarities: bicycle and bike are similar."
      "\nHowever, according to the smaller model, the words are much more similar to each other than the medium model suggested.")

print("\nNow, the small model will compare sentences to 'Why is my cat on the car': ")
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ",  similarity)
# Print my notes on the second model (small)'s sentence comparison exercise
print("Compared to the first model (medium) all of the similarity scores are lower."
      "\nHowever, the rankings (most similar to least similar) are quite similar."
      "\nThe 1st, 2nd and 5th most similar sentences are the same, according to both models."
      "\nI think the medium model better matches my expectations with its higher similarity scores."
      "\nThis is because the sentences are similar lengths and are all first person 'speech' about animals and vehicles.")

# Overall notes
print("\nThe medium model behaves more like I would expect it to when comparing similar words."
      "\nIt's also noteworthy that the word similarity comparison prompts a warning message, saying the model has no word vectors loaded."
      "\nThis leads the model to advise using the larger model instead."
      "\nI would concur! But the small model is interesting and possibly useful for non-similarity comparisons, "
      "or for comparing words that are not very similar at all!")