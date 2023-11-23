import spacy
nlp = spacy.load('en_core_web_sm')

mystring =   '"We\'re moving to T.N.! and the cost of house/month is \u20B9 1000."'
# To print the INR symbol: print(u'\u20B9')

print(mystring)
print("")

doc1 = nlp(mystring)
for token in doc1:
    print(token.text)

print("")
print("No. of tokens in doc1 is ", len(doc1))

#index stuff

print(doc1[3])
print("")
print(doc1[3:6])


#vocabulary stuff
print(doc1.vocab)
print("")
print(len(doc1.vocab))

#spacy recognizes names and Organizations

print("Spacy not recognizes Rs sign")
print('\n')

doc2 = nlp("Infosys is building a factory in Bengaluru for \u20B91000 crore")
for token in doc2:
    print(token.text, end=' |')

for entity in doc2.ents:
    print(entity)
    print(entity.label_)
    print(str(spacy.explain(entity.label_)))
    print('\n')

print('\n')

print("Spacy recognizes $ sign")
print('\n')

doc3 = nlp("Apple is building a factory in Bengaluru for $10 million")
for token in doc3:
    print(token.text, end=' |')

for entity in doc3.ents:
    print(entity)
    print(entity.label_)
    print(str(spacy.explain(entity.label_)))
    print('\n')

#Chunks - Chunking is the process of grouping similar words together based on the nature of the word. 
doc4 = nlp(u'Automatic cars shift insurance liability towards manufactures.')
for chunk in doc4.noun_chunks:
    print(chunk)

doc5 = nlp(u'Real estate Agents hikes the cost to tenants in Housing market.')
for chunk in doc5.noun_chunks:
    print(chunk)

"""
****OUTPUT for the above code *****

"We're moving to T.N.! and the cost of house/month is ₹ 1000."

"
We
're
moving
to
T.N.
!
and
the
cost
of
house
/
month
is
₹
1000
.
"

No. of tokens in doc1 is  19
moving

moving to T.N.
<spacy.vocab.Vocab object at 0x7fbdd1ea85e0>

775
Spacy not recognizes Rs sign


Infosys |is |building |a |factory |in |Bengaluru |for |₹ |1000 |crore |Infosys
ORG
Companies, agencies, institutions, etc.


Bengaluru
GPE
Countries, cities, states


1000
MONEY
Monetary values, including unit




Spacy recognizes $ sign


Apple |is |building |a |factory |in |Bengaluru |for |$ |10 |million |Apple
ORG
Companies, agencies, institutions, etc.


Bengaluru
GPE
Countries, cities, states


$10 million
MONEY
Monetary values, including unit


Automatic cars
insurance liability
manufactures
Real estate Agents
the cost
tenants
Housing market

"""