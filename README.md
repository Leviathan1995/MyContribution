# MyContribution

Crawl all merged pull request and show on `README.md`

## Basic

### Dependencies

 - Python 3.5+
 - request (only in sync mode)

```bash
pip3 install request
```
 - aiohttp (only in async mode)

```bash
pip3 install aiohttp
```

### How to use

Fork this repository and 

```bash
python3 contribution.py <github_oauth_token>
```

Default mode is `ASYNC`, if error happened, you can try slower `--sync` mode.

Use `--help` to see full options and usage.

## Contributions(4 merged)

* [**devlucky/Kakapo**(★724)](https://github.com/devlucky/Kakapo) - [Implement NSURLProtocol.stopLoading() for delayed requests](https://github.com/devlucky/Kakapo/pulls/96)
* [**RoleModel/RMSTokenView**(★207)](https://github.com/RoleModel/RMSTokenView) - [Avoid crash when multiple token fields causes a crash due to the constra...](https://github.com/RoleModel/RMSTokenView/pulls/13)
* [**rafiki270/HTTP-Status-Codes-for-Objective-C**(★33)](https://github.com/rafiki270/HTTP-Status-Codes-for-Objective-C) - [compiler warning fixed non-void method returning nothing](https://github.com/rafiki270/HTTP-Status-Codes-for-Objective-C/pulls/1)
* [**kevinzhow/PNChart**(★8828)](https://github.com/kevinzhow/PNChart) - [Updated PNLineChart to allow the display of multiple lines in the chart](https://github.com/kevinzhow/PNChart/pulls/19)
