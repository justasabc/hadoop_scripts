Hadoop/Hbase Fully-Distributed Installer Scripts
==========================================

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

## 3.1.1 update hadoop (**MASTER NODE ONLY**)

	./update_masters_slaves

## 3.2 install hbase

	./install_hbase

## 3.2.1 update hbase (**MASTER NODE ONLY**)

	./update_regionservers

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
	
## 5.1.2 stop hadoop

	cd /home/hduser
	./hadoop/bin/stop-mapred.sh
	./hadoop/bin/stop-dfs.sh

## 5.2 hbase
## 5.2.1 start hbase

	cd /home/hduser
	./hadoop/bin/start-dfs.sh
	./hbase/bin/start-hbase.sh
	
## 5.2.2 stop hbase

	cd /home/hduser
	./hbase/bin/stop-hbase.sh
	./hadoop/bin/stop-dfs.sh

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
