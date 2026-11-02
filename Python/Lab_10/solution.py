# Lab 10 - Text Processing Tool

print("==========================================")
print("          TEXT PROCESSING TOOL            ")
print("==========================================")

sentence = input("Enter a sentence: ")

print("\n--- Processing Results ---")
pos = int(input("Enter position for indexing: "))
print(f"Character at position {pos} : '{sentence[pos]}'")

start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing   : "))
print(f"Sliced string [{start}:{end}]        : '{sentence[start:end]}'")

print(f"Uppercase                     : {sentence.upper()}")
print(f"Lowercase                     : {sentence.lower()}")

word = input("Enter word to replace         : ")
replacement = input("Enter replacement word        : ")
print(f"After replace                 : {sentence.replace(word, replacement)}")
print(f"Length of sentence            : {len(sentence)}")

print("\n==========================================")
print("Analysis Complete!")
print("==========================================")
