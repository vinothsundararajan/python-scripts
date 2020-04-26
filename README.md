[![ Travis-Build Status](https://travis-ci.org/vinothsundararajan/python-scripts.svg?branch=master)](https://travis-ci.org/vinothsundararajan/python-scripts)

### python-scripts

- first_helloworld.py
maintenance - Print hello world in console.
- forloop1.py
maintenance - Array of index, forloop and if and else condition covered.
- functions.py
maintenance - Functions with input parms handle & handled format with multiple arugs in print.
- create_directory.py
maintenance - creating the master directory and creating the child directory with array of objs.
- variables_structure.py
maintenance - types of variable assignments.
- dictionary.py
maintenance - collection of list how can proceed with it.
- dictionary_json.py
maintenance - collection of json input to iterate into the python dictionary.
- basics.py
maintenance - collection classes and objects with references.
- pipeline/jenkinsfile
maintenance - wrote jenkins files to automate in and out of creating build opertion using GITHUB jenkins job.
- reminder/reminder.py
maintenance - wrote reminder python program from "https://www.geeksforgeeks.org/birthday-reminder-application-python/" to test windows10toaster and looking to integrate email option.
- reminder/taskreminder.py
maintenance - wrote task based reminder python program from reminder.py to test task based work on basics of every minute.
- .travis.yml - Free Open Source Tool 12-4-2020   
maintenance - added to check how travis ci works
- base64/base64codes.py
maintenance - created Tkinter app for conver base64 codes from encode and decode.
- googlesearch.py
maintenance - created script to search online.


### Docker images handle
- docker search newimages
- docker pull imagename
- docker run -it imagename /bin/bash
    run to activate 
    it - interactive session
    imagename - docker image
    /bin/bash (linux) or cmd (windows)
- docker ps
    will show current process
    (-a) will show all history
- docker exec 5dcfbe74e100 container_id /usr/local/tomcat/bin/catalina.sh run
- docker run --rm -it -p 8443:8080 tomcat:latest
