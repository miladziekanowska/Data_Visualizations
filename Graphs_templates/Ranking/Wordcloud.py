# Libraries
from wordcloud import WordCloud, STOPWORDS
# wordcloud might not be installed in you venv or computer, if it not, pip install it
import matplotlib.pyplot as plt

# Create a list of word
text = open ('unforgiven.txt').read()

fig, wordcloud = plt.subplots()
# Create the wordcloud object
wordcloud = WordCloud(stopwords=STOPWORDS, 
                      background_color = 'white',
                      width=480, 
                      height=480, 
                      margin=0).generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

plt.savefig('Wordcloud_Unforgiven.png')