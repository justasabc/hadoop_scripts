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
* ZoopKeeper: 3.4.5

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

## 2.7 edit zoopkeeper confs


# 3. install 
Please run the following commands as **root** and on **all nodes**! 

`su - root`


## 3.1 install hadoop

	./install_hadoop

## 3.1.1 update hadoop for **MASTER NODE ONLY**

	./update_masters_slaves

## 3.2 install hbase

	./install_hbase

## 3.2.1 update hbase for **MASTER NODE ONLY**

	./update_regionservers

# 4. post-install (**MASTER ONLY**) 
Please run the following commands as **hduser** and on **master node only**! 

`su - hduser`

## 4.1 configure ssh 

	cd post
	vim configure_ssh.ini

## 4.2 format hdfs
	cd post
	vim format_hdfs.ini

# 5. play with cluster

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
	./hbase/bin/start-hbase.sh
	
## 5.2.2 stop hbase

	cd /home/hduser
	./hbase/bin/stop-hbase.sh
