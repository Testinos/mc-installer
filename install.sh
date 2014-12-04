#!/bin/bash
yum -y groupinstall 'Development Tools'
cd /etc/yum.repos.d
wget http://www.hop5.in/yum/el6/hop5.repo 
yum update 
yum -y install unzip bzip2-devel libtool libevent-devel libcap-devel openssl-devel bison flex snappy-devel numactl-devel cyrus-sasl-devel
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cd ~
git clone https://github.com/Testinos/master.git
cp master/spec/* ~/rpmbuild/SPECS
cp master/patch/* ~/rpmbuild/SOURCES
cd ~/rpmbuild/SOURCES
wget http://ftp.gnu.org.ua/gnu/autoconf/autoconf-2.69.tar.xz
wget http://github.com/schuhschuh/gflags/archive/v2.1.1/gflags-2.1.1.tar.gz
wget https://google-glog.googlecode.com/files/glog-0.3.3.tar.gz
wget http://www.colm.net/files/ragel/ragel-6.9.tar.gz
wget https://codeload.github.com/floitsch/double-conversion/tar.gz/master -O double-conversion-master.tar.gz
rpmbuild -bb ~/rpmbuild/SPECS/* 
cd ~/rpmbuild/RPMS/x86_64/
rpm -ivh double-conversion-devel-master-1.el6.x86_64.rpm double-conversion-master-1.el6.x86_64.rpm gflags-2.1.1-6.el6.x86_64.rpm gflags-devel-2.1.1-6.el6.x86_64.rpm glog-0.3.3-8.el6.x86_64.rpm glog-devel-0.3.3-8.el6.x86_64.rpm ragel-6.9-2.3.x86_64.rpm 
rpm -Uvh ~/rpmbuild/RPMS/noarch/autoconf-2.69-12.2.noarch.rpm
echo '/usr/local/lib' >> /etc/ld.so.conf.d/libs.conf && ldconfig
yum -y install centos-release-SCL
yum -y install python27
scl enable python27 "easy_install pip"
scl enable python27 bash
cd /opt && git clone https://github.com/facebook/folly.git
cd /opt/folly/folly/ && autoreconf -ivf
./configure
make && make install
ldconfig
cd /opt/folly/folly/test
wget https://googletest.googlecode.com/files/gtest-1.6.0.zip
unzip gtest-1.6.0.zip

cd /opt && git clone https://github.com/facebook/fbthrift.git
cd fbthrift/thrift
ln -sf thrifty.h "/opt/fbthrift/thrift/compiler/thrifty.hh"
autoreconf -ivf
./configure --enable-boostthreads
cd /opt/fbthrift/thrift/compiler && make
cd /opt/fbthrift/thrift/lib/thrift && make
cd /opt/fbthrift/thrift/lib/cpp2 && make gen-cpp2/Sasl_types.h
cd /opt/fbthrift/thrift/lib/cpp2/test && make gen-cpp2/Service_constants.cpp
cd /opt/fbthrift/thrift && make && make install


cd /opt && git clone https://github.com/facebook/mcrouter.git
cd mcrouter/mcrouter
autoreconf -ivf && ./configure
make && make install
mcrouter --help
