

## 1.0 pandas
Pandas 主要引入了两种新的数据结构：
DataFrame 和 Series
Series - 一维数组
DataFrame - 二维数组



## git 冲突
通过git status查看冲突,似乎是因为我在线上版本删掉了一些东西，但是我git pull 下来之后，我自己本地还存在这个文件，就需要我手动删除，或者跳过冲突：
```shell
% git status

# On branch main
# You have unmerged paths.
#   (fix conflicts and run "git commit")
#   (use "git merge --abort" to abort the merge)

# Unmerged paths:
#   (use "git add/rm <file>..." as appropriate to mark resolution)
#         deleted by them: .DS_Store
#         added by us:     kaggleDeep/.DS_Store
#         added by us:     kaggleDeep/01-Exercise-Single-Neuron/.DS_Store

# no changes added to commit (use "git add" and/or "git commit -a")