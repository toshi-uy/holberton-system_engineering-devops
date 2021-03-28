# 0x01. Shell, permissions
<img src="https://i.imgur.com/TqcfRSL.png" width=100%>

### man or help

-  `chmod`-   `sudo`-   `su`-   `chown`-   `chgrp`-   `id`-   `groups`-   `whoami`-   `adduser`-   `useradd`-   `addgroup`
## Learning Objectives
### Permissions
-   What do the commands  `chmod`,  `sudo`,  `su`,  `chown`,  `chgrp`  do
-   Linux file permissions
-   How to represent each of the three sets of permissions (owner, group, and other) as a single digit
-   How to change permissions, owner and group of a file
-   Why can’t a normal user  `chown`  a file
-   How to run a command with root privileges
-   How to change user ID or become superuser  
### Other Man Pages
-   How to create a user
-   How to create a group
-   How to print real and effective user and group IDs
-   How to print the groups a user is in
-   How to print the effective userid
## Requirements
-   All your scripts will be tested on Ubuntu 14.04 LTS
-   All your scripts should be exactly two lines long (`$ wc -l file`  should print 2)
-   All your files should end with a new line
-  The first line of all your files should be exactly  `#!/bin/bash`
-  All your scripts must be executable. To make your file executable, use the `chmod` command: `chmod u+x file`
- All files can be executed with ./name_of_file
## Tasks
### 0. My name is Betty
Create a script that switches the current user to the user  `betty`.

-   You should use exactly 8 characters for your command (+1 character for the new line)
-   You can assume that the user  `betty`  will exist when we will run your script
```
julien@ubuntu:/tmp/h$ tail -1 0-iam_betty | wc -c
9
julien@ubuntu:/tmp/h$
```
-   File:  `0-iam_betty`
### 1. Who am I
Write a script that prints the effective username of the current user.

```
julien@ubuntu:/tmp/h$ ./1-who_am_i
julien
julien@ubuntu:/tmp/h$ 
```
-   File:  `1-who_am_i`
### 2. Groups
Write a script that prints all the groups the current user is part of.

```
julien@ubuntu:/tmp/h$ ./2-groups
julien adm cdrom sudo dip plugdev lpadmin sambashare
julien@ubuntu:/tmp/h$ 
```
*Note: depending on the user, you will get a different output.*
-   File:  `2-groups`
### 3. New owner
Write a script that changes the owner of the file  `hello`  to the user  `betty`.
```
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 julien julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$ sudo ./3-new_owner 
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 betty  julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$
```
-   File:  `3-new_owner`
### 4. Empty!
Write a script that creates an empty file called  `hello`.
-   File:  `4-empty`
### 5. Execute
Write a script that adds execute permission to the owner of the file  `hello`.
-   The file  `hello`  will be in the working directory
```
julien@ubuntu:/tmp/h$ ./hello
bash: ./hello: Permission denied
julien@ubuntu:/tmp/h$ ./5-execute 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:26 5-execute
-rwxrw-r-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
```
-   File:  `5-execute`
### 6. Multiple permissions
Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file  `hello`.

-   The file  `hello`  will be in the working directory

```
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 36 Sep 20 14:31 6-multiple_permissions
-r--r----- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./6-multiple_permissions 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 36 Sep 20 14:31 6-multiple_permissions
-r-xr-xr-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
```
-   File:  `6-multiple_permissions`
### 7. Everybody!
Write a script that adds execution permission to the owner, the group owner and the other users, to the file  `hello`

-   The file  `hello`  will be in the working directory
-   You are not allowed to use commas for this script
```
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:35 7-everybody
-rw-r----- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./7-everybody 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:35 7-everybody
-rwxr-x--x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```
-   File:  `7-everybody`
### 8. James Bond
Write a script that sets the permission to the file  `hello`  as follows:

-   Owner: no permission at all
-   Group: no permission at all
-   Other users: all the permissions

