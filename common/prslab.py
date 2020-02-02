# from  import DocCorpus as c
# c.NUM_DOC = 10
# import prs
# print(c.NUM_DOC)
# import os
# currDirPath = os.getcwd()
# print(currDirPath)
# currDir = os.path.split(currDirPath)[1]
# parentDirPath = os.path.split(currDirPath)[0]
# parDir = os.path.split(parentDirPath)[1]
# print(currDir)
# if currDir != common:
#     if parentDir == TIBigdataMiddleware:
#         os.chdir(parentDirPath+"common")
    # os.chdir()
# import timeEvlt as te # te gloval scope init at this point. 
import prs
prs.readyData(10)
# print(prs.readyData())




# issue : 내용 없는 데이터가 생긴다...
# import json
# import esFunc
# import prs

# data = prs.readyData(30)
# ids = data[0]
# titles = data[1]
# content = data[2]


# print("데이터 길이 : ", len(ids), len(titles), len(content))