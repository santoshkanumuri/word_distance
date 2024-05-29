import nltk
import streamlit as st
st.title("Word Distance")
# Get the paragraph from the user
para = st.text_area("Enter a paragraph:")

# Tokenize the paragraph
tokens = nltk.word_tokenize(para)
# Create a frequency distribution of the tokens
fdist = nltk.FreqDist(tokens)
arr=[]
# Print the frequency of every word and position of each appearance
for word, freq in fdist.items():
    positions = [i for i, token in enumerate(tokens) if token == word]
    arr.append(f"{word}: {positions}")
if(st.button("Show")):
    st.write(arr)

