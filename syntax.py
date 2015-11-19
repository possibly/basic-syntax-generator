from random import randint

lexicon = {
  'NP': ['she', 'Fluffy', 'Bob', 'Sally', 'Karl', 'Daniella', 'Allie', 'Tyler', 'Sarah'],
  'N': ['dog', 'cat', 'woman', 'poopie'],
  'Adj': ['fluffy', 'cute', 'gray'],
  'Det': ['the', 'this', 'some'],
  'VP': ['slept', 'barked'],
  'TV': ['liked', 'devoured', 'ate', 'smelled', 'swallowed'],
  'DTV': ['gave', 'sent'],
  'SV': ['thought', 'said'],
  'P': ['to', 'for', 'with', 'on', 'under'],
  'Adv': ['carefully','quickly', 'yesterday']
}

def genSentence():
  return [genNounPhrase()] + [genVerbPhrase()]

def genNounPhrase():
  noun = genNoun()
  if ([n for n in lexicon['N'] if noun == n]):
    determiner = genDeterminer()
    return [determiner, noun]
  else:
    return [noun]

def genVerbPhrase():
  verb = genVerb()
  if ([v for v in lexicon['TV'] if verb == v]):
    return [verb, genNounPhrase()]
  elif([v for v in lexicon['DTV'] if verb == v]): #Beware the Double Object form!
    return [verb, genNounPhrase(), genNounPhrase()]
  else:
    return [verb]

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

print genSentence()