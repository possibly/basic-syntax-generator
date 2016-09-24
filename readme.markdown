#Basic syntax generation
My Intro to Linguistics class had a section on syntax and I couldn't resist turning a lot of that simple theory into a quick program that could generate syntacticly correct language.

Later, on the first day on my Syntax 1 class, I thought of a much more clever way of writing this program.

##Usage
`python syntax.py` will run the program and give some test outputs.

The part of the code that provides these outputs are: 

```
print expand(['S', 'S'])
#  pitchfork lied 
#  pig came pitchfork

print expand('S')
# the pig came pitchfork

print expand(['S', ['NP', 'VP']])
#the answer came pig
#the pig
#lied pitchfork
```

Add to the lexicon and grammar without having to change the expand() algorithm. Change the expand() algorithm if you want the formatting / output to look different.