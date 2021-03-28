 # 0x00-SHELL BASICS
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/205/image.jpg" width=100%>

### man or help

-   `cd`-   `ls`-   `pwd`-   `less`-   `file`-   `ln`-   `cp`-   `mv`-   `rm`-   `mkdir`-   `type`-   `which`-   `help`-   `man`
## Learning Objectives
### General
-   What does **RTFM** mean?
-   What is a **Shebang**
### What is the Shell
-   What is the shell
-   What is the difference between a terminal and a shell
-   What is the shell prompt
-   How to use the history (the basics)
### Navigation
-   What do the commands or built-ins  `cd`,  `pwd`,  `ls`  do
-   How to navigate the filesystem
-   What are the . and .. directories
-   What is the working directory, how to print it and how to change it
-   What is the root directory
-   What is the home directory, and how to go there
-   What is the difference between the root directory and the home directory of the user root
-   What are the characteristics of hidden files and how to list them
-   What does the command  `cd -`  do
### Looking Around
-   What do the commands  `ls`,  `less`,  `file`  do
-   How do you use options and arguments with commands
-   Understand the ls long format and how to display it
-   What does the  `ln`  command do
-   What do you find in the most common/important directories
-   What is a symbolic link
-   What is a hard link
-   What is the difference between a hard link and a symbolic link
### Manipulating Files
-   What do the commands  `cp`,  `mv`,  `rm`,  `mkdir`  do
-   What are wildcards and how do they work
-   How to use wildcards
### Working with Commands
-   What do  `type`,  `which`,  `help`,  `man`  commands do
-   What are the different kinds of commands
-   What is an alias
-   When do you use the command help instead of man
### Reading Man Pages
-   How to read a man page
-   What are man page sections
-   What are the section numbers for User commands, System calls and Library functions
### Keyboard Shortcuts for Bash
-   Common shortcuts for Bash
### LTS
-   What does  `LTS`  mean?
## Requirements
-   All your scripts will be tested on Ubuntu 14.04 LTS
-   All your scripts should be exactly two lines long (`$ wc -l file`  should print 2)
-   All your files should end with a new line
-  The first line of all your files should be exactly  `#!/bin/bash`
-  All your scripts must be executable. To make your file executable, use the `chmod` command: `chmod u+x file`
- All files can be executed with ./name_of_file
## Tasks
### 0. Hello World
Write a script that prints the absolute path name of the current working directory.
Example:
```
$ ./0-current_working_directory
/Users/holbertonschool/holbertonschool-sysadmin_devops/0x00-shell_basics
$
```
-   File:  `0-current_working_directory`
### 1. What’s in there?
Display the contents list of your current directory.
Example:
```
$ ./1-listit
Applications    Documents   Dropbox Movies Pictures
Desktop Downloads   Library Music Public
$
```
-   File:  `1-listit`

### 2. There is no place like home
Write a script that changes the working directory to the user’s home directory.
-   You are not allowed to use any shell variables
```
/tmp$ source ./2-bring_me_home
:~$ pwd
/home/user
```
-   File:  `2-bring_me_home`
### 3. The long format
Display current directory contents in a long format
Example:
```
$ ./3-listfiles
total 32
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
$
```
-   File:  `3-listfiles`
### 4. Hidden files
Display current directory contents, including hidden files (starting with  `.`). Use the long format.
Example:
```
$ ./4-listmorefiles
total 32
drwxr-xr-x@ 6 sylvain staff 204 Jan 25 00:29 .
drwxr-xr-x@ 43 sylvain staff 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:41 4-listmorefiles
$
```
-   File:  `4-listmorefiles`
### 5. I love numbers
Display current directory contents.
-   Long format
-   with user and group IDs displayed numerically
-   And hidden files (starting with .)

Example:
```
$ ./5-listfilesdigitonly
total 32
drwxr-xr-x@ 6 501 20 204 Jan 25 00:29 .
drwxr-xr-x@ 43 501 20 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:23 1-listfiles
-rwxr-xr-x@ 1 501 20 19 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 501 20 20 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:41 4-listmorefiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:43 5-listfilesdigitonly
$
```
-   File:  `5-listfilesdigitonly`
### 6. Welcome holberton
Create a script that creates a directory named  `holberton`  in the  `/tmp/`  directory.
Example:
```
$ ./6-firstdirectory
$ file /tmp/holberton/
/tmp/holberton/: directory
$
```
-   File:  `6-firstdirectory`
### 7. Betty in Holberton
Move the file  `betty`  from  `/tmp/`  to  `/tmp/holberton`.
Example:
```
$ ./7-movethatfile
$ ls /tmp/holberton/
betty
$
```
-   File:  `7-movethatfile`
### 8. Bye bye Betty
Delete the file  `betty`.
-   The file  `betty`  is in  `/tmp/holberton`

