from pathlib import Path
import os
import requests

def attempt_download(file, repo='ultralytics/yolov5'):
    '''
    Download models with curl. Torch downloader has been erased to reduce code dependences.
    '''
    # Attempt file download if does not exist
    file = Path(str(file).strip().replace("'", '').lower())
    
    if not file.exists():
        # github api
        response = requests.get(f'https://api.github.com/repos/{repo}/releases/latest').json()
        assets = [x['name'] for x in response['assets']]                                        # release assets, i.e. ['yolov5s.pt', 'yolov5m.pt', ...]
        tag = response['tag_name']                                                              # i.e. 'v1.0'
        print(assets)

        name = file.name
        if name in assets:
            try:
                url = f'https://storage.googleapis.com/{repo}/ckpt/{name}'
                print(f'Downloading {url} to {file}...')
                os.system(f'curl -L {url} -o {file}')
            except:
                if not file.exists() or file.stat().st_size < 1E6:  # check
                    file.unlink(missing_ok=True)  # remove partial downloads
                    print(f'ERROR: Download failure: {msg}')
                print('')
                return

if __name__ == '__main__':

   ## --img 640 models
   #files_640 = ['yolov5s.pt', 'yolov5m.pt', 'yolov5l.pt']#, 'yolov5x.pt']
   
   ## --img 1280 models
   #files_1280 = ['yolov5s6.pt', 'yolov5m6.pt', 'yolov5l6.pt', 'yolov5x6.pt']
   
   files = ['yolov5s.pt']

   for file in files:
      attempt_download(file)
