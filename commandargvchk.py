#!/usr/bin/python3
#-----------------------------------------------------------------------------#
#       Creating python Script to handle command line argument for cloning    #
#   git repository with specific branch                                       #
#-----------------------------------------------------------------------------#
import sys
from git import repo
import os
if len(sys.argv) != 4:
    print(sys.argv)
    print ('ERROR: MISSING INPUT PARMS SHOULD BE IN 4')
    print ('ERROR: Usage should be gitclonebranch.py remoteurl branch destinationfolder')
    sys.exit(0)


