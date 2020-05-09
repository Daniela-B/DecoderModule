def split(word): 
    return [char for char in word]  

def decodes(codigo,avanza):
    
	length_iterator = 0 
	decoded_string = ""
	code_upper = codigo.upper()
	decoded_list = split(codigo)
    
    
    
	list_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
	"J", "K","L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
	list_number = ["0", "1" , "2", "3", "4", "5", "6", "7", "8", "9"]

	print ("original chain: " + codigo)
	while length_iterator < len(code_upper):
		
		char_to_explore = decoded_list[length_iterator]
        

		if char_to_explore.isalpha():
			index_list = list_alphabet.index(char_to_explore)
			posicion_letra = index_list + int(avanza)
			if posicion_letra > 25:
				posicion_letra = posicion_letra -26
				decoded_string = decoded_string + list_alphabet[posicion_letra]
			else:
				decoded_string = decoded_string + list_alphabet[posicion_letra]

		if char_to_explore.isdigit():
			index_list = list_number.index(char_to_explore)
			posicion_numero= index_list + int(avanza)
			if posicion_numero > 9:
				posicion_numero = posicion_numero-10
				decoded_string = decoded_string + list_number[posicion_numero]
			else:
				decoded_string = decoded_string + list_number[posicion_numero]
			
		
		length_iterator = length_iterator + 1
        

	print ("decoded chain: " + decoded_string)

def main():
	
	print ("-------- RebelAllianceDecoderModule ---------")
	
	input1 = input("R2 insert the key to decode: ")
	inputMay = input1.upper()
	input_advance = input ("R2 insert the advance key to generate the decode result: ")
	decodes(inputMay,input_advance)


if __name__ == "__main__":
	main()

