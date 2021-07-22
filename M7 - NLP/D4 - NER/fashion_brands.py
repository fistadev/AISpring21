# Import libraries
import spacy
import random
from spacy.util import minibatch, compounding
from pathlib import Path
from spacy.training import Example

nlp = spacy.load("en_core_web_sm")

with open("fashion brands.txt") as file:
    dataset = file.read()

doc = nlp(dataset)
print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])

"""
STEP 1 - TRAIN DATA
"""
# Prepare training data

words = [
    ""
]

train_data = []

with open("cars.txt") as file:
    dataset = file.readlines()
    for sentence in dataset:
        print("######")
        print("sentence: ", sentence)
        print("######")
        sentence = sentence.lower()
        entities = []
        for word in words:
            word = word.lower()
            if word in sentence:
                start_index = sentence.index(word)
                end_index = len(word) + start_index
                print("----------------")
                print("word: ", word)
                print("start index:", start_index)
                print("end index:", end_index)
                print("----------------")
                pos = (start_index, end_index, "CAR_BRAND")
                entities.append(pos)
        element = (sentence.rstrip('\n'), {"entities": entities})

        train_data.append(element)
        print('----------------')
        print("element:", element)
        print('################')

"""
STEP 2 - UPDATE MODEL
"""

ner = nlp.get_pipe("ner")

for _, annotations in train_data:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# Train model

pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

with nlp.disable_pipes(*unaffected_pipes):
    for iteration in range(30):
        print("Iteration #", iteration)

        random.shuffle(train_data)
        losses = {}

        batches = minibatch(train_data, size=compounding(4.0, 32.0, 1.001))
        for batch in batches:
            for text, annotations in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                nlp.update([example], losses=losses, drop=0.1)
        print("Losses:", losses)

# Save model to output directory

output_dir = Path("/models/")
if not output_dir.exists():
    output_dir.mkdir()
nlp.to_disk(output_dir)
print("Saved model to", output_dir)