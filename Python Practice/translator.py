acronyms = {'LOL': 'laugh out loud',
            'IDK': "I don't know",
            'OMG': 'Oh my god!',
            'TBH': 'to be honest'}

sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)