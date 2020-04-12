## 命令行识别
  安装Tesseract-OCR，设置classPath指向【这是我安装的位置】：D:\Program Files (x86)\Tesseract-OCR\

- `tesseract test.png output_1 -l eng`
 ```
 例如： tesseract D:\data\code_scan11120200002.PNG output_1 -l eng
 以eng语言，识别路径下的图片，将结果打印到当前文件夹的output_1.txt
【语法】:  tesseract imagename outputbase [-l lang] [-psm pagesegmode] [configfile…]

imagename为目标图片文件名，需加格式后缀；outputbase是转换结果文件名；
lang是语言名称（在Tesseract-OCR中tessdata文件夹可看到以eng开头的语言文件eng.traineddata），
如不标-l eng则默认为eng。

```
 
 
 ## 训练
 请参考：
 https://www.cnblogs.com/cnlian/p/5765871.html
 - 训练文件主要是针对你的项目所要处理的样本的， 训练有极强的针对性
 - 没有合并功能 ，一般默认使用 -l eng , 训练后只能使用自己的训练语言 -l myl
 
 ```angular2
引用
训练的库能和原来的库合并吗？不然的话训练好意义就不大了。

https://stackoverflow.com/questions/17420800/combine-trained-tesseract-files-into-one
严格来说是个hack或者workaround，Tesseract没有提供合并训练文件的功能。训练文件主要是针对你的项目所要处理的样本的。一旦训练完成，就没必要用它自带的traineddata了。不过，缺少合并功能，这样只能一次收集尽可能多的样本，而不能逐步增加，确实有点不方便。
```


## IP 代理
- 使用的是免费ip代理：

http://www.goubanjia.com/

https://www.xicidaili.com/nn/

- 校验IP地址

https://www.ip.cn/


 
 