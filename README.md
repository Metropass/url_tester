# url_tester
This tests if a URL passed a check, or if it's dead


# Setting Up the Script

After you have cloned the respository, you *must* run this command in order to execute the script while omitting '.py':

**pip3 install --editable .**

This will install any missing libraries, and allows dynamic editing on the script.

# How to run the Script

The syntax for the script is the following:

**release0_1 \[command] [arg]**

# Commands

## url

**url**: pass a url as an argument to test for. This only tests the argument link, and is not recursive.
 
    example: **release0_1 url https://www.youtube.com/watch?v=zILpjFqlOak**

**--l**: an option for the **url** command that allows you to search through a website for dead links given the url
    
    example: **release0_1 url --l https://www.youtube.com/watch?v=zILpjFqlOak**

**--s**: an option for the **url** command that allows you to search through a website for http links and sees if they work as https
    
    example: **release0_1 url --s https://www.youtube.com/watch?v=zILpjFqlOak**

## file

**file**: pass a file as an argument to test links inside. If the file has multiple links, it will test those as well.

    example: **release0_1 file test.html**

**--s**: an option for the **file** command that allows you to search through a file for http links and sees if they work as https
    
    example: **release0_1 url --s C:\Users\user1\Documents\file.html**

**version**: returns you the version of this code 

    example: **release0_1 version**

**--help**: gives you the lists of commands for help

    example: **release0_1 --help**
