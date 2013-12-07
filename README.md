Hadoop Fully-Distributed Installer Scripts
==========================================

# 1. introduction

## 1.1 description
Hadoop fully-distributed installer scripts and guides for Ubuntu 12.04 Server 64-bit x86. Feel free to get copy of this repository.

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

# 2. pre-modification
Please run the following commands as **root** and on **all nodes**! 

`su - root`

## 2.1 edit hosts 
vim ./conf/hosts

## 2.2 edit hadoop confs

	vim ./conf/hadoop/core-site.xml
	vim ./conf/hadoop/mapred-site.xml
	vim ./conf/hadoop/hdfs-site.xml

## 2.3 edit master/slave confs

	vim ./conf/hadoop/masters
	vim ./conf/hadoop/slaves

# 3. installation for all nodes
Please run the following commands as **root** and on **all nodes**! 

`su - root`

## 3.1 install jdk

	cd pre/jdk/
	./install_jdk

## 3.2 disable ipv6

	cd pre/
	./disable_ipv6

## 3.3 install hadoop

	./install_hadoop

## 3.4 uninstall hadoop(optional)

	./uninstall_hadoop

# 4. update for master node **ONLY**
Please run the following commands as **root** and on **master node only**! 

`su - root`

	./update_master

# 5. start/stop hadoop cluster
Please run the following commands as **hduser** and on **master node only**! 

`su - hduser`

## 5.1 configure ssh 

	cd post
	vim configure_ssh.ini

## 5.2 format hdfs
	cd post
	vim format_hdfs.ini

## 5.3 start hadoop

	cd /home/hduser
	./hadoop/bin/start-dfs.sh
	./hadoop/bin/start-mapred.sh
	
## 5.4 stop hadoop

	cd /home/hduser
	./hadoop/bin/stop-mapred.sh
	./hadoop/bin/stop-dfs.sh
