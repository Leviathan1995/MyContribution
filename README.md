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
# 密码模式
python3 contribution.py

# token模式
python3 contribution.py -t <github token>
```

Default mode is `ASYNC`, if error happened, you can try slower `--sync` mode.

Use `--help` to see full options and usage.

## Contributions(79 merged)


* [**HouzuoGuo/tiedot**(★1993)](https://github.com/HouzuoGuo/tiedot) - [Use fmt.Errorf() instead of errors.New(fmt.Sprintf(...))](https://github.com/HouzuoGuo/tiedot/pull/133)
* [**Qihoo360/evpp**(★856)](https://github.com/Qihoo360/evpp) - [typo](https://github.com/Qihoo360/evpp/pull/1)
* [**Qihoo360/floyd**(★126)](https://github.com/Qihoo360/floyd) - [update .travis.yml](https://github.com/Qihoo360/floyd/pull/27)
* [**Qihoo360/nemo**(★63)](https://github.com/Qihoo360/nemo)
  * [bugfix strtoint](https://github.com/Qihoo360/nemo/pull/22)
  * [support keys for select by type](https://github.com/Qihoo360/nemo/pull/21)
  * [Support Scanbytype](https://github.com/Qihoo360/nemo/pull/17)
  * [To improve HLL precision](https://github.com/Qihoo360/nemo/pull/8)
  * [fix bug](https://github.com/Qihoo360/nemo/pull/7)
  * [Support hyperloglog](https://github.com/Qihoo360/nemo/pull/6)
* [**Qihoo360/pika**(★1546)](https://github.com/Qihoo360/pika)
  * [optimize code](https://github.com/Qihoo360/pika/pull/227)
  * [fix srandmember](https://github.com/Qihoo360/pika/pull/224)
  * [add slave-priority](https://github.com/Qihoo360/pika/pull/222)
  * [add CPU usage](https://github.com/Qihoo360/pika/pull/218)
  * [Support Pub/Sub](https://github.com/Qihoo360/pika/pull/207)
  * [fix pika will crash when the disk is full](https://github.com/Qihoo360/pika/pull/190)
  * [Support pika context tool](https://github.com/Qihoo360/pika/pull/186)
  * [Support keys for select by type](https://github.com/Qihoo360/pika/pull/179)
  * [Support double master](https://github.com/Qihoo360/pika/pull/176)
  * [Update .gitignore](https://github.com/Qihoo360/pika/pull/164)
  * [Rsync optimized for speed](https://github.com/Qihoo360/pika/pull/162)
  * [Fix expire dump bug](https://github.com/Qihoo360/pika/pull/147)
  * [add pika_to_redis](https://github.com/Qihoo360/pika/pull/137)
  * [Support delbackup command](https://github.com/Qihoo360/pika/pull/133)
  * [Support dump-expire parameter](https://github.com/Qihoo360/pika/pull/127)
  * [Support time command](https://github.com/Qihoo360/pika/pull/124)
  * [fix memory leak](https://github.com/Qihoo360/pika/pull/98)
  * [Modify test directory structure](https://github.com/Qihoo360/pika/pull/90)
  * [bugfix GEO](https://github.com/Qihoo360/pika/pull/77)
  * [修改HLL测试文件](https://github.com/Qihoo360/pika/pull/74)
  * [fix bug](https://github.com/Qihoo360/pika/pull/72)
  * [Update README.md](https://github.com/Qihoo360/pika/pull/71)
  * [format code](https://github.com/Qihoo360/pika/pull/66)
  * [Support GEO](https://github.com/Qihoo360/pika/pull/59)
  * [Support hyperloglog](https://github.com/Qihoo360/pika/pull/56)
* [**Qihoo360/pink**(★207)](https://github.com/Qihoo360/pink)
  * [optimize code](https://github.com/Qihoo360/pink/pull/23)
  * [Support Pub/Sub](https://github.com/Qihoo360/pink/pull/22)
  * [Support Pub/Sub](https://github.com/Qihoo360/pink/pull/20)
  * [fix bug](https://github.com/Qihoo360/pink/pull/3)
* [**Qihoo360/slash**(★40)](https://github.com/Qihoo360/slash)
  * [bugfix rsync](https://github.com/Qihoo360/slash/pull/10)
  * [use posix_fallocate](https://github.com/Qihoo360/slash/pull/6)
  * [Make the file descriptor limit configurable](https://github.com/Qihoo360/slash/pull/3)
  * [Support long long int](https://github.com/Qihoo360/slash/pull/2)
* [**Qihoo360/zeppelin**(★107)](https://github.com/Qihoo360/zeppelin)
  * [return statement is unnecessary](https://github.com/Qihoo360/zeppelin/pull/6)
  * [Make the file descriptor limit configurable](https://github.com/Qihoo360/zeppelin/pull/5)
  * [Makefile bug](https://github.com/Qihoo360/zeppelin/pull/4)
  * [Makefile bug](https://github.com/Qihoo360/zeppelin/pull/3)
* [**Qihoo360/zeppelin-client**(★10)](https://github.com/Qihoo360/zeppelin-client)
  * [fix crash](https://github.com/Qihoo360/zeppelin-client/pull/14)
  * [bugfix](https://github.com/Qihoo360/zeppelin-client/pull/13)
  * [Modify constructor function interface](https://github.com/Qihoo360/zeppelin-client/pull/12)
  * [Add examples](https://github.com/Qihoo360/zeppelin-client/pull/11)
  * [Support mget command and overload constructor funciton in php](https://github.com/Qihoo360/zeppelin-client/pull/9)
  * [bugfix:use the value of pointer to check](https://github.com/Qihoo360/zeppelin-client/pull/8)
  * [Add parallel testing](https://github.com/Qihoo360/zeppelin-client/pull/4)
  * [use NULL instead of unused pointer](https://github.com/Qihoo360/zeppelin-client/pull/3)
  * [fix compile error and the limit of ttl](https://github.com/Qihoo360/zeppelin-client/pull/2)
  * [support exit command for zp_manager](https://github.com/Qihoo360/zeppelin-client/pull/1)
* [**Qihoo360/zeppelin-gateway**(★11)](https://github.com/Qihoo360/zeppelin-gateway) - [Fix memory leak and remove redundant condition statemen](https://github.com/Qihoo360/zeppelin-gateway/pull/1)
* [**TalkingData/owl**(★404)](https://github.com/TalkingData/owl) - [fix RWMutex and gofmt -s](https://github.com/TalkingData/owl/pull/5)
* [**Tencent/libco**(★2481)](https://github.com/Tencent/libco) - [fix warning](https://github.com/Tencent/libco/pull/1)
* [**akumuli/Akumuli**(★352)](https://github.com/akumuli/Akumuli)
  * [Add a option that allows to preallocate file space](https://github.com/akumuli/Akumuli/pull/185)
  * [Set meaningful number of CPU's in TcpServer configuration](https://github.com/akumuli/Akumuli/pull/184)
  * [fix to clarify the precendence](https://github.com/akumuli/Akumuli/pull/182)
* [**blablamoxian/doubantop250**(★1)](https://github.com/blablamoxian/doubantop250) - [add .gitignore](https://github.com/blablamoxian/doubantop250/pull/1)
* [**gwuhaolin/lightsocks**(★800)](https://github.com/gwuhaolin/lightsocks) - [bugfix socks5](https://github.com/gwuhaolin/lightsocks/pull/32)
* [**jhao104/proxy_pool**(★2210)](https://github.com/jhao104/proxy_pool) - [typo](https://github.com/jhao104/proxy_pool/pull/42)
* [**onexsoft/OneValue**(★46)](https://github.com/onexsoft/OneValue)
  * [complete TODO](https://github.com/onexsoft/OneValue/pull/21)
  * [modify Makefile](https://github.com/onexsoft/OneValue/pull/20)
  * [remove the size of list](https://github.com/onexsoft/OneValue/pull/19)
  * [fix `ltrim` command bug](https://github.com/onexsoft/OneValue/pull/17)
  * [Improve the efficiency of list data type](https://github.com/onexsoft/OneValue/pull/16)
  * [Support for OS X and fix some warnings](https://github.com/onexsoft/OneValue/pull/15)
  * [support PFCOUNT method to Handle multiple values.](https://github.com/onexsoft/OneValue/pull/12)
  * [Use a lock for the key operation and support PFMERGE  method  to Handle multiple values.](https://github.com/onexsoft/OneValue/pull/9)
  * [Add support for HyperLogLog PFMERGE command.](https://github.com/onexsoft/OneValue/pull/8)
  * [Add the HyperLogLog algorithm as a native feature,but now only support PFADD and PFCOUNT method.](https://github.com/onexsoft/OneValue/pull/6)
  * [fix warning: ‘brdaddr’ may be used uninitialized in this function](https://github.com/onexsoft/OneValue/pull/3)
  * [fix "::read() has not been declared" error](https://github.com/onexsoft/OneValue/pull/1)
* [**tencent-wechat/libco**(★360)](https://github.com/tencent-wechat/libco) - [fix warning](https://github.com/tencent-wechat/libco/pull/1)
* [**tinyclub/linux-doc**(★103)](https://github.com/tinyclub/linux-doc) - [Update PLAN.md](https://github.com/tinyclub/linux-doc/pull/5)
