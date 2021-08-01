import dropbox

class TransferData:
          def __init__(self,access_token):
               self.access_token=access_token

          def upload_file(self,file_from,file_to):
                    dbx=dropbox.Dropbox(self.access_token) 

                    with open(file_from,'rb') as f:
                              dbx.files_upload(f.read(),file_to)

def main():
          access_token='rz84SfAgHtAAAAAAAAAAAShvRUtBfbq2FX0k3RBozn88FAtEXDi5fDz7mvXw6_DM' 
          transferData=TransferData(access_token)  

          file_from="text1.txt"    
          file_to="/home/Edu-A/text1.txt"         

          transferData.upload_file(file_from,file_to)         

if __name__=='__main__':
          main()    

   