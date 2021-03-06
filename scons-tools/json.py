

def exists(env):
    return True

def generate(env):
    inc_dir = env['dep_dir'].Dir('json-master/include')

    usage = {'CPPSYSTEMPATH': [inc_dir],
             }

    if inc_dir.exists():
        return usage

    import urllib2
    import StringIO
    import zipfile

    response = urllib2.urlopen('https://github.com/nlohmann/json/archive/master.zip')
    contents = StringIO.StringIO(response.read())
    zipped = zipfile.ZipFile(contents)
    members = [filename for filename in zipped.namelist()
               if 'include' in filename or 'LICENSE' in filename]
    zipped.extractall(env['dep_dir'].abspath, members)

    return usage
