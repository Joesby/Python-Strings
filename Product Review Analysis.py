#List of reviews given in assignment
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

#List of words given in assignment
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "average", "terrible", "horrible", "awful", "disappointing", "subpar"]

#create new list to store substrings
substring = []

#Task 1: Keyword Highlighter
#Use a for loop to iterate through each element in the reviews list
for i in range(len(reviews)):
    #use the split method to separate each word in each individual element of the reviews list and store them in the substring list
    substring = reviews[i].split()
    
    #iterate through the positive_words list to see if they exist in each element of the substring list
    for j in range(len(positive_words)):
        for k in range(len(substring)):
            #ensure each iteration in the substring list is lowercase to eliminate discrepencies
            if positive_words[j] in substring[k].lower() or positive_words[j] in substring[k].lower():
                #replace the corresponding word with the same word with an uppercase version
                substring[k] = substring[k].upper()
            else:
                pass
    #iterate through the negative_words list to see if they exist in each element of the substring list
    for j in range(len(negative_words)):
        for k in range(len(substring)):
            #ensure each iteration in the substring list is lowercase to eliminate discrepencies
            if negative_words[j] in substring[k].lower() or negative_words[j] in substring[k].lower():
                #replace the corresponding word with the same word with an uppercase version
                substring[k] = substring[k].upper()
            else:
                pass

    #replace the current iteration of the reviews element with the new substring after changes are made, then print it
    reviews[i] = " ".join(substring)
    print(reviews[i])

print()

#Task 2: Sentiment Tally
#define a new function, taking each list of positive and negative words as parameters
def review_count(first_list, second_list):

    #find the length of each list and assign them to new variables
    pos_reviews = len(first_list)
    neg_reviews = len(second_list)

    #print out the number of both positive and negarive words
    print("Number of positive words: " + str(pos_reviews))
    print("Number of negative words: " + str(neg_reviews))

    #return both values as requested
    return pos_reviews, neg_reviews

#call the function
review_count(positive_words, negative_words)

print()

#Task 3: Review Summary
#create a new list for rewiew summaries
review_summaries = []

#iterate through each element of the reviews list
for i in range(len(reviews)):
    #reuse the substring variable to store elements from the reviews list again
    substring = reviews[i]
    #make a variable that determines the default end of a slice that resets upon each loop
    end_slice = 30

    #use a while loop and check if the element of the string is a space, if not incriment the end_slice until it is
    while substring[end_slice].isspace() == False:
        end_slice += 1

    #add a ... to the end of the substring that stops at the first space of a word that contains the 30th character
    substring = substring[0:end_slice] + "..."
    #output to show the results
    print(substring)

    #add the current substring to the review_summaries list
    review_summaries.append(substring)