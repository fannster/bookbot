def get_num_words(text): 
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    characters = {}
  

    for character in lower_text:
        if character not in characters:
            characters[character] = 1
        else:
            character
            characters[character] += 1
    
    return characters

def sort_on(unsorted_dictionary):
    return unsorted_dictionary["count"]

def sort_characters(unsorted_dictionary):
    char_list = [] 
    for k,v in unsorted_dictionary.items():
        new_dict = {"char": k, "count": v}
        char_list.append(new_dict)
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list
    
 
        

    


    

    
    


            
    

