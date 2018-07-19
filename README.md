# Simple Google Drive API implementation


## Overview

It can be a bit tricky to get started with the Google Drive API. This project provides a simple framework in Python to get started.


## Setup

First you need to obtain a 'credentials.json' file and a 'client_secret.json' file.<br>
This is possible by enabling the Drive API in this link:<br>
https://developers.google.com/drive/api/v3/quickstart/python
In this process, you can save the 'credentials.json' file.

For the 'client_secret.json' file, go to<br>
https://console.developers.google.com <br>
and click the Credentials tab. There you can download 'client_secret.json'.


## Code

In 'drivetalk.py', you will need to complete an authentication flow the first time you connect to the API. After this flow, export your credentials using the pickle library. That way, you can just import your credentials back into the workspace, as an attribute to your drivetalk class instance, without having to complete the annoying flow sequence.

So, the first time, you do this:
```python
dt = drivetalk()
dt.generateCreds('credentials.json', 'client_secret.json')
dt.exportCreds('myCreds.pkl')
```

And then the next time, you simply do this:
```python
dt = drivetalk()
dt.importCreds('myCreds.pkl')
```


