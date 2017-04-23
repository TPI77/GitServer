#!/usr/bin/python
from git import *
from getpass import getpass
import os, shutil

try:
   username = raw_input("Username [defaul=git]: ") or "git"
   workdir = raw_input("Workdir [default=/tmp]: ") or "/tmp"
   git_server = raw_input("Git Server [default=127.0.0.1]: ") or "127.0.0.1"
   project = raw_input("Projectname: ")
   gitbase = "root"
   basedir = os.chdir(workdir)

   def clone():
      try:
         repo = Repo.clone_from("http://%s@%s/%s/%s.git" %(username, git_server, gitbase, project), "%s" %project)
         print(" %s cloned.."%project)
      except GitCommandError:
         print(" Cloning into an existing directory is only allowed if the directory is empty")
         answer = raw_input(" Would you like to remove the contents from this directory? [y/n]: ")
         if answer == "y": 
           ld = "/tmp/%s"%project
           rm = os.listdir("/tmp/%s"%project)
           for a in rm:
              print("about to remove %s"%a)
           try:
              cm = shutil.rmtree(ld)
              print " File(s) removed.."
              clone()
           except OSError:
              print " Failed to remove.."
   clone()
except KeyboardInterrupt:
   print " \nInterrupt by user.."



###commit
# Repo.commit("v0.1")
# Repo.init(workdir)
# Repo.index.add(workdir)
#r.index.add([file_name])
#r.index.commit("initial commit")

#push
#remote origin
#add
#init
#config
