# Write a function analyze_text(data: list) that receives a list of sentences (strings). Count how many sentences contain the word "python"; return a dictionary with: "total": total number of sentences, "contains_python": number of sentences with the word "python"
def analyze_text(data:list):
    if not isinstance(data, list):
        raise TypeError("Input must be a list of sentences.")
    for sentence in data:
        if not isinstance(sentence, str):
            raise ValueError("All items in the list must be strings.")
    contains_python=0
    for sentence in data:
        new_sentence=sentence.lower().split()#Creates a list that contains the words of a sentence.
        if any("python"==word.strip(".,!?;:()\"'") for word in new_sentence):# Checks whether the sentence contains the word ‘python’.
            contains_python+=1
    dict_text={
        'total':len(data) ,'contains_python': contains_python}
    return dict_text
data1 = [
    "I love programming in Python.",
    "Yesterday I learned Java.",
    "python python is very popular.",
    "This sentence has nothing interesting."
]
try:
    print(analyze_text(data1)) #output is {'total': 4, 'contains_python': 2}
except (TypeError,ValueError) as e:
    print("ERROR:",e)
