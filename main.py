location = "books/frankenstein.txt"  

with open(location) as f:
        content = f.read()
        
words = content.split()

print("Total number of words in file is ",len(words),".")
lower_content = content.lower()

char_count = {}
for char in lower_content:
    if char.isalpha():
          char_count[char]=char_count.get(char,0) + 1
sorted_char_count = dict(sorted(char_count.items()))

for char,count in sorted_char_count.items():
      print(f"The {char} was found {count} times")         