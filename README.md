# antiword
针对中文词语的反义词查询接口．  
在当前的中文信息处理当中，有大量的近义词词典，如同义词词林等，  
但少有反义词词典，反义词词典在构造对立语义上有很大用途，本项目目的是为提供这一接口  

# How to run?

```shell
bash run.sh
```

This command will create the environment that needed by the models.  
This project is created on the purposes of easy-on-run.  
If you want to know the details about the models, just read code.  

# 问题

1) 基于词典的反义词查询，不可取，取无法穷举
2) 要是能够找到像word2vec这样的技术大规模地挖掘反义词，该有多好．
