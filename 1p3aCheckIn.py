import requests
import re
import json

class AutoPunch:
    def __init__(self, username, pwd):
        self.username = username
        self.pwd = pwd
        self.login_url = 'https://www.1point3acres.com/bbs/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
        self.punch_url = 'https://www.1point3acres.com/bbs/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&sign_as=1&inajax=1'
        self.session = requests.Session()
        self.headers = {
                'origin': 'https://www.1point3acres.com',
                'referer': 'https://www.1point3acres.com/bbs/',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            }

    def login(self):
        res = self.session.post(self.login_url,
            headers=self.headers,
            data={
                'username': self.username,
                'password': self.pwd,
                'quickforward': 'yes',
                'handlekey': 'ls'
            })

        return res

    def get_formhash(self):
        res = self.session.get('https://www.1point3acres.com/bbs/', headers=self.headers)
        result = re.search('dsu_paulsign:sign&(.{8})', res.text)

        if result:
            return result.group(1)

    # post body里的qdxq=签到心情，todaysay=今日想说的话。
    def punch(self, formhash):
        res = self.session.post(self.punch_url,
            headers=self.headers,
            data={
                'formhash': formhash,
                'qdxq': 'kx',
                'qdmode': 2,
                'todaysay': 'check in',
                'fastreply': 0
            })

        print('status: ' + res.status_code)


if __name__ == '__main__':
    with open('accounts.json') as json_file:
        data = json.load(json_file)

        for account in data:
            ap = AutoPunch(account['id'], account['password'])
            ap.login()
            formhash = ap.get_formhash()

            if formhash:
                ap.punch(formhash)
            else:
                print(account['id'] + ' 今日已签到')
