import requests
import os

def download_file(url):
    local_filename = 'fixtures/'+ url.split('/')[-1]
    if not os.path.exists(os.path.dirname(local_filename)):
        try:
            os.makedirs(os.path.dirname(local_filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    print local_filename
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

print download_file('http://www.ssa.gov/oact/babynames/state/namesbystate.zip')
