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

## Contributions(68 merged)


* [**gwuhaolin/lightsocks**(★498)](https://github.com/gwuhaolin/lightsocks) - [bugfix socks5](https://github.com/gwuhaolin/lightsocks/pull/32)
* [**Qihoo360/slash**(★30)](https://github.com/Qihoo360/slash) - [use posix_fallocate](https://github.com/Qihoo360/slash/pull/6)
* [**Qihoo360/pika**(★1406)](https://github.com/Qihoo360/pika) - [fix pika will crash when the disk is full](https://github.com/Qihoo360/pika/pull/190)
* [**Qihoo360/nemo**(★56)](https://github.com/Qihoo360/nemo) - [bugfix strtoint](https://github.com/Qihoo360/nemo/pull/22)
* [**TalkingData/owl**(★366)](https://github.com/TalkingData/owl) - [fix RWMutex and gofmt -s](https://github.com/TalkingData/owl/pull/5)
* [**Qihoo360/pika**(★1406)](https://github.com/Qihoo360/pika) - [Support pika context tool](https://github.com/Qihoo360/pika/pull/186)
* [**Qihoo360/nemo**(★56)](https://github.com/Qihoo360/nemo) - [support keys for select by type](https://github.com/Qihoo360/nemo/pull/21)
* [**Qihoo360/pika**(★1406)](https://github.com/Qihoo360/pika)
  * [Support keys for select by type](https://github.com/Qihoo360/pika/pull/179)
  * [Support double master](https://github.com/Qihoo360/pika/pull/176)
  * [Update .gitignore](https://github.com/Qihoo360/pika/pull/164)
  * [Rsync optimized for speed](https://github.com/Qihoo360/pika/pull/162)
  * [Fix expire dump bug](https://github.com/Qihoo360/pika/pull/147)
* [**Qihoo360/zeppelin-client**(★8)](https://github.com/Qihoo360/zeppelin-client) - [fix crash](https://github.com/Qihoo360/zeppelin-client/pull/14)
* [**Qihoo360/nemo**(★56)](https://github.com/Qihoo360/nemo) - [Support Scanbytype](https://github.com/Qihoo360/nemo/pull/17)
* [**Qihoo360/pika**(★1406)](https://github.com/Qihoo360/pika) - [add pika_to_redis](https://github.com/Qihoo360/pika/pull/137)
* [**Qihoo360/zeppelin-client**(★8)](https://github.com/Qihoo360/zeppelin-client)
  * [bugfix](https://github.com/Qihoo360/zeppelin-client/pull/13)
  * [Modify constructor function interface](https://github.com/Qihoo360/zeppelin-client/pull/12)
  * [Add examples](https://github.com/Qihoo360/zeppelin-client/pull/11)
  * [Support mget command and overload constructor funciton in php](https://github.com/Qihoo360/zeppelin-client/pull/9)
* [**Qihoo360/pika**(★1406)](https://github.com/Qihoo360/pika)
  * [Support delbackup command](https://github.com/Qihoo360/pika/pull/133)
  * [Support dump-expire parameter](https://github.com/Qihoo360/pika/pull/127)
* [**Qihoo360/zeppelin-client**(★8)](https://github.com/Qihoo360/zeppelin-client) - [bugfix:use the value of pointer to check](https://github.com/Qihoo360/zeppelin-client/pull/8)
* [**Qihoo360/pika**(★1406)](https://github.com/Qihoo360/pika) - [Support time command](https://github.com/Qihoo360/pika/pull/124)
* [**HouzuoGuo/tiedot**(★1943)](https://github.com/HouzuoGuo/tiedot) - [Use fmt.Errorf() instead of errors.New(fmt.Sprintf(...))](https://github.com/HouzuoGuo/tiedot/pull/133)
* [**jhao104/proxy_pool**(★1810)](https://github.com/jhao104/proxy_pool) - [typo](https://github.com/jhao104/proxy_pool/pull/42)
* [**Qihoo360/zeppelin-gateway**(★11)](https://github.com/Qihoo360/zeppelin-gateway) - [Fix memory leak and remove redundant condition statemen](https://github.com/Qihoo360/zeppelin-gateway/pull/1)
* [**akumuli/Akumuli**(★310)](https://github.com/akumuli/Akumuli) - [Add a option that allows to preallocate file space](https://github.com/akumuli/Akumuli/pull/185)
* [**Qihoo360/pika**(★1406)](https://github.com/Qihoo360/pika) - [fix memory leak](https://github.com/Qihoo360/pika/pull/98)
* [**akumuli/Akumuli**(★310)](https://github.com/akumuli/Akumuli)
  * [Set meaningful number of CPU's in TcpServer configuration](https://github.com/akumuli/Akumuli/pull/184)
  * [fix to clarify the precendence](https://github.com/akumuli/Akumuli/pull/182)
* [**Qihoo360/zeppelin**(★76)](https://github.com/Qihoo360/zeppelin) - [return statement is unnecessary](https://github.com/Qihoo360/zeppelin/pull/6)
* [**Qihoo360/zeppelin-client**(★8)](https://github.com/Qihoo360/zeppelin-client)
  * [Add parallel testing](https://github.com/Qihoo360/zeppelin-client/pull/4)
  * [use NULL instead of unused pointer](https://github.com/Qihoo360/zeppelin-client/pull/3)
* [**Qihoo360/slash**(★30)](https://github.com/Qihoo360/slash) - [Make the file descriptor limit configurable](https://github.com/Qihoo360/slash/pull/3)
* [**Qihoo360/zeppelin**(★76)](https://github.com/Qihoo360/zeppelin) - [Make the file descriptor limit configurable](https://github.com/Qihoo360/zeppelin/pull/5)
* [**Qihoo360/slash**(★30)](https://github.com/Qihoo360/slash) - [Support long long int](https://github.com/Qihoo360/slash/pull/2)
* [**Qihoo360/zeppelin-client**(★8)](https://github.com/Qihoo360/zeppelin-client)
  * [fix compile error and the limit of ttl](https://github.com/Qihoo360/zeppelin-client/pull/2)
  * [support exit command for zp_manager](https://github.com/Qihoo360/zeppelin-client/pull/1)
* [**Qihoo360/pika**(★1406)](https://github.com/Qihoo360/pika) - [Modify test directory structure](https://github.com/Qihoo360/pika/pull/90)
* [**Qihoo360/zeppelin**(★76)](https://github.com/Qihoo360/zeppelin)
  * [Makefile bug](https://github.com/Qihoo360/zeppelin/pull/4)
  * [Makefile bug](https://github.com/Qihoo360/zeppelin/pull/3)
* [**Qihoo360/pika**(★1406)](https://github.com/Qihoo360/pika) - [bugfix GEO](https://github.com/Qihoo360/pika/pull/77)
* [**Qihoo360/nemo**(★56)](https://github.com/Qihoo360/nemo) - [To improve HLL precision](https://github.com/Qihoo360/nemo/pull/8)
* [**Qihoo360/pika**(★1406)](https://github.com/Qihoo360/pika)
  * [修改HLL测试文件](https://github.com/Qihoo360/pika/pull/74)
  * [fix bug](https://github.com/Qihoo360/pika/pull/72)
* [**Qihoo360/nemo**(★56)](https://github.com/Qihoo360/nemo) - [fix bug](https://github.com/Qihoo360/nemo/pull/7)
* [**Qihoo360/pika**(★1406)](https://github.com/Qihoo360/pika) - [Update README.md](https://github.com/Qihoo360/pika/pull/71)
* [**Qihoo360/evpp**(★767)](https://github.com/Qihoo360/evpp) - [typo](https://github.com/Qihoo360/evpp/pull/1)
* [**Qihoo360/pika**(★1406)](https://github.com/Qihoo360/pika)
  * [format code](https://github.com/Qihoo360/pika/pull/66)
  * [Support GEO](https://github.com/Qihoo360/pika/pull/59)
* [**Qihoo360/pink**(★182)](https://github.com/Qihoo360/pink) - [fix bug](https://github.com/Qihoo360/pink/pull/3)
* [**Qihoo360/pika**(★1406)](https://github.com/Qihoo360/pika) - [Support hyperloglog](https://github.com/Qihoo360/pika/pull/56)
* [**Qihoo360/nemo**(★56)](https://github.com/Qihoo360/nemo) - [Support hyperloglog](https://github.com/Qihoo360/nemo/pull/6)
* [**onexsoft/OneValue**(★45)](https://github.com/onexsoft/OneValue)
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
* [**Tencent/libco**(★2327)](https://github.com/Tencent/libco) - [fix warning](https://github.com/Tencent/libco/pull/1)
* [**tencent-wechat/libco**(★350)](https://github.com/tencent-wechat/libco) - [fix warning](https://github.com/tencent-wechat/libco/pull/1)
* [**tinyclub/linux-doc**(★99)](https://github.com/tinyclub/linux-doc) - [Update PLAN.md](https://github.com/tinyclub/linux-doc/pull/5)
