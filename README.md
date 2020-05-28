# yuketang
雨课堂测试题爬虫

本来以为随便几个正则就弄出来了，结果F12到处搜不到题目，题干，答案都搜不到。
拿Charles抓包发现这鬼东西全是图片（腾讯真有钱），还好图片里的文字都非常规则，python的的图像识别库可以识别大部分文字。
于是用tesseract作了处理，代码很简单，因为题量不大，所有没有使用多线程爬取，而且还是有一部分图片无法识别。最后希望大家顺利通过考试。

chi_sim雨课堂.traineddata 文件为OCR库中tessdata里的中文识别包，我使用的是这个文件来识别图片，大家可以在网上下载更好的包来替换这个文件，
注意：更换的话需要在read_img中更换掉 chi_sim雨课堂.traineddata 的名字 默认中文翻译包为 chi_sim.traineddata

out_txt 与 out_word 中需要修改的代码如下，具体修改为雨课堂中相应的参数

![image]https://github.com/sayasora/yuketang/blob/master/show1.png)

problem_id 与 problem_id2 为一个测试题的第一题与最后一题 如果差值大于题数，那就要自己写try循环了，中间有些题号被作废了

    修改此处'cookie': '',

    classroom_id = 3545590
    # 试题id
    quiz_id = 878580
    # 第一道题id
    problem_id = 19068856
    # 最后一道题id
    problem_id2 = 19068859
    
    document.save('测试7.docx')

read_img.py 文件为识图接口
out_txt.py 将会print出来 不会自动保存 复制即刻 无法识别的图片会输出网址 结果展示如文件 测试5.txt
out_word.py 直接将网址图片打印出来，输出word文档  结果展示如文件 测试5.docx

