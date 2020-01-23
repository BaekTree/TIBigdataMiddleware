# import sys
# import os
# file_dir = os.path.dirname(__file__)
# print(file_dir)
# import sys
# sys.path.insert(0, '/path/to/application/app/folder2')

# # import dill
# import os
# path = os.getcwd()
# print("cur dic in ldalab : ", path)
# from pathlib import Path
# print(Path(path).parent)
# print("curdir : " , curDir[-1])
# fileName = os.getcwd().split()[0] + "\\LDA_model\\text.txt"
# with open(fileName,'wb') as f:
#     dill.dump("fuciking work asshole", f)
# print(fileName+"\\LDA_model")
# LDA lab
import json
import LDA as lda
# path = os.getcwd()
# print("cur dic after import LDA : ", path)
lda.LDA(600,5,3)
# import gensim
# ldamodel = gensim.models.ldamodel.LdaModel.load("./LDA_model/c19i5t3")
# # print(ldamodel.show_topics())
# if __name__ == "__main__":
#     main()


# with open("./LDA_model/tokenDoc19.json", "rt", encoding="UTF8") as f:
#     tknDoc = json.load(f)
# tknDoc = tknDoc["data"]

# from gensim import corpora
# id2word = corpora.Dictionary(tknDoc)#문서 별 각 단어에 고유 id 부여
# # id2word = [dictionary.doc2bow(text) for text in corpus]# 문서를 벡터화?
# # # with open("./LDA_model/word2Vec29.json",  "rt", encoding="UTF8") as f:
# # #     id2word = json.load(f)
# # # id2word = id2word["data"]
# # # from gensim.corpora import Dictionary
# # # id2word = Dictionary.load_from_text("./LDA_model/c29i5t3.id2word")

# # id2word = gensim.models.ldamodel.LdaModel.load("./LDA_model/c29i5t3.id2word")
# from gensim.models import CoherenceModel
# coherence_model_lda = CoherenceModel(model=ldamodel, texts=tknDoc, dictionary=id2word, coherence='c_v')
# coherence_lda = coherence_model_lda.get_coherence()
# print('\nCoherence Score: ', coherence_lda)


# import gensim
# from gensim.test.utils import datapath

# # # Save model to disk.
# temp_file = datapath("model")
# ldamodel = gensim.models.ldamodel.LdaModel.load(temp_file)
# # # ldamodel.print_topics
# topics = ldamodel.show_topics(num_words=10, formatted=False)
# print("each topics word prob distribution")
# for i in topics:
#     print(i)
#     print()

# print()
# print("top topics")
# print(type(ldamodel.top_topics()))
# # # print(type(topics))
# # # topics[i][1]
# # wordListTpl = topics[i][1]
# # wordList=[]
# # for wordTpl in wordListTpl:
# #     print(wordTpl[0])
# #     wordList.append(wordTpl[0])
# # print(wordList)




# """
# LDA resut = [
#     {
#         "topic ":0, 
#         "docs" : [
#                     {
#                         "doc" : 1,
#                         "words " : ["a", "b", ...],
#                     }

#                  ]
#     }


# ]
# """
# # lda.LDA(5,10,2)

# # # download LDA result if Tru
# # DOWNLOAD_OPTION = True 
# # # Frontend directory to store LDA result
# # DIR_FE = "../TIBigdataFE/src/assets/special_first/data.json"

# # #OFFLINE_MODE
# # # use sample data in ./raw data sample, and not connet to ES.
# # # without HGU-WLAN network, use raw data sample no matter this value
# # BACKEND_CONCT = True

# # #RANDOM_MODE
# # # 알고리즘 정확성 확인을 위해서 문서를 불러와서 순서를 섞는다.
# # RANDOM_MODE = False


# # # Sample Raw Data from Backend directory
# # DIR_SMP_DATA = "./raw data sample/rawData.json"

# # import time
# # from konlpy.tag import Okt

# # titles = []
# # contents = []
# # start = time.time()


# # # time taken evaluation
# # def showTime():
# #     global start
# #     seconds = time.time() - start
# #     m, s = divmod(seconds, 60)
# #     h, m = divmod(m, 60)
# #     # print("투입된 문서의 수 : %d\n설정된 Iteratin 수 : %d\n설전된 토픽의 수 : %d" %(NUM_DOC, NUM_ITER, NUM_TOPICS))
# #     print("%d 시간 : %02d 분 : %02d 초 " % (h, m, s))
# # # Phase 1 : ES에서 문서 쿼리 및 content와 title 분리 전처리
# # def loadData():
# #     #if internet connection failed to backend    
# #     import json
# #     import sys
# #     import traceback
# #     global NUM_DOC
# #     print("데이터 로드 중...")
# #     try :
# #         if BACKEND_CONCT == False:
# #             raise Exception("서버 연결 옵션 False")
# #         corpus = esFunc.esGetDocs(NUM_DOC)
# #         print("connection to Backend server succeed!")
# #         print(len(corpus),"개의 문서를 가져옴")# 문서의 수... 내용 없으면 뺀다...

# #     except Exception as e:
# #         # traceback.print_exc()
# #         print('Error: {}. {} : "서버 연결 불가'.format(sys.exc_info()[0],
# #                 sys.exc_info()[1]))
# #         print("대체 파일 로드 from ",DIR_SMP_DATA)

# #         with open(DIR_SMP_DATA, "rt", encoding="UTF8") as f:
# #             corpus = json.load(f)
        
# #         print("connection to Backend server failed!")
# #     showTime() 
# #     NUM_DOC = len(corpus) # 전체 사용 가능한 문서 수를 업데이트한다. 
# #     print("문서 로드 완료!")
# #     print()


# #     # 알고리즘 정확성을 확인하기 위해 일부러 문서 순서를 섞는다.
# #     if RANDOM_MODE == True:
# #         import random
# #         random.shuffle(corpus)

# #     for idx, doc in enumerate(corpus):
# #         titles.append(doc["post_title"])
# #         contents.append(doc["content"])

# #     # print(titles)#순서가 뒤바뀐 문서 set을 출력
# #     print("투입된 문서의 수 : %d" %(NUM_DOC))
# #     # print(len(contents))

# #     return NUM_DOC

# # # phase 2 형태소 분석기 + 내용 없는 문서 지우기
# # def dataPrePrcs():
    
# #     # 형태소 분석기 instance
# #     okt = Okt()
# #     print("데이터 전처리 중... It may takes few hours...")
# #     tokenized_doc = [okt.nouns(contents[cnt]) for cnt in range(len(contents))]

# #     print("형태소 분석 완료!")
# #     print("투입된 문서의 수 : %d" %(NUM_DOC))
# #     showTime()

# #     # 한글자 단어들 지우기!
# #     num_doc = len(tokenized_doc)
# #     for i in range(num_doc):
# #         tokenized_doc[i] = [word for word in tokenized_doc[i] if len(word) > 1]

# #     print("데이터 전처리 완료!")
# #     return tokenized_doc


# # loadData()
# # dataPrePrcs()

# # print(contents)