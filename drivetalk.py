#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
#
# drivetalk.py


from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file,client,tools
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
import pickle
import io


def main():
    
    dt = drivetalk()
    #dt.generateCreds('credentials.json', 'client_secret.json')
    #dt.exportCreds('myCreds.pkl')
    dt.importCreds('myCreds.pkl')
    dt.generateService()
    #dt.uploadFile('sample.png', '/my/path/to/sample.png', 'image/png', '*** folder ID ***')
    dt.uploadFolder()
    #dt.downloadFile('*** file ID ***', 'sample.png')

    


class drivetalk:

    def __init__(self):
        self.scopes = 'https://www.googleapis.com/auth/drive'
        self.creds = 'no creds yet...'
        self.drive_service = 'no drive_service yet...'

    def generateCreds(self, credentials_file, client_secret_file):
        store = file.Storage(credentials_file)
        flow = client.flow_from_clientsecrets(client_secret_file, self.scopes)
        self.creds = tools.run_flow(flow, store)

    def exportCreds(self,credsFileName):
        f = open(credsFileName, 'wb')
        pickle.dump(self.creds, f, pickle.HIGHEST_PROTOCOL)
        f.close()

    def importCreds(self,fileName):
        f = open(fileName, 'rb')
        self.creds = pickle.load(f)
        f.close()

    def generateService(self):
        self.drive_service = build('drive','v3',http=self.creds.authorize(Http()))
        
    def uploadFile(self, fileName, filePath, mimeType, folderID):
        file_metadata = {'name': fileName, 'parents': [folderID] }
        media = MediaFileUpload(filePath, mimetype=mimeType)
        file = self.drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(file.get('id'))

    def downloadFile(self, file_id, filePath):
        request = self.drive_service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        with io.open(filePath,'wb') as f:
            fh.seek(0)
            f.write(fh.read())

        
if __name__ == '__main__':
    main()
