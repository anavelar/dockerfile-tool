import wget
import sys
import logging
import os
import git
import shutil
import json

temp_repo_path = "./temp"
available_repos_dict = {}

try:
  entriesfile = wget.download(sys.argv[1])
except:
  logging.exception("dockerfile-list-tool expects a URL pointing to a plain text file as argument, aborting the execution.")
  sys.exit(1)

try:
  file = open(entriesfile, "r")
except:
  logging.exception("The text file could not be read.")
  os.remove("./" + entriesfile)
  sys.exit(1)

for line in file:
  repo_data = line.split(" ")
  try:
    repo = git.Repo.clone_from(repo_data[0], temp_repo_path)
    repo.head.reference = repo.commit(repo_data[1])
    repo.head.reset(index=True, working_tree=True)
    repo_dict = {}
    for dirpath, dirlist, filelist in os.walk(temp_repo_path):
      for filename in filelist:
        if (str(filename) == "Dockerfile"):
          try:
            dockerfile = open(dirpath+"/Dockerfile", "r")
          except:
            logging.exception("It was not possible to open "+dirpath+"/Dockerfile, abort.")
            continue
          list_dockerfile_from = []
          for dockerfile_line in dockerfile:
            if(dockerfile_line.startswith("FROM")):
              dockerfile_data = dockerfile_line.split(" ")
              list_dockerfile_from.append(dockerfile_data[1].strip("\n"))
          dockerfile.close()
          repo_dict[dirpath[7:]+"/Dockerfile"] = list_dockerfile_from
    shutil.rmtree(temp_repo_path)
    available_repos_dict[repo_data[0]+":"+repo_data[1]] = repo_dict 
  except:
    logging.exception("Entry \'" + line + "\' could not be scanned, please check the syntax.")
    continue

output = json.dumps({"data":available_repos_dict}, indent=2)

try:
  json_file = open("imageslist.json", "wt")
  json_file.write(output)
  json_file.close()
except:
  logging.exception("The output file could not be created, please remove previous file.")

try:
  file.close()
except:
  logging.exception("The text file could not be closed.")

os.remove("./" + entriesfile)
sys.exit(0)
