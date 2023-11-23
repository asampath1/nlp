import spacy
nlp = spacy.load('en_core_web_sm')

doc1 =   nlp(u'Tesla and Anand are buying a startup for $6 million')
for token in doc1 :
    print(token.text,token.pos, token.pos_)
print("")  

doc2 =   nlp(u"This is first sentence. This is second sentence. This is last sentence.")
for sentence in doc2.sents:
    print(sentence)

print("")    
#indexing
print("Third token is ", doc2[2])
print("Fourth token is ",doc2[3])

"""
Use Conda Environment.
This is output for the above code

Tesla 96 PROPN
and 89 CCONJ
Anand 96 PROPN
are 87 AUX
buying 100 VERB
a 90 DET
startup 92 NOUN
for 85 ADP
$ 99 SYM
6 93 NUM
million 93 NUM

This is first sentence.
This is second sentence.
This is last sentence.

Third token is  first
Fourth token is  sentence

"""