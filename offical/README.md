Hadoop/Hbase Fully-Distributed Installer Scripts
================================================

# 1. introduction

## 1.1 description
Hadoop and Hbase fully-distributed installer scripts and guides for Ubuntu 12.04 Server 64-bit x86. Feel free to get copy of this repository.

`git clone https://github.com/justasabc/hadoop_scripts.git`

## 1.2 contributors
* 2013.12.6 - [justasabc](http://github.com/justasabc)

## 1.3 licenses
Apache 2.0

## 1.4 version
* OS: Ubuntu 12.04 Server 64-bit x86
* Hadoop: 1.2.1
* Hbase: 0.94.12
* zookeeper: 3.4.5

**NOTICE**

* Please download **jdk-6u35-linux-i586.bin** or **jdk-6u35-linux-x64.bin** and place in **`./offical/pre/jdk/`** folder.
* Please download **hadoop-1.2.1.tar.gz**, **hbase-0.94.12.tar.gz** and **zookeeper-3.4.5.tar.gz** and place in **`./offical/tar/`** folder.
* Then the **offical** folder structure should look like this:

```
offical/
├── conf
│   ├── hadoop
│   │   ├── core-site.xml
│   │   ├── hdfs-site.xml
│   │   ├── mapred-site.xml
│   │   ├── masters
│   │   └── slaves
│   ├── hbase
│   │   ├── hbase-site.xml
│   │   └── regionservers
│   └── zookeeper
│       ├── hbase-site.xml
│       └── zoo.cfg
├── examples
│   ├── java
│   │   └── wordcount
│   │       ├── cmd.ini
│   │       └── WordCount.java
│   └── python
│       └── pyhbase
│           ├── gis.py
│           ├── hbase
│           │   └── ...
│           ├── __init__.py
│           └── thrift
│               └── ...
├── guides
│   ├── compile_thrift_for_python.ini
│   ├── hadoop.ini
│   ├── hbase.ini
│   ├── params_hbase.ini
│   ├── rest_hbase.ini
│   └── thrift_hbase.ini
├── install_hadoop
├── install_hbase
├── install_zookeeper
├── post
│   ├── configure_ssh.ini
│   ├── format_hdfs.ini
│   └── run_as_hduser_on_master_only
├── pre
│   ├── create_hadoop_accounts
│   ├── demos_hosts
│   ├── disable_ipv6
│   ├── hosts
│   ├── jdk
│   │   ├── install_jdk
│   │   ├── javahome
│   │   ├── jdk-6u35-linux-i586.bin
│   │   └── jdk-6u35-linux-x64.bin
│   ├── run_as_root_on_all_nodes
│   └── update_hosts
├── README.md
└── tar
    ├── hadoop-1.2.1.tar.gz
    ├── hbase-0.94.12.tar.gz
    ├── thrift-0.9.1.tar.gz
    └── zookeeper-3.4.5.tar.gz

19 directories, 81 files

```

## 1.5 overall planning
* install hadoop and hbase on all nodes. what's more, configuration files on all nodes are same.
* install zookeeper on master node.
* only need to issue commands on master node to start hadoop, zookeeper,hbase(including rest and thrift gateway).

# 2. pre-install
Please run the following commands as **root** and on **all nodes**! 

`su - root`

## 2.1 install jdk

	cd pre/jdk/
	./install_jdk

## 2.2 disable ipv6

	cd pre/
	./disable_ipv6

## 2.3 update hosts 

	cd pre/
	vim ./hosts
	./update_hosts

## 2.4 create hadoop accouts

	cd pre/
	./create_hadoop_accounts

## 2.5 edit hadoop confs

	cd ./conf/hadoop/
	vim core-site.xml
	vim mapred-site.xml
	vim hdfs-site.xml
	vim masters
	vim slaves

## 2.6 edit hbase confs

	cd ./conf/hbase/
	vim hbase-site.xml
	vim regionservers

# 3. install
Please run the following commands as **root** and on **all nodes**! 

`su - root`

## 3.1 install hadoop

	./install_hadoop

## 3.2 install hbase

	./install_hbase

# 4. post-install
Please run the following commands as **hduser** and on **master node only**! 

`su - hduser`

## 4.1 configure ssh 

	cd post
	vim configure_ssh.ini

Issue the commands from the **configure_ssh** file.

## 4.2 format hdfs

	cd post
	vim format_hdfs.ini

Issue the commands from the **format_hdfs** file.

# 5. play with cluster
Please run the following commands as **hduser** and on **master node only**! 

`su - hduser`

## 5.1 hadoop

## 5.1.1 start hadoop

	cd /home/hduser
	./hadoop/bin/start-dfs.sh
	./hadoop/bin/start-mapred.sh
or 

	cd /home/hduser
	./hadoop/bin/start-all.sh

## 5.1.2 run a mapreduce task
See `examples/java/wordcount/`.

## 5.1.3 stop hadoop

	cd /home/hduser
	./hadoop/bin/stop-mapred.sh
	./hadoop/bin/stop-dfs.sh
or 

	cd /home/hduser
	./hadoop/bin/stop-all.sh

## 5.2 hbase

## 5.2.1 play with hbase

### 5.2.1.1 start hbase

	cd /home/hduser
	./hadoop/bin/start-dfs.sh
	./hbase/bin/start-hbase.sh

### 5.2.1.2 run hbase shell

	cd /home/hduser
	./hbase/bin/hbase shell

### 5.2.1.3 stop hbase

	cd /home/hduser
	./hbase/bin/stop-hbase.sh
	./hadoop/bin/stop-dfs.sh

## 5.2.2 play with rest

## 5.2.2.1 start rest
**NOTICE**: Please start hbase first.

	./hbase/bin/hbase-daemon.sh start rest -p 8080

## 5.2.2.2 access rest services

	curl http://master:8080/
	curl http://master:8080/version
	curl http://master:8080/version/cluster
	curl http://master:8080/status/cluster

## 5.2.2.3 stop rest

	./hbase/bin/hbase-daemon.sh stop rest

## 5.2.3 play with thrift

## 5.2.3.1 start thrift
**NOTICE**: Please start hbase first.

	./hbase/bin/hbase-daemon.sh start thrift -p 9090

## 5.2.3.2 access thrift services
See `examples/python/pyhbase/gis.py` for accessing hbase by using hbase/thrift python library. 

## 5.2.3.3 stop thrift

	./hbase/bin/hbase-daemon.sh stop thrift

# 6. set up a separate zookeeper for cluster

## 6.1 edit zookeeper confs
Please run the following commands as **root** and on **master node only**! 

`su - root`

	cd ./conf/zookeeper/
	vim hbase-site.xml
	vim zoo.cfg

## 6.2 install zookeeper

	./install_zookeeper

## 6.3 play with zookeeper
Please run the following commands as **hduser** and on **master node only**! 

`su - hduser`

### 6.3.1 start zookeeper

	cd /home/hduser
	./hadoop/bin/start-dfs.sh
	./zookeeper/bin/zkServer.sh start
	./hbase/bin/start-hbase.sh

### 6.3.2 stop zookeeper

	cd /home/hduser
	./hbase/bin/stop-hbase.sh
	./zookeeper/bin/zkServer.sh stop
	./hadoop/bin/stop-dfs.sh
