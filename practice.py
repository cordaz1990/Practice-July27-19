while j > 0:
  print(i, j)
  
  if word[i] != word2[j]:
     return False
    
   i = i + 1
   j = j - 1
    
 
def has_no_e(word):
    for letter in word:
      if letter == 'e':
         return False
    return True
