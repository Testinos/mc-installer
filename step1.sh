#!/bin/bash
yum -y groupinstall 'Development Tools'
wget http://www.hop5.in/yum/el6/hop5.repo -P /etc/yum.repos.d/
yum -y update 
yum -y install unzip bzip2-devel libtool libevent-devel libcap-devel openssl-devel bison flex snappy-devel numactl-devel cyrus-sasl-devel boost-devel python-setuptools cmake
rpm -Uvh http://sourceforge.net/projects/scons/files/scons/2.3.4/scons-2.3.4-1.noarch.rpm
yum -y install centos-release-SCL
yum -y install python27
scl enable python27 "easy_install pip"
scl enable python27 ~/mc-installer/step2.sh

