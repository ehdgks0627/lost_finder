from gensim.models.word2vec import Word2Vec
import pickle

f = open("word.data", "rb")
words = pickle.load(f)
model = Word2Vec(words, size=500, window=10, min_count=2, workers=4)
model.save("word2vec.model")
print(model.most_similar("가방"))
print(model.most_similar("지갑"))
#model = Word2Vec.load("word2vec.model")
