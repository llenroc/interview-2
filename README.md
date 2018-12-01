# Machine To Learn
<!--
* 罗列1
	- 罗列二
[回到底部](#resume) 跳转到某个标题，标题都是小写，且用-连接
> 引用的文字
**文字** 字体加粗
`文字` 背景加灰
![](path/to/*.jpg) 引用图片
[百度](https://baidu.com) 跳转到百度
## 二级目录，两行作分隔符
### 三级目录，一行作分隔符
-->


## SQL

### Joins

* Inner join: return records that have matched values in both tables
* Left join: return all records from the left table, if matched in the right table 1 else 0
* Right join: oppsite to left join
* Outer join: return all records when there is a match in either left or right table

### Optimize

[todo]


### FAQ

[todo]


## Statistics and ML

### Project Workflow

Given a data science problem, what steps should we flollow? Or how to design a ML system?
or How to design a recommend engine? Heres are some major steps:

* Specify business objective
* Define the problem: The most important step. You should know how to model your problem and figure out which type it is, supervised or unsupervised, classification or regression.
* Create a baseline: No need to use ML or DL, even random select or rule based.
* Review ML literatures
* ML design
	- Do exploratory data analysis
	- Patition data
	- Preprocess
	- Engineer features
	- Choose proper alogorithm, ML or DL
	- Train, test and validation
	- Ensemble
* Deploy model
* Monitor model
* Iterate model

### Cross Validation

Cross-validation is a technique to enhance model stability and performace by partitioning the original data into training data to train the model, validation data to evaluate it. Usually, a k-fold cross validation divides the data into k folds, trains on each k-1 folds and the left 1 fold to evalatue. This results k models, which can be averaged to get an overall model performance.

### Feature Importance

* In linear models, feature importance can be calculated by the scale of the coefficients!!!
* In tree-based mothods, important features are likely to appear closer to the root of the tree. It can be computed by the average of the depth across all trees.

### Mean Squared Error vs. Mean Absolute Error

namely MSE vs. MAE.

* Similarity:



## Natural Language Processing

### NER

从文本中识别出命名性指称项，为关系抽取、知识图谱等任务做铺垫。

**基于规则的方法**：

利用手工编写的规则对文本进行匹配。需要谨慎处理规则之间的冲突，以及维护成本过大。

**基于特征模版的方法**：

将NER看作是序列标注任务，利用大规模预料来学习出标注模型，从而对句子的各个位置进行标注。常用的模型包括生成式模型HMM、判别式模型CRF等。比较流行的方法是**特征模版 + CRF**的方案。

**基于深度学习+crf的方法**：
> John  lives in New   York  and works for the European Union

> B-PER O     O  B-LOC I-LOC O   O     O   O   B-ORG    I-ORG

其中，LOC, PER, ORG and MISC分别代表locations, persons, orgnizations and miscellaneous。B-...代表着一个实体的Beginning，I-...代表一个实体的inside。


模型是如何得知每个单词的意思？需要有一个.txt类似文件保存如下的信息。
```
EU B-ORG
rejects O
German B-MISC
call O
to O
boycott O
British B-MISC
lamb O
. O

Peter B-PER
Blackburn I-PER
```

























