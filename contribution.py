import requests
import os
import re
import getpass
from bs4 import BeautifulSoup

basic_content = '''
# MyContribution
Crawl my all merged pull request and show on `README.md`

## Basic

#### Dependencies
 * Python 3.5+
 * BeautifulSoup

#### How to use
Fork this repository and 
        
        python3 contribution.py

## Contribution
'''

class ContributionInfo:
    def __init__(self, pr_title, pr_url, project_name, project_url, author):
        self.pr_title = pr_title
        self.pr_url = pr_url
        self.project_name = project_name
        self.project_url = project_url
        self.author = author


class Contribution:
    def __init__(self):
        self.github_url = "https://github.com"
        self.login_url = 'https://github.com/login'
        self.github_username = ""
        self.github_password = ""
        self.user_headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
        }
        self.session_url = 'https://github.com/session'
        self.contribution_url = "https://github.com/pulls?q=is%3Apr+is%3Aclosed+is%3Amerged+author%3A"
        self.contribution_response = ""
        self.contribution_info = []
        self.session = ""

    def login(self):
        self.github_username = input("Your Github Username Not Email:")
        self.github_password = getpass.getpass("Your Github Password:")
        self.session = requests.Session()
        response = self.session.get(self.login_url, headers=self.user_headers)
        pattern = re.compile(r'<input name="authenticity_token" type="hidden" value="(.*)" />')

        authenticity_token = pattern.findall(response.content.decode('utf-8'))[0]

        login_data = {
            'commit': 'Sign in',
            'utf8': '%E2%9C%93',
            'authenticity_token': authenticity_token, 'login': self.github_username,
            'password': self.github_password
        }

        login_response = self.session.post(self.session_url, headers=self.user_headers, data=login_data)
        if str(login_response) == "<Response [200]>":
            print("Login Success.")
        else:
            print("Login Failed.")

        self.contribution_url = self.contribution_url + self.github_username

    def parser(self):
        while self.contribution_url != "":
            self.contribution_response = self.session.get(self.contribution_url, headers=self.user_headers)
            soup = BeautifulSoup(self.contribution_response.text, 'html.parser')

            pr_info = soup.find_all('a', 'link-gray-dark no-underline h4 js-navigation-open')
            pr_project = soup.find_all('a', 'muted-link h4 pr-1')
            next_page = soup.find_all('a', 'next_page')

            for info, project in zip(pr_info, pr_project):
                info = BeautifulSoup(str(info), 'html.parser')
                project = BeautifulSoup(str(project), 'html.parser')

                pr_title = info.string
                pr_url = self.github_url + info.a['href']
                project_name = project.string
                project_url = project.a['href']

                c = ContributionInfo(pr_title.strip(), pr_url.strip(), project_name.strip(), project_url.strip(), self.github_username)
                self.contribution_info.append(c)

            if next_page:
                next_page = BeautifulSoup(str(next_page), 'html.parser')
                self.contribution_url = self.github_url + next_page.a['href']
            else:
                self.contribution_url = ""


    def write(self):
        str_info = ""
        for info in self.contribution_info:
            str_info += ' * [**{}**]({}):[*{}*]({})\n'.format(info.project_name, info.project_url, info.pr_title, info.pr_url)
        print(str_info)
        str_contribution = basic_content + "\n" + str_info

        if not os.path.isfile("README.md"):
            raise TypeError("README.md does not exist")

        file = open("README.md", 'r+')
        file.truncate()
        file.write(str_contribution)
        file.close()

    def push(self):
        os.system('git add README.md')
        os.system('git commit -m "update README.md"')
        os.system('git push')

def main():
    c = Contribution()
    c.login()
    c.parser()
    c.write()
    c.push()

if __name__ == '__main__':
    main()
