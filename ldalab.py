import pandas as pd
import json

with open("./LDA_model/tokenDoc548.json", "rt", encoding="UTF8") as f:
    file = json.load(f)
#     tknDoc = json.load(f)
# with open("./LDA_model/tokenDoc19.json") as json_file:
# print(file)
tknDoc = file["data"]
# print(tknDoc)
import gensim.corpora as corpora
# Create Dictionary
id2word = corpora.Dictionary(tknDoc)
# Create Corpus
texts = tknDoc
# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]


##################### topic test ########################
from common import cmm
import gensim
from gensim.models import CoherenceModel
# for i in range(2,30):
lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                        id2word=id2word,
                                        num_topics=9, 
                                        random_state=100,
                                        chunksize=100,
                                        passes=30,
                                        alpha=0.91,
                                        eta=0.91,
                                        per_word_topics=True)

coherence_model_lda = CoherenceModel(model=lda_model, texts=tknDoc, dictionary=id2word, coherence='c_v')

cmm.showTime()
print("coh val : ",coherence_model_lda.get_coherence())
print("num topics: " , len(lda_model.print_topics()))
print()
