from glob import glob
from information import Information


class FindFiles:
    @staticmethod
    def byPattern(pattern):
        return glob(pattern,recursive= True)

    @staticmethod
    def countByPattern(pattern):
        return len(FindFiles.byPattern(pattern))

    @staticmethod
    def linesCountByPattern(pattern):
        count = 0
        for path in FindFiles.byPattern(pattern):
            count += Information.linesCount(path)
        return count

    @staticmethod
    def inDir(dir, exts=None):
        if exts:
            basePath = '{0}/**/*{1}'.format(dir,''.join(['[.'+_+']' for _ in exts]))
        else:
            basePath = '{0}/**'.format(dir)
        return FindFiles.byPattern(basePath)

    @staticmethod
    def countInDir(dir, exts=None):
        return len(FindFiles.inDir(dir, exts))

    @staticmethod
    def linesCountInDir(dir, exts=None):
        count = 0
        for path in FindFiles.inDir(dir, exts):
            count += Information.linesCount(path)
        return count


def run():
    import sys
    sys.path.append('../')
    from arg.Arg import Arg
    options = Arg.keyValue(defaults={
        'command': ''
    })

    if options['command'].lower() in ['count']:
        if 'pattern' in options:
            print(FindFiles.countByPattern(options['pattern']))
        elif 'dir' in options or 'path' in options:
            if 'ext' in options:
                print(FindFiles.countInDir(options['dir'] if 'dir' in options else options['path'], options['ext'].split(',')))
            else:
                print(FindFiles.countInDir(options['dir'] if 'dir' in options else options['path']))

    elif options['command'].lower() in ['linescount']:
        if 'pattern' in options:
            print(FindFiles.linesCountByPattern(options['pattern']))
        elif 'dir' in options or 'path' in options:
            if 'ext' in options:
                print(FindFiles.linesCountInDir(options['dir'] if 'dir' in options else options['path'], options['ext'].split(',')))
            else:
                print(FindFiles.linesCountInDir(options['dir'] if 'dir' in options else options['path']))

    elif options['command'].lower() in ['files']:
        if 'pattern' in options:
            print(FindFiles.byPattern(options['pattern']))
        elif 'dir' in options or 'path' in options:
            if 'ext' in options:
                print(FindFiles.inDir(options['dir'] if 'dir' in options else options['path'], options['ext'].split(',')))
            else:
                print(FindFiles.inDir(options['dir'] if 'dir' in options else options['path']))


if __name__ == '__main__':
    run()