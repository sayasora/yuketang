import requests
from read_img import get_text

def get_url(a,b,c):
    # 需要获取登陆账户 获取cookie 否则无法爬取
    headers = {
        'authority': 'www.yuketang.cn',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': 'application/json, text/plain, */*',
        'sec-fetch-dest': 'empty',
        'xtbz': 'ykt',
        'university-id': '0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'xt-agent': 'web',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://www.yuketang.cn/v2/web/quizSummary/3545590/878580',
        'accept-language': 'zh-CN,zh;q=0.9',
        修改此处'cookie': '',
    }

    params = (
        ('classroom_id', str(a)),
        ('quiz_id', str(b)),
        ('problem_id', str(c)),
    )

    response = requests.get('https://www.yuketang.cn/v2/api/web/quiz/problem_shape', headers=headers, params=params)
    text = response.text
    return text

def get_aq(text):
    text_all = eval(text.replace('true', 'True').replace('false', 'False'))
    urls = text_all['data']['Shapes']
    dicts = {'0': '', '1': 'A：', '2': 'B：', '3': 'C：', '4': 'D：', '5': '图片', '6': '图片', '7': '图片', '8': '图片', '9': '图片', '10': '图片', '11': '图片'}
    for i in range(len(urls)):
        url = urls[i].get('URL')
        text = get_text(url)
        play_text = text['content']
        print(dicts[str(i)] + play_text)
    print("答案： " + text_all['data']['Answer'])

if __name__ == '__main__':
    # 根据具体情况修改
    # 课程id
    classroom_id = 3545590
    # 试题id
    quiz_id = 957301
    # 第一道题id
    problem_id = 20204890
    # 最后一道题id
    problem_id2 = 20205021
    # 题号
    num = 1

    for i in range(problem_id, problem_id2+1):
        text = get_url(classroom_id, quiz_id, i)
        print('题号：' + str(num) + '  参数'+str([classroom_id, quiz_id, i]))
        get_aq(text)
        num = num+1
        print()