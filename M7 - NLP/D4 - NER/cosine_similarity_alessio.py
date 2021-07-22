import spacy
import numpy as np


def semantic_sim(u,v):
    return (u @ v) / (np.sqrt(sum(u**2)) * np.sqrt(sum(v**2)))

def sentence_similarity(sent1, sent2):
    nlp = spacy.load("en_core_web_sm")

    # tokenization
    sent1_list = nlp(sent1) 
    sent2_list = nlp(sent2)
    # print('lists: ', sent1_list, sent2_list)

    # remove stop words from the string
    sent1set = {w.lemma.lower() for w in sent1_list if not w.is_punct and not w.is_stop and not w.text.isdigit()} 
    sent2set = {w.lemma.lower() for w in sent2_list if not w.is_punct and not w.is_stop and not w.text.isdigit()} 
    # print('sets: ', sent1_set, sent2_set)

    sent_sims = []

    # form a set containing keywords of both strings
    for w1 in sent1set:
        word_sim = 0
        w1 = nlp(w1)

        for w2 in sent2set:
            w2 = nlp(w2)
            # print('words: ', w1, w2)
            u = w1.vector
            v = w2.vector
            ss = semantic_sim(u, v)
            # print('ss: ', ss)
            # print(ss > word_sim)
            if ss > word_sim:
                word_sim = ss
        sent_sims.append(word_sim)

    return(sum(sent_sims)/len(sent_sims))