def sentence( nounPhrase, verbPhrase ):
  return {'NP': nounPhrase, 'VP': verbPhrase}

def nounPhrase( determiner, noun ):
  return {'Det': determiner, 'N': noun}

def noun( adjective, noun ):
  return {'Adj': adjective, 'N': noun}

def verbPhrase( transVerb ):
  return {'TV': transVerb}

def generate():
  n = noun('smart', 'gorilla')
  np = ('the', n)
  vp = verbPhrase('slept')
  s = sentence(np, vp)
  print(s)

generate()

