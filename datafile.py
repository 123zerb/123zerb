import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression as LR
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn import metrics
import seaborn as sns
csv_file_path = "/Users/mac/Desktop/九章云极机器学习笔试(1)/churn_train.csv"
csv_file_path1 = "/Users/mac/Desktop/九章云极机器学习笔试(1)/churn_test.csv"
df = pd.read_csv(csv_file_path)
df1 = pd.read_csv(csv_file_path1)
print(df1.info)
print('------------------------------')
count_classes = pd.value_counts(df['churn'], sort=True).sort_index()  ##取出Class列中不同数的个数，并按照大小排序
print(count_classes)
X = df.drop('churn',axis= 1)
y = df['churn']
print(X.shape)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
lrl1 = LR(penalty="l1", solver="liblinear", C=0.5, max_iter=1000)
lrl2 = LR(penalty="l2", solver="liblinear", C=0.5, max_iter=1000)
lrl1 = lrl1.fit(X,y)
print(lrl1.coef_)#coef_查看每个特征所对应的参数
print((lrl1.coef_ != 0).sum(axis=1))#array([10]),30个特征中有10个特征的系数不为0;由此可见l1正则化会让参数的系数为0
lrl2 = lrl2.fit(X,y)
print(lrl2.coef_)#没有一个参数的系数为0,由此可见l2会尽量让每一个参数都能有贡献
print('***************************')
l1 = []
l2 = []
l1test = []
l2test = []
l3yanzheng = []
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.3, random_state=420)
for i in np.linspace(0.05, 1.5, 19):#取了19个数
    lrl1 = LR(penalty="l1", solver="liblinear", C=i, max_iter=1000)
    lrl2 = LR(penalty="l2", solver="liblinear", C=i, max_iter=1000)
    lrl1 = lrl1.fit(Xtrain, Ytrain)#对模型训练
    l1.append(accuracy_score(lrl1.predict(Xtrain), Ytrain))#训练的结果
    l1test.append(accuracy_score(lrl1.predict(Xtest), Ytest))#测试的结果
    lrl2 = lrl2.fit(Xtrain, Ytrain)#对模型训练
    l2.append(accuracy_score(lrl2.predict(Xtrain), Ytrain))#训练的结果
    l2test.append(accuracy_score(lrl2.predict(Xtest), Ytest))#测试的结果

print('***************************')
confusion_matrix_result = metrics.confusion_matrix(lrl2.predict(Xtest),Ytest)
print('The confusion matrix result:\n',confusion_matrix_result)
print('***************************')
confusion_matrix_result = metrics.confusion_matrix(lrl1.predict(Xtest),Ytest)
print('The confusion matrix result:\n',confusion_matrix_result)
print('***************************')
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix_result, annot=True, cmap='Blues')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.show()

graph = [l1, l2, l1test, l2test]
color = ["green", "black", "lightgreen", "gray"]
label = ["L1", "L2", "L1test", "L2test"]
plt.figure(figsize=(6, 6))
for i in range(len(graph)):
    plt.plot(np.linspace(0.05, 1.5, 19), graph[i], color[i], label=label[i])#折线图cd
plt.legend(loc=4)  # 图例的位置在哪里?4表示，右下角
plt.show()

#
#
# clf = LogisticRegression()
# clf.fit(X_train ,y_train)
# ## 预测模型
# train_predict = clf.predict(X_train)
# test_predict = clf.predict(X_test)
# ## 查看其对应的w
# print('the weight of Logistic Regression:',clf.coef_)
# ## 查看其对应的w0
# print('the intercept(w0) of Logistic Regression:',clf.intercept_)
# ## 利用accuracy（准确度）评估模型效果
# print('The accuracy of the Logistic Regression is:',metrics.accuracy_score(y_train,train_predict))
# print('The accuracy of the Logistic Regression is:',metrics.accuracy_score(y_test,test_predict))
#
# ## 查看混淆矩阵 (预测值和真实值的各类情况统计矩阵)
# confusion_matrix_result = metrics.confusion_matrix(test_predict,y_test)
# print('The confusion matrix result:\n',confusion_matrix_result)
# # 可视化
# plt.figure(figsize=(8, 6))
# sns.heatmap(confusion_matrix_result, annot=True, cmap='Blues')
# plt.xlabel('Predicted labels')
# plt.ylabel('True labels')
# plt.show()





#
# # build model
# l1, l2, l1test, l2test = [], [], [], []
#
# for i in np.linspace(0.05, 1, 19):
#     lrl1 = LogisticRegression(penalty="l1", solver="liblinear", C=i, max_iter=1000)
#     lrl2 = LogisticRegression(penalty="l2", solver="liblinear", C=i, max_iter=1000)
#
#     lrl1 = lrl1.fit(X_train, y_train)
#     l1.append(accuracy_score(lrl1.predict(X_train), y_train))
#     l1test.append(accuracy_score(lrl1.predict(X_test), y_test))
#
#     lrl2 = lrl2.fit(X_train, y_train)
#     l2.append(accuracy_score(lrl2.predict(X_train), y_train))
#     l2test.append(accuracy_score(lrl2.predict(X_test), y_test))
#
# print("L1正则化结果：\n", lrl1.coef_, "\nL2正则化结果：\n", lrl2.coef_)
# result = [l1, l2, l1test, l2test]
# color = ["green", "red", "yellow", "black"]
# label = ["L1", "L2", "L1test", "L2test"]
#
# # 结果展示
# plt.figure(figsize=(8, 4))
# for i in range(4):
#     plt.plot(np.linspace(0.05, 1, 19), result[i], color[i], label=label[i])
# plt.legend()
# plt.show()

