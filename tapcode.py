
def tapcode(message):
	"""This function decodes a tap code message (by using dots [..]) placed as an argument in the function as a string. Each letter must
	be separated by two spaces. Each word must be separated by an asterik ("*") with two spaces on each side of the asterik. The letter
	"c" and "k" use the same code and are to be interpreted depending on the context."""

	tapmap = {'a': '. .', 'b': '. ..', 'c/k': '. ...', 'd': '. ....', 'e': '. .....', 'f': '.. .', 'g': '.. ..', 'h': '.. ...', 'i': '.. ....',
			  'j': '.. .....', 'l': '... .',
			  'm': '... ..', 'n': '... ...', 'o': '... ....', 'p': '... .....', 'q': '.... .', 'r': '.... ..', 's': '.... ...', 't': '.... ....',
			  'u': '.... .....',
			  'v': '..... .', 'w': '..... ..', 'x': '..... ...', 'y': '..... ....', 'z': '..... .....', " ": "*"}
	translated = ""
	message = message.split('  ')
	for word in message:
		for key, value in tapmap.items():
			if word == value:
				translated += key

	return translated


a = tapcode(".. ...  .. ....  *  ..... ....  ... ....  .... .....  *  .... ...  .. ....  ... .  ... .  ..... ....")
print(a.title())

b = tapcode(
	"... .....  ..... ....  .... ....  .. ...  ... ....  ... ...  *  .. ....  .... ...  *  ..... .  . .....  .... ..  ..... ....  *  . ...  ... ....  ... ....  ... .")
print(b.title())
