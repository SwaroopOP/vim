def edit_distance(str1, str2):
  m, n = len(str1), len(str2)
  dp = [[0] * (n + 1) for _ in range (m + 1)] # Create a DP table

  for i in range(m + 1):
    dp[i][0] = i
  for j in range(n + 1):
    dp[0][j] = j

# Fill the DP table
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if str1[i - 1] == str2[j - 1]: # If characters match, no edit needed
         dp[i][j] = dp[i - 1][j - 1]
      else:  
        dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
  return dp[m][n] 

#Example usage
str1 = "Sunday"
str2 = "Saturday"
min_edit_distance=edit_distance(str1,str2)
print('Edit distance between "{}" and "{}" is {}'.format(str1,str2,min_edit_distance))


#Dictionary of correctly spelled words
dictionary = {"search","engine", "example"}

#Spelling correction function
def spell_correct(word):
  if word in dictionary:
    return word
  closest_word=min(dictionary, key=lambda x:edit_distance(word,x))

  #if the closest word is within edit distance 1, return it as the corrected word
  if edit_distance (word,closest_word) == 1:
    return closest_word

  #if no close match is found, return the orignal word
  return word

def process_query(query):
  words = query.split()
  #correct the spelling of each word in query
  corrected_words= [spell_correct(word) for word in words]
  #join the correcte words back into a single string
  corrected_query=' '.join(corrected_words)
  return corrected_query

#Example usage
def main():
  #user query
  query ="serch enjine exampl"
  print(f"Orignal Query:{query}")
  corrected_query=process_query(query)
  print("Corrected Query:", corrected_query)

if __name__=="__main__":
  main()

