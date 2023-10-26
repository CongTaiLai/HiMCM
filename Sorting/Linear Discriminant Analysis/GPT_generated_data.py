# 导入必要的库
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np

# 创建示例数据
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# 创建LDA模型
lda = LinearDiscriminantAnalysis()
lda.fit(X, y)

# 创建一个新的数据点进行分类
new_data_point = np.array([[2.5, 3.5]])
predicted_class = lda.predict(new_data_point)

# 输出预测结果
if predicted_class == 0:
    print("新数据点属于类别 0")
else:
    print("新数据点属于类别 1")
