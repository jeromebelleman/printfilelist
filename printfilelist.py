'''
List files in an evim buffer, ready for printing
'''

import subprocess
from gi.repository import Nautilus, GObject


def printfilelist(_, files):
    '''
    Load file list into evim
    '''

    proc = subprocess.Popen(['evim', '-'], stdin=subprocess.PIPE)
    proc.communicate('\n'.join([fle.get_name() for fle in files]))


class PrintFileList(GObject.GObject, Nautilus.MenuProvider):
    '''
    Menu provider
    '''

    def get_file_items(self, _, files): # pylint: disable=arguments-differ
        item = Nautilus.MenuItem(name='Nautilus::printfilelist',
                                 label='Print File List')
        item.connect('activate', printfilelist, files)
        return item,