The file  `hello`  will be in the working directory You are not allowed to use commas for this script
```
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:40 8-James_Bond
-rwxr-x--x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./8-James_Bond 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:40 8-James_Bond
-------rwx 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
```
-   File:  `8-James_Bond`
### 9. John Doe
Write a script that sets the mode of the file  `hello`  to this:
```
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
```
-   The file  `hello`  will be in the working directory
-   You are not allowed to use commas for this script
-   File:  `9-John_Doe`
### 10. Look in the mirror
Write a script that sets the mode of the file  `hello`  the same as  `olleh`’s mode.
-   The file  `hello`  will be in the working directory
-   The file  `olleh`  will be in the working directory
```
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$ ./10-mirror_permissions 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rw-rw-r-- 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$ 
```
Note: the mode of  `olleh`  will not always be 664. Make sure your script works for any mode.
-   File:  `10-mirror_permissions`
### 11. Directories
Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
```
julien@ubuntu:/tmp/h$ ./11-directories_permissions 
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   24 Sep 20 14:53 11-directories_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
```
-   File:  `11-directories_permissions`
### 12. More directories
Create a script that creates a directory called  `dir_holberton`  with permissions 751 in the working directory.
```
julien@ubuntu:/tmp/h$ ./12-directory_permission s
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   39 Sep 20 14:59 12-directory_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 dir_holberton
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
```
-   File:  `12-directory_permissions`
### 13. Change group
Write a script that changes the group owner to  `holberton`  for the file  `hello`
-   The file  `hello`  will be in the working directory
```
julien@ubuntu:/tmp/h$ sudo ./13-change_group 
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      34 Sep 20 15:03 13-change_group
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien    4096 Sep 20 14:59 dir_holberton
-rw-rw-r-- 1 julien holberton   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
```
-   File:  `13-change_group`
### 14. Owner and group
Write a script that changes the owner to  `betty`  and the group owner to  `holberton`  for all the files and directories in the working directory.
```
julien@ubuntu:/tmp/h$ sudo ./14-change_owner_and_group 
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 betty holberton   36 Sep 20 15:06 14-change_owner_and_group
drwx--x--x 2 betty holberton 4096 Sep 20 14:49 dir0
drwx--x--x 2 betty holberton 4096 Sep 20 14:49 dir1
drwx--x--x 2 betty holberton 4096 Sep 20 14:49 dir2
drwxr-x--x 2 betty holberton 4096 Sep 20 14:59 dir_holberton
-rw-rw-r-- 1 betty holberton   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
```
-   File:  `14-change_owner_and_group`
### 15. Symbolic links
Write a script that changes the owner and the group owner of  `_hello`  to  `betty`  and  `holberton`  respectively.
-   The file  `_hello`  is in the working directory
-   The file  `_hello`  is a symbolic link
```
julien@ubuntu:/tmp/h$ sudo ./15-symbolic_link_permissions 
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      44 Sep 20 15:12 15-symbolic_link_permissions
-rw-rw-r-- 1 julien julien      23 Sep 20 14:25 hello
lrwxrwxrwx 1 betty  holberton    5 Sep 20 15:10 _hello -> hello
julien@ubuntu:/tmp/h$ 
```
-   File:  `15-symbolic_link_permissions`
### 16. If only
Write a script that changes the owner of the file  `hello`  to  `betty`  only if it is owned by the user  `guillaume`.
-   The file  `hello`  will be in the working directory
```
julien@ubuntu:/tmp/h$ sudo ./16-if_only 
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      47 Sep 20 15:18 16-if_only
-rw-rw-r-- 1 betty  julien      23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
```
-   File:  `16-if_only`
### 17. Star Wars
Write a script that will play the StarWars IV episode in the terminal.
*Note: you will need to install telnet to run it:*
```
$ apt-get **install telnet**.
```
-   File:  `100-Star_Wars`
## Author:
Toshi Borgia
