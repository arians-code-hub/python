import mmap


class Information:
    @staticmethod
    def linesCount(path):
        with open(path, "r+", encoding='utf-8') as f:
            buf = mmap.mmap(f.fileno(), 0)
            lines = 0
            readline = buf.readline
            while readline():
                lines += 1
            return lines


def run():
    import sys
    sys.path.append('../')
    from arg.Arg import Arg
    options = Arg.keyValue(defaults={
        'command': ''
    })

    if options['command'].lower() == 'linescount':
        print(Information.linesCount(options['path']))


if __name__ == '__main__':
    run()