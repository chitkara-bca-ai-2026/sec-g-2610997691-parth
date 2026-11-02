# Lab 12 - Document Analysis System

sentence = input("Enter a sentence:\n")
print("==================================================")
print("            DOCUMENT ANALYSIS REPORT              ")
print("==================================================")
print(f"Sentence: {sentence}")
print(f"Total characters: {len(sentence)}")
print("\n--- Character Breakdown ---")

words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

vowels_list = "aeiouAEIOU"

for c in sentence:
    if c in vowels_list:
        vowels += 1
    elif c.isalpha():
        consonants += 1
    elif c.isdigit():
        digits += 1
    elif c.isspace():
        spaces += 1
    else:
        special += 1

total_letters = vowels + consonants
vowel_perc = (vowels / total_letters * 100) if total_letters > 0 else 0

print(f"{'Words:':<20} {words}")
print(f"{'Vowels:':<20} {vowels}")
print(f"{'Consonants:':<20} {consonants}")
print(f"{'Digits:':<20} {digits}")
print(f"{'Spaces:':<20} {spaces}")
print(f"{'Special characters:':<20} {special}")

print("\n--- Summary ---")
print(f"{'Total letters:':<20} {total_letters}")
print(f"{'Vowel percentage:':<20} {vowel_perc:.1f}%")
print("\n==================================================")
print("Analysis Complete!")
print("==================================================")
