class BuffaloEncoding:

	def __init__(self):
		self._encoding_base = "buffalos"

	def _bin_to_buffalo(self, bitstring):
		"""
			Converts a bitstring into a single buffalo
		"""
		return_value = ""
		for i in range(0, 8):
			next_char = self._encoding_base[i]
			if int(bitstring[i]) == 1:
				next_char = next_char.upper()
			return_value += next_char
		return return_value

	def _buffalo_to_int(self, buffalo):
		"""
			Converts a single buffalo to an integer
		"""
		bitstring = ""
		for i in range(0, 8):
			next_char = "0"
			if buffalo[i] == buffalo[i].upper():
				next_char = "1"
			bitstring += next_char
		return int(bitstring, 2)
			
	@staticmethod
	def encode(input_string):
		output_string = ""
		encoding = BuffaloEncoding()
		for character in list(input_string):
			# Convert an ASCII character to its corresponding bitstring
			bitstring = bin(ord(character))[2:].zfill(8)
			output_string += encoding._bin_to_buffalo(bitstring)
		return output_string

	@staticmethod
	def decode(input_string):
		output_string = ""
		encoding = BuffaloEncoding()
		if len(input_string) % len(encoding._encoding_base) != 0:
			raise ValueError("Invalid input length for buffalo encoding.")
		for i in range(0, len(input_string), len(encoding._encoding_base)):
			next_buffalo = input_string[i:i+len(encoding._encoding_base)]
			if next_buffalo.lower() != encoding._encoding_base:
				raise ValueError("Input is not buffalo encoded.")
			output_string += chr(encoding._buffalo_to_int(next_buffalo))
		return output_string

if __name__ == "__main__":
	test_string = "This is a test."
	encoded = BuffaloEncoding.encode(test_string)
	print("[+] Encoded input: {0}".format(encoded))
	decoded = BuffaloEncoding.decode(encoded)
	print("[+] Decoded input: {0}".format(decoded))
