lexicon = {
  'NP': ['she', 'Fluffy', 'Bob', 'Sally'],
  'N': ['dog', 'cat', 'women'],
  'Adj': ['fluffy', 'cute', 'gray'],
  'Det': ['the', 'this', 'some'],
  'VP': ['slept', 'barked'],
  'TV': ['liked', 'devoured'],
  'DTV': ['gave', 'sent'],
  'SV': ['thought', 'said'],
  'P': ['to', 'for', 'with', 'on', 'under'],
  'Adv': ['carefully','quickly', 'yesterday']
}

def genSentence():
  return [genNounPhrase(), genVerbPhrase()]

def genNounPhrase():
  noun = genNoun()
  if ([n for n in lexicon['N'] if noun == n]):
    print noun
    determiner = genDeterminer(noun)
    return [determiner, noun]
  else:
    return [noun]

def genVerbPhrase():
  verb = genVerb()
  if ([v for v in lexicon['TV'] if verb == v]):
    return [verb, genNounPhrase()]
  elif([v for v in lexicon['DTV'] if verb == v]):
    return [verb, genNounPhrase(), genNounPhrase()]
  else:
    return [verb]

def genNoun():
  return 'she'

def genVerb():
  return 'slept'

print genSentence()