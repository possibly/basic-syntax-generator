from random import randint

lexicon = {
  'N': ['pig', 'answer', 'pitchfork'],
  'V': ['knew', 'lied', 'came', 'became'],
  'D': ['the', 'a']
}

PSG = {
  'S': ['NP', 'VP'],
  'VP': ['V', '(NP)'],
  'NP': ['(D)', 'N']
}

def expand(phrase):
  if '(' in phrase and ')' in phrase:
    if randint(0,1) == 1:
      word_set = lexicon[phrase[1:2]]
      return word_set[randint(0, len(word_set)-1)]
    else:
      return ''
  elif ('N' in phrase or 'V' in phrase or 'D' in phrase) and ('P' not in phrase):
      return lexicon[phrase][randint(0, 2)]
  try:
    expandedPhrases = map(expand, PSG[phrase])
    return ' '.join(expandedPhrases)
  except:
    expandedPhrases = map(expand, phrase)
    return '\n'.join(expandedPhrases)


print expand(['S', 'S'])
#  pitchfork lied 
#  pig came pitchfork

print expand('S')
# the pig came pitchfork

print expand(['S', ['NP', 'VP']])
#the answer came pig
#the pig
#lied pitchfork
