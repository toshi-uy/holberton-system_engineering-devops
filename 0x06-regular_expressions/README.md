
# 0x06. Regular expression
### Foundations > System engineering & DevOps > Scripting

## Tasks

### 0. Simply matching Holberton


![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210705T193932Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=02835ecf88ac21d55c4213a46a08251637dc982e96713adb6ad1552ef67f90d9)

Requirements:

-   The regular expression must match  `Holberton`
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

```
sylvain@ubuntu$ ./0-simply_match_holberton.rb Holberton | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School" | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School Holberton" | cat -e
HolbertonHolberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Grace Hopper" | cat -e
$

```
-   File:  `0-simply_match_holberton.rb`


### 1. Repetition Token #0


![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210705T193932Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=eb3ec4fba1a32bd9c6b838bfda6ea7ec9ccd23415443694c7d927186c0536776)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

-   File:  `1-repetition_token_0.rb`


### 2. Repetition Token #1


![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210705T193932Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cc7b9de1dd50de47f149862961e9ce167794fef5acf06fe999ca2f59d447e6b2)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

-   File:  `2-repetition_token_1.rb`

### 3. Repetition Token #2


![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210705T193932Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2a5b20db1933c7e6f520a64f5a3678b9d01a032ccfaf1411536dd766942d70b7)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

-   File:  `3-repetition_token_2.rb`

### 4. Repetition Token #3

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/f8dbcb9cf5ae569a8645027dc46e81cb372ce28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210705T193932Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5ec6a3785e7a1287ae57d16d2335d68891e5f76c8c1f7b454cb0aebc83dbdca1)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
-   Your regex should not contain square brackets

-   File:  `4-repetition_token_3.rb`


### 5. Not quite HBTN yet


Requirements:

-   The regular expression must be exactly matching a string that starts with  `h`  ends with  `n`  and can have any single character in between
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

```
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
$

```
-   File:  `5-beginning_and_end.rb`

### 6. Call me maybe

mandatory

This task is brought to you by Holberton professional advisor  [Neha Jain](https://intranet.hbtn.io/rltoken/V4rEpseJEPRMMnfaZPbkgw "Neha Jain"), Senior Software Engineer at LinkedIn.

Requirement:

-   The regular expression must match a 10 digit phone number

Example:

```
sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
sylvain@ubuntu$

```
-   File:  `6-phone_number.rb`

### 7. OMG WHY ARE YOU SHOUTING?

mandatory

![](https://intranet.hbtn.io/images/contents/sysadmin/projects/78/shouting.jpg)

Requirement:

-   The regular expression must be only matching: capital letters

Example:

```
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
sylvain@ubuntu$

```

-   File:  `7-OMG_WHY_ARE_YOU_SHOUTING.rb`

### 8. Textme

This exercise was prepared for you by  [Guillaume Plessis](https://intranet.hbtn.io/rltoken/l2JCUH5R2qdg7YVMYR1UmA "Guillaume Plessis"), VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project  [on Twitter](https://intranet.hbtn.io/rltoken/FuFAuWPWMeiCgyQkh3SwZA "on Twitter").

For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

Requirements:

-   Your script should output:  `[SENDER],[RECEIVER],[FLAGS]`
    -   The sender phone number or name (including country code if present)
    -   The receiver phone number or name (including country code if present)
    -   The flags that were used

You can find a  [log file here](http://intranet-projects-files.s3.amazonaws.com/holbertonschool-sysadmin_devops/78/text_messages.log "log file here").

Example:

```
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
Google,+16474951758,-1:0:-1:0:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-10 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE2] [SVC:] [ACT:] [BINF:] [FID:] [from:+17272713208] [to:+19172319348] [flags:-1:0:-1:0:-1] [msg:136:Orbiting this at a distance of roughly ninety-two million miles is an utterly insignificant little blue green planet whose ape-descended] [udh:0:]'
+17272713208,+19172319348,-1:0:-1:0:-1
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:18572406905] [to:14022180266] [flags:-1:0:-1:-1:-1] [msg:136:Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun.] [udh:0:]'
18572406905,14022180266,-1:0:-1:-1:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:12392190384] [to:19148265919] [flags:-1:0:-1:-1:-1] [msg:99:life forms are so amazingly primitive that they still think digital watches are a pretty neat idea.] [udh:0:]'
12392190384,19148265919,-1:0:-1:-1:-1
$


```
-   File:  `100-textme.rb`

### 9. Pass LinkedIn technical interview level0

One way to get started in getting a Software Engineering job at LinkedIn is to solve their regex puzzle.

Requirements:

-   Solve LinkedIn regex puzzle:  [https://engineering.linkedin.com/puzzle](https://intranet.hbtn.io/rltoken/u2xzwrPyylRY7dpGJJ9P-Q "https://engineering.linkedin.com/puzzle")
-   Provide as an answer file a screenshot of the “Congratulations” screen with the date and time of completion

Example:

![](https://assets.holbertonschool.com/media_images/files/000/001/208/thumb_1000/Screen_Shot_2020-02-25_at_12.56.14_PM.png)

Well, I guess I can get into LinkedIn hiring process:

**It is your responsibility to request a review for this task from a peer. If no peers have been reviewed, you should request a review from a TA or staff member.**

**Repo:**

-   File:  `101-passed_linkedin_regex_challenge.jpg`
