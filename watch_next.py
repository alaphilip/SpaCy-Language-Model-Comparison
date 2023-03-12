# This program is an example of using NLP to generate film similarity scores
# The system will tell you what to watch next based on word vector similarity
# The description of the film is used to generate the similarity score
# And I have been given the description of the film Planet Hulk to start with

# Import the essential SpaCy library to enable NLP
import spacy

# Load the English language medium model
nlp = spacy.load('en_core_web_md')

# Read the text file containing the movie descriptions
with open('movies.txt', 'r') as f:
    movie_descriptions = f.readlines()

# Process the movie descriptions in the file
processed_descriptions = []
for description in movie_descriptions:
# doc is a variable representing a SpaCy 'Doc' object
# The Doc object represents a string passed into the nlp function, after processing by the model
# The Doc object is a container for the linguistic annotations and a sequence of 'Token' objects
# Each token represents a word in the string or punctuation mark
    doc = nlp(description)
# Break down the descriptions into individual words (or tokens) using SpaCy
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    processed_descriptions.append(tokens)

# Define a function that finds the most similar movie to a query description
def find_similar_movie(query_description):
# Process the query description
    query_doc = nlp(query_description)
# Reduce each word to its lemma and remove stop words and punctuation
    processed_query = [token.lemma_ for token in query_doc if not token.is_stop and not token.is_punct]

# Work out the similarity between the query, and each movie
    similarities = []
    for i, description in enumerate(processed_descriptions):
# Convert the processed description to an object
        doc = nlp(' '.join(description))
        similarity = doc.similarity(nlp(' '.join(processed_query)))
        similarities.append((i, similarity))

# Method sorting the movies by similarity score and return the most similar one!
# The similarities list contains tuples where the first element is a title, and the second is the similarity to input
# The sorted function is called on similarities to sort the tuples on the second element
# The key argument is a lambda function that returns the second element of the tuple
# This means that the sorting is done on the similarities scores
# The reverse argument is set to True to sort the list in descending order
# Lastly, the [0] index is used to extract the first tuple from the sorted list
# This is the tuple with the highest similarity score - which is assigned to most_similar
    most_similar = sorted(similarities, key=lambda x: x[1], reverse=True)[0]
    return f"Movie {chr(most_similar[0] + ord('A'))} is the most similar with a similarity score of {most_similar[1]}."

# Demonstrative example usage of this program
query_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
print(find_similar_movie(query_description))
