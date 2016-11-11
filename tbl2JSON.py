from bs4 import BeautifulSoup
import json
import sys

def byteify(input):
    #Removes unicode encodings from the given input string.
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def produceJSON():
	html = open(sys.argv[1], "r")
	soup = BeautifulSoup(html, 'html.parser')

	words = {
		td.text:
		td.find_next('td').text for td in soup('td', 'text-rgh')
		}
	
	json_input = byteify(words)

	#testing
	print(json.dumps(json_input, indent = 4, ensure_ascii=False))
	
	file_prefix = (sys.argv[1]).partition(".")[0]
	with open(file_prefix + '.JSON', 'w') as outfile:
		json.dump(json_input, outfile, indent = 4, ensure_ascii=False)

if __name__ == "__main__":
	produceJSON()