import lyrics, json

file_ = open('data.json', 'r')
f = file_.read()
j = json.loads(f)
out = open('dataset.txt', 'w')

for el in j:
    print('getting', el['name'], '  ',  el['title'])
    out.write(lyrics.get_lyrics(el['name'], el['title']))

print('DONE')