# 导入必要的库
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt

# 加载鸢尾花数据集
data = load_iris()
X = data.data  # 'data': array([[5.1, 3.5, 1.4, 0.2], [4.9, 3. , 1.4, 0.2], [4.7, 3.2, 1.3, 0.2], ...]) shape(150,4) the attributes of flowers
y = data.target  # 'target': array([0, 0, 0, ..., 1, 1, 1, ...]) shape(150,0) large type belonged to

# 将数据集分成训练集和测试集
# random_state: just to set seed
# test_size: 30% test, 70% train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 创建并训练LDA模型
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = lda.predict(X_test)

# 评估模型性能
accuracy = accuracy_score(y_test, y_pred)
print(f'模型准确度: {accuracy}')


def foo():
    pass


