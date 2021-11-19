# Download Cleaner for SE's

## What this project does

This project allows you to delete the following folders and files within your Download repository:

* Datadog Flare Zip File
* Datadog Cluster Agent Flare Zip File
* Datadog Flare Extracted Folder
* Datadog Cluster Agent Flare Extracted Folder
* Helm Manifest
* Daemonset Manifest
* Unqueried Metrics Value



## How to get Started

In order to getting started with the project, you can either running the **main** executable file which then executes the python project within your host machine. Otherwise, as this is an open source project you can simply execute the command by running it within your terminal line.

```
$ python main.py
```



## How the code works

The project is broken down to three distinct parts, the first being in relation to capturing deleting the the zip flare files with the snippet shown below:

```python
    zipFlareName = "datadog-agent"
    extension = ".zip"
    search_path = str(Path.home() / "Downloads")
```

The snippet above allows the code to capture the zip file with the name beginning with **datadog-agent** and allow it to iterate through the Downloads folder until it has gone through the list of all the flare zip files it can capture. 



The second part is capturing all the extracted flare folder by navigating scanning within the folders itself as seen below:

```python
    path = str(Path.home() / "Downloads")
    file_name = ["status.log", "cluster-agent-status.log"]
```
This section scans through the flare folder and looks for the file names consisting of what is shown within the array file_name. Once this captures that the folder contains status.log or cluster-agent-status.log then it goes back to the download's folder and deletes the file using the following line:

```python
    shutil.rmtree(pathToRemove)
```


Lastly, the third part is in relation to capturing any files which is in relation to a Helm manifest, a Daemonset Manifest or Unqueried CSV files as shown below:

```python
search_path = str(Path.home() / "Downloads")
        file_type = [".yaml", ".yml", ".csv"]
        search_str = ["replicaCount:", "datadog:", "datadogAgents:", "podAnnotations:", "kind: DaemonSet", "kind: Deployment", "AWSTemplateFormatVersion:", "Average Custom Metrics / Hour", "init_config:"]
```
This section scans the file_types within the Downloads folder which looks for any values within the search_str and deletes the file with the following line:

```python
os.remove(search_path + fname)
```
The search_path is the string value that is capturing the path of the download files and the fname is the file that captures the search_str value. 


## Contribution/References

In order to capture the information, we used the following resources to capture further information on how we can extract and remove files:

* https://www.opentechguides.com/how-to/article/python/59/files-containing-text.html
* https://docs.python.org/3/library/os.html
* https://docs.python.org/3/library/shutil.html


# Authors and acknowledgment

Created by Venus Parfait and Kumail Anis