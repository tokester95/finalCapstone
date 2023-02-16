# running code to practice spacy similarity concepts
import spacy

nlp = spacy.load('en_core_web_sm')

# master comparison sentence
sentence_to_compare = "will he save their world or destroy it? When the Hulk becomes too dangerous for the earth,\n" \
                      "the illuminati trick Hulk into a shuttle and launch him into space to a planet where the \n" \
                      "Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold \n" \
                      "into slavery and trained as a gladiator."

# Comparison sentences
sentences = [
    "Movie A :When Hiccup discovers Toothless isn't the only Night Fury, he must seek The Hidden World\n"
    "a secret Dragon Utopia before a hired tyrant named Grimmel finds it first."
    "Movie B :After the death of Superman, several new people present themselves as possible successors."
    "Movie C :A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic\n"
    " director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare.\n"
    " Others will finally wake up."
    "Movie D :A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes\n"
    " and Doctor Watson."
    "Movie E :A 16-year-old girl and her extended family are left reeling after her calculating grandmother\n"
    " unveils an array of secrets on her deathbed."
    "Movie F :In the last moments of World War II, a young German soldier fighting for survival finds a\n"
    " Nazi captain's uniform. Impersonating an officer, the man quickly takes on the monstrous identity\n"
    " of the perpetrators he is trying to escape from."
    "Movie G :The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes."
    "Movie H :A musician helps a young singer and actress find fame, even as age and alcoholism send his own career\n"
    " into a downward spiral."
    "Movie I :Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until\n"
    " her uncle arrives with a handsome stranger in tow."
    "Movie J :Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and\n"
    " tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney."
]

# Comparison sentence coding
model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
    
# Github link https://github.com/tokester95/finalCapstone/upload/main
