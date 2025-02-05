Title: Installing MySQL 8.4 on Ubuntu 22.04 
Date: 2025-02-05 18:00
Category: Tech
Tags: linux, tips
Lang: en
Summary: When the official Ubuntu packages are not enough

## Download the official packages from Oracle

On Ubuntu 22.04, the default mysql-server version available through apt is unfortunately an old one (8.0.41), so if you need the current MySQL **LTS** (8.4) you have to install it "manually".

Here are the steps:

* Go to the [MySQL website download page](https://dev.mysql.com/downloads/mysql/)
* Select "Ubuntu Linux"
* Select "Ubuntu Linux 22.04 x86 64 bits"
* Download **DEB Bundle** (click on the link _No thanks, just start my download_ to avoid creating an Oracle account)

This will download the complete list of .deb packages needed for a full install.
From that list you will only need 8 packages.

## Installation

* Install in that order with `sudo apt install`:
    * mysql-common_8.4.4-1ubuntu22.04_amd64.deb
    * mysql-community-server-core_8.4.4-1ubuntu22.04_amd64.deb
    * mysql-community-client-plugins_8.4.4-1ubuntu22.04_amd64.deb
    * mysql-community-client-core_8.4.4-1ubuntu22.04_amd64.deb
    * mysql-community-client_8.4.4-1ubuntu22.04_amd64.deb
    * mysql-client_8.4.4-1ubuntu22.04_amd64.deb
    * mysql-community-server_8.4.4-1ubuntu22.04_amd64.deb
    * mysql-server_8.4.4-1ubuntu22.04_amd64.deb

* Set up a root password (example: root)
* Check if the service is running:

```
$ sudo systemctl status mysql.service 
● mysql.service - MySQL Community Server
     Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2025-02-05 15:17:12 CET; 22min ago
       Docs: man:mysqld(8)
             http://dev.mysql.com/doc/refman/en/using-systemd.html
   Main PID: 27538 (mysqld)
     Status: "Server is operational"
      Tasks: 47 (limit: 37938)
     Memory: 432.5M
        CPU: 13.990s
     CGroup: /system.slice/mysql.service
             └─27538 /usr/sbin/mysqld
```

You're set! Happy SQLing!