Example:
```
$ ./8-firstdelete
$ ls /tmp/holberton/
$
```
-   File:  `8-firstdelete`
### 9. Bye bye Holberton
Delete the directory  `holberton`  that is in the  `/tmp`  directory.
Example:
```
$ ./9-firstdirdeletion
$ file /tmp/holberton
/tmp/holberton: cannot open `/tmp/holberton' (No such file or directory)
$
```
-   File:  `9-firstdirdeletion`
### 10. Back to the future
Write a script that changes the working directory to the previous one.

```
julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ cd /var
julien@ubuntu:/var$ pwd
/var
julien@ubuntu:/var$ source ./10-back
/tmp
julien@ubuntu:/tmp$ pwd
/tmp
```
-   File:  `10-back`
### 11. Lists
Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the  `/boot`  directory (in this order), in long format.
-   File:  `11-lists`
### 12. File type
Write a script that prints the type of the file named  `iamafile`. The file  `iamafile`  will be in the  `/tmp`  directory when we will run your script.
Example
```
ubuntu@ip-172-31-63-244:~$ ./12-file_type
/tmp/iamafile: ELF 64-bit LSB  executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=bd39c07194a778ccc066fc963ca152bdfaa3f971, stripped
```
-   File:  `12-file_type`
### 13. We are symbols, and inhabit symbols
Create a symbolic link to  `/bin/ls`, named  `__ls__`. The symbolic link should be created in the current working directory.

```
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 144
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
ubuntu@ip-172-31-63-244:/tmp/sym$./13-symbolic_link
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 144
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
```
-   File:  `13-symbolic_link`
### 14. Copy HTML files
Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
You can consider that all HTML files have the extension  `.html`
-   File:  `14-copy_html`
### 15. Let’s move
Create a script that moves all files beginning with an uppercase letter to the directory  `/tmp/u`.
You can assume that the directory  `/tmp/u`  will exist when we will run your script
```
ubuntu@ip-172-31-63-244:/tmp/sym$ ./15-lets_move
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 148
drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
```
-   File:  `15-lets_move`
### 16. Clean Emacs
Create a script that deletes all files in the current working directory that end with the character  `~`.
```
ubuntu@ip-172-31-63-244:/tmp/sym$ ls
main.c  main.c~  Makefile~
ubuntu@ip-172-31-63-244:/tmp/sym$ ./16-clean_emacs
ubuntu@ip-172-31-63-244:/tmp/emacs$ ls
main.c
ubuntu@ip-172-31-63-244:/tmp/emacs$
```
-   File:  `16-clean_emacs`
### 17. Tree
Create a script that creates the directories  `welcome/`,  `welcome/to/`  and  `welcome/to/holberton`  in the current directory.
You are only allowed to use two spaces (and lines) in your script, not more.
```
julien@ubuntu:/tmp/h$ ./17-tree 
julien@ubuntu:/tmp/h$ ls
17-tree  welcome
julien@ubuntu:/tmp/h$ ls welcome/
to
julien@ubuntu:/tmp/h$ ls -l welcome/to
total 4
drwxrwxr-x 2 julien julien 4096 Sep 20 12:11 holberton
julien@ubuntu:/tmp/h$ 
```
-   File:  `17-tree`
### 18. Life is a series of commas, not periods
Write a command that lists all the files and directories of the current directory, separated by commas (`,`).

-   Directory names should end with a slash (`/`)  
    
-   Files and directories starting with a dot (`.`) should be listed  
    
-   The listing should be alpha ordered, except for the directories  `.`  and  `..`  which should be listed at the very beginning
-   Only digits and letters are used to sort; Digits should come first
-   You can assume that all the files we will test with will have at least one letter or one digit
-   The listing should end with a new line
```
ubuntu@ip-172-31-63-244:~/holbertonschool$ ./18-commas
./, ../, 0-commas, 0-commas-checks/, 1-empty_casks, 2-gifs, 3-directories, 4-zeros, 5-rot13, 6-odd, 7-sort_rot13, Makefile, quote, .test, test_dir/, test.var
ubuntu@ip-172-31-63-244:~/holbertonschool$
```
-   File:  `18-commas`
### 19. File type: Holberton
Create a magic file  `holberton.mgc`  that can be used with the command  `file`  to detect  `Holberton`  data files.  `Holberton`  data files always contain the string  `HOLBERTON`  at offset 0.
**holberton.mgc has to be created on Ubuntu 14.04 LTS**
```
ubuntu@ip-172-31-63-244:/tmp/magic$ file --mime-type -m holberton.mgc *
holberton.mgc:         application/octet-stream
ls:                    application/octet-stream
thisisanholbertonfile: Holberton
thisisatextfile:       text/plain
ubuntu@ip-172-31-63-244:/tmp/magic$ file -m holberton.mgc *
holberton.mgc:         data
ls:                    data
thisisanholbertonfile: Holberton data
thisisatextfile:       ASCII text
ubuntu@ip-172-31-63-244:/tmp/magic$
```
-   File:  `holberton.mgc`
## Author:
Toshi Borgia
