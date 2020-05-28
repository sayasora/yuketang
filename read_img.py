from PIL import Image
import pytesseract
import io
import requests

cookies = {
    '_ga': 'GA1.2.546944743.1590029771',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Sec-Fetch-Dest': 'image',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Referer': 'https://www.yuketang.cn/v2/web/quizSummary/3545590/878580',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

def get_text(url):
    response = requests.get(url, headers=headers, cookies=cookies)
    a = response.content
    img = Image.open(io.BytesIO(a))
    text = pytesseract.image_to_string(img, lang="chi_sim雨课堂")
    text = text.replace('\n', '').replace(' ', '')
    if text == '':
        return {
            'state': 0,
            'url': url,
            'content': '无法识别:('+url+')'
        }
    else:
        return {
            'state': 1,
            'content': text
        }