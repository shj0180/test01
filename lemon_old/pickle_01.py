import pickle

dict = {'北京':{'曹阳','海淀'},('a','fot'):(33,44),'ttt':{5,66,'fggg'}}

# 写入
# with open('s_56_pickle.txt','wb') as f:
#     ret = pickle.dump(dict,f)
# print(ret)
#

# 读取
# with open('s_56_pickle.txt','rb') as f:
#     res = pickle.load(f)
# print(res)

rets = pickle.dumps(dict)
print(rets)

repd=pickle.loads(rets)
print(repd)








