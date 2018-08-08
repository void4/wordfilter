from metaphone.metaphone import doublemetaphone

wlfilepath = "wordlists/en.txt"

wordlist = []
with open(wlfilepath) as f:
	for w in f.readlines():
		w = "".join(w.split())
		mp = doublemetaphone(w)
		wordlist.append([w,mp[0].lower(),mp[1]])

lastN = 5
last = []

def filter(s):
	global last
	s1 = doublemetaphone(s)[0].lower()
	cat = "".join(s.split())
	s2 = doublemetaphone(cat)[0].lower()
	s3 = "".join(["".join(l.split()) for l in last])
	slist = [s1,s2,s3]
	for word in wordlist:
		for s in slist:
			if len(word[1])>2 and word[1] in s:
				print(word, s)
				return True # or just replace?
		if word[0] in s.split():
			return True
	
	last.append(s)
	last = last[-lastN:]
	return False

from string import ascii_lowercase
def test():
	for a in ascii_lowercase:
		print(filter(a))
