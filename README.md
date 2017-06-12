
# MyContribution

Crawl all merged pull request and show on `README.md`

## Basic

#### Dependencies

 - Python 3.5+
 - request (Only in sync mode)
 - aiohttp (Only in async mode)

#### How to use

Fork this repository and 
        
```bash
python3 contribution.py <YourUserName>
```

Default mode is ASYNC, if error happened, you can try slower `--sync` mode.

For only merged PRs, use `-m` option. 

For force override `README.md`, use `-f` option.

Use `--help` to see full option and usage.

## ContributionsCrawler

- [x] [jhao104/proxy_pool (874★ 305🍴)](https://github.com/jhao104/proxy_pool) - [typo](https://github.com/jhao104/proxy_pool/pulls/42)
- [ ] [Qihoo360/zeppelin (40★ 11🍴)](https://github.com/Qihoo360/zeppelin) - [Use prefix ++ operator](https://github.com/Qihoo360/zeppelin/pulls/8)
- [x] [Qihoo360/zeppelin-gateway (9★ 4🍴)](https://github.com/Qihoo360/zeppelin-gateway) - [Fix memory leak and remove redundant condition statemen](https://github.com/Qihoo360/zeppelin-gateway/pulls/1)
- [x] [akumuli/Akumuli (250★ 26🍴)](https://github.com/akumuli/Akumuli) - [Add a option that allows to preallocate file space](https://github.com/akumuli/Akumuli/pulls/185)
- [x] [Qihoo360/pika (976★ 228🍴)](https://github.com/Qihoo360/pika) - [fix memory leak](https://github.com/Qihoo360/pika/pulls/98)
- [x] [akumuli/Akumuli (250★ 26🍴)](https://github.com/akumuli/Akumuli) - [Set meaningful number of CPU's in TcpServer configuration](https://github.com/akumuli/Akumuli/pulls/184)
- [ ] [akumuli/Akumuli (250★ 26🍴)](https://github.com/akumuli/Akumuli) - [Set meaningful number of CPU's in TcpServer configuration](https://github.com/akumuli/Akumuli/pulls/183)
- [x] [akumuli/Akumuli (250★ 26🍴)](https://github.com/akumuli/Akumuli) - [fix to clarify the precendence](https://github.com/akumuli/Akumuli/pulls/182)
- [x] [Qihoo360/zeppelin (40★ 11🍴)](https://github.com/Qihoo360/zeppelin) - [return statement is unnecessary](https://github.com/Qihoo360/zeppelin/pulls/6)
- [x] [CatKang/zeppelin-client (3★ 1🍴)](https://github.com/CatKang/zeppelin-client) - [Add parallel testing](https://github.com/CatKang/zeppelin-client/pulls/4)
- [x] [CatKang/zeppelin-client (3★ 1🍴)](https://github.com/CatKang/zeppelin-client) - [use NULL instead of unused pointer](https://github.com/CatKang/zeppelin-client/pulls/3)
- [x] [Qihoo360/slash (13★ 8🍴)](https://github.com/Qihoo360/slash) - [Make the file descriptor limit configurable](https://github.com/Qihoo360/slash/pulls/3)
- [x] [Qihoo360/zeppelin (40★ 11🍴)](https://github.com/Qihoo360/zeppelin) - [Make the file descriptor limit configurable](https://github.com/Qihoo360/zeppelin/pulls/5)
- [x] [Qihoo360/slash (13★ 8🍴)](https://github.com/Qihoo360/slash) - [Support long long int](https://github.com/Qihoo360/slash/pulls/2)
- [x] [CatKang/zeppelin-client (3★ 1🍴)](https://github.com/CatKang/zeppelin-client) - [fix compile error and the limit of ttl](https://github.com/CatKang/zeppelin-client/pulls/2)
- [x] [CatKang/zeppelin-client (3★ 1🍴)](https://github.com/CatKang/zeppelin-client) - [support exit command for zp_manager](https://github.com/CatKang/zeppelin-client/pulls/1)
- [x] [Qihoo360/pika (976★ 228🍴)](https://github.com/Qihoo360/pika) - [Modify test directory structure](https://github.com/Qihoo360/pika/pulls/90)
- [x] [Qihoo360/zeppelin (40★ 11🍴)](https://github.com/Qihoo360/zeppelin) - [Makefile bug](https://github.com/Qihoo360/zeppelin/pulls/4)
- [x] [Qihoo360/zeppelin (40★ 11🍴)](https://github.com/Qihoo360/zeppelin) - [Makefile bug](https://github.com/Qihoo360/zeppelin/pulls/3)
- [x] [Qihoo360/pika (976★ 228🍴)](https://github.com/Qihoo360/pika) - [bugfix GEO](https://github.com/Qihoo360/pika/pulls/77)
- [x] [Qihoo360/nemo (37★ 25🍴)](https://github.com/Qihoo360/nemo) - [To improve HLL precision](https://github.com/Qihoo360/nemo/pulls/8)
- [x] [Qihoo360/pika (976★ 228🍴)](https://github.com/Qihoo360/pika) - [修改HLL测试文件](https://github.com/Qihoo360/pika/pulls/74)
- [x] [Qihoo360/pika (976★ 228🍴)](https://github.com/Qihoo360/pika) - [fix bug](https://github.com/Qihoo360/pika/pulls/72)
- [x] [Qihoo360/nemo (37★ 25🍴)](https://github.com/Qihoo360/nemo) - [fix bug](https://github.com/Qihoo360/nemo/pulls/7)
- [x] [Qihoo360/pika (976★ 228🍴)](https://github.com/Qihoo360/pika) - [Update README.md](https://github.com/Qihoo360/pika/pulls/71)
- [ ] [**ideawu/ssdb (4473★ 1004🍴)**](https://github.com/ideawu/ssdb) - [format code](https://github.com/ideawu/ssdb/pulls/1058)
- [x] [Qihoo360/pika (976★ 228🍴)](https://github.com/Qihoo360/pika) - [format code](https://github.com/Qihoo360/pika/pulls/66)
- [x] [Qihoo360/pika (976★ 228🍴)](https://github.com/Qihoo360/pika) - [Support GEO](https://github.com/Qihoo360/pika/pulls/59)
- [x] [Qihoo360/pink (137★ 57🍴)](https://github.com/Qihoo360/pink) - [fix bug](https://github.com/Qihoo360/pink/pulls/3)
- [x] [Qihoo360/pika (976★ 228🍴)](https://github.com/Qihoo360/pika) - [Support hyperloglog](https://github.com/Qihoo360/pika/pulls/56)
- [x] [Qihoo360/nemo (37★ 25🍴)](https://github.com/Qihoo360/nemo) - [Support hyperloglog](https://github.com/Qihoo360/nemo/pulls/6)
- [x] [onexsoft/OneValue (42★ 16🍴)](https://github.com/onexsoft/OneValue) - [complete TODO](https://github.com/onexsoft/OneValue/pulls/21)
- [x] [onexsoft/OneValue (42★ 16🍴)](https://github.com/onexsoft/OneValue) - [modify Makefile](https://github.com/onexsoft/OneValue/pulls/20)
- [x] [onexsoft/OneValue (42★ 16🍴)](https://github.com/onexsoft/OneValue) - [remove the size of list](https://github.com/onexsoft/OneValue/pulls/19)
- [x] [onexsoft/OneValue (42★ 16🍴)](https://github.com/onexsoft/OneValue) - [fix `ltrim` command bug](https://github.com/onexsoft/OneValue/pulls/17)
- [x] [onexsoft/OneValue (42★ 16🍴)](https://github.com/onexsoft/OneValue) - [Improve the efficiency of list data type](https://github.com/onexsoft/OneValue/pulls/16)
- [x] [onexsoft/OneValue (42★ 16🍴)](https://github.com/onexsoft/OneValue) - [Support for OS X and fix some warnings](https://github.com/onexsoft/OneValue/pulls/15)
- [x] [onexsoft/OneValue (42★ 16🍴)](https://github.com/onexsoft/OneValue) - [support PFCOUNT method to Handle multiple values.](https://github.com/onexsoft/OneValue/pulls/12)
- [x] [onexsoft/OneValue (42★ 16🍴)](https://github.com/onexsoft/OneValue) - [Use a lock for the key operation and support PFMERGE  method  to Handle multiple values.](https://github.com/onexsoft/OneValue/pulls/9)
- [x] [onexsoft/OneValue (42★ 16🍴)](https://github.com/onexsoft/OneValue) - [Add support for HyperLogLog PFMERGE command.](https://github.com/onexsoft/OneValue/pulls/8)
- [x] [onexsoft/OneValue (42★ 16🍴)](https://github.com/onexsoft/OneValue) - [Add the HyperLogLog algorithm as a native feature,but now only support PFADD and PFCOUNT method.](https://github.com/onexsoft/OneValue/pulls/6)
- [x] [onexsoft/OneValue (42★ 16🍴)](https://github.com/onexsoft/OneValue) - [fix warning: ‘brdaddr’ may be used uninitialized in this function](https://github.com/onexsoft/OneValue/pulls/3)
- [x] [onexsoft/OneValue (42★ 16🍴)](https://github.com/onexsoft/OneValue) - [fix "::read() has not been declared" error](https://github.com/onexsoft/OneValue/pulls/1)
- [ ] [yyzybb537/libgo (686★ 237🍴)](https://github.com/yyzybb537/libgo) - [use while instead of goto](https://github.com/yyzybb537/libgo/pulls/22)
- [x] [Tencent/libco (1609★ 453🍴)](https://github.com/Tencent/libco) - [fix warning](https://github.com/Tencent/libco/pulls/1)
- [x] [tencent-wechat/libco (331★ 129🍴)](https://github.com/tencent-wechat/libco) - [fix warning](https://github.com/tencent-wechat/libco/pulls/1)
- [ ] [tencent-wechat/phxrpc (647★ 227🍴)](https://github.com/tencent-wechat/phxrpc) - [add EV_ENABLE flags](https://github.com/tencent-wechat/phxrpc/pulls/19)
- [ ] [Qihoo360/pink (137★ 57🍴)](https://github.com/Qihoo360/pink) - [judge the return value of listen()](https://github.com/Qihoo360/pink/pulls/2)
- [x] [tinyclub/linux-doc (83★ 44🍴)](https://github.com/tinyclub/linux-doc) - [Update PLAN.md](https://github.com/tinyclub/linux-doc/pulls/5)