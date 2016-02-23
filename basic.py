import zipfile
import urllib.request

fixtures_url = "http://www.ssa.gov/oact/babynames/state/namesbystate.zip"

def dl_zipfile(url):
    file = urllib.request.urlopen(url)

def zip_read(archive_link):
    zp = zipfile.ZipFile("./namesbystate.zip", "r").open("*.txt", "r")
    # zp = zipfile.Zipfile(archive_link, 'r')
    for info in zf.infolist():
        print(info.filename)
        print('\tComment:\t', info.comment)
        print('\tModified:\t', datetime.datetime(*info.date_time))
        print('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
        print('\tZIP version:\t', info.create_version)
        print('\tCompressed:\t', info.compress_size, 'bytes')
        print('\tUncompressed:\t', info.file_size, 'bytes')
        print
    print(zf.namelist())
#     try:
#     except HTTPError as e:
#     print 'The server couldn\'t fulfill the request.'
#     print 'Error code: ', e.code
# except URLError as e:
#     print 'We failed to reach a server.'
#     print 'Reason: ', e.reason

if __name__ == '__main__':
    # zip_read('namesbystate.zip')
    dl_zipfile(fixtures_url)
