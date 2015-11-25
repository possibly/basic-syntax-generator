from random import randint
from sys import argv

lexicon = {
  'NP': ['Tyler', 'the ball'],
  'N': ['cat'],
  # 'Adj': ['fluffy', 'cute', 'gray'],
  'Det': ['the', 'this', 'some'],
  'VP': ['slept', 'barked'],
  'TV': ['ate', 'smelled'],
  'DTV': ['gave', 'sent'],
  'SV': ['thought', 'said'],
  # 'P': ['to', 'for', 'with', 'on', 'under'],
  # 'Adv': ['carefully','quickly', 'yesterday']
}

'''
Generating the syntax tree.
'''
def genSentence():
  return ('nounPhrase', genNounPhrase(), 'verbPhase', genVerbPhrase())

def genNounPhrase():
  noun = genNoun()
  if ([n for n in lexicon['N'] if noun == n]):
    return ('determiner', genDeterminer(), 'noun', noun)
  else:
    return ('noun', noun)

def genVerbPhrase():
  verb = genVerb()
  if ([v for v in lexicon['TV'] if verb == v]):
    return ('transitiveVerb', verb, 'nounPhrase', genNounPhrase())
  elif([v for v in lexicon['DTV'] if verb == v]): #Beware the Double Object form!
    return ('ditransitiveVerb', verb, 'nounPhrase', genNounPhrase(), 'nounPhrase', genNounPhrase())
  else:
    return ('intransitiveVerb', verb)

def genNoun(nounType='any'):
  if (nounType == 'any'):
    if (randint(0,1) == 0): nounType = 'NP'
    else: nounType = 'N'
  return lexicon[nounType][ randint(  0,  len(lexicon[nounType])-1  ) ]

def genVerb(verbType='any'):
  if (verbType == 'any'):
    coinToss = randint(0,2)
    if (coinToss == 0): verbType = 'VP'
    elif (coinToss == 1): verbType = 'TV'
    else: verbType = 'DTV'
  return lexicon[verbType][ randint(  0,  len(lexicon[verbType])-1  ) ]

def genDeterminer():
  return lexicon['Det'][randint(0,len(lexicon['Det'])-1)]

'''
Prepping the syntax tree for string output.
'''
def leaves(sentence):
  # Break each descriptor down until it is of type noun, determiner or verb, then print that value.
  if (sentence[0] == 'noun'):
    return sentence[1]
  if (sentence[0] == 'determiner'):
    return sentence[1] +' '+ sentence[3]
  if ('Verb' in sentence[0]):
    return findChildren(sentence[1] + ' ', sentence)
  else:
    return findChildren('', sentence)

def findChildren(leaf, sentence):
  children = filter(lambda part: type(part) == tuple, sentence)
  for child in children:
    leaf += leaves(child) + ' '
  return leaf

'''
Using the syntax generator via the command line.
'''
times = 1
try:
  times = int(argv[1])
except: None

while times > 0:
  sentence = genSentence()
  print leaves(sentence)
  if(len(argv) > 2 and argv[2] == 'tree'):
    print sentence
  times -= 1