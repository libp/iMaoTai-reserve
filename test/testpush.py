
import requests

url = 'http://www.pushplus.plus/send'
r = requests.get(url, params={'token': 'a7ce19add22c40658938c6759c7b7488',
                            'title': '会话过期请重新登录',
                            'content': 'chatgpt机器人会话过期请重新登录'})
print(f'通知推送结果：{r.status_code, r.text}')
