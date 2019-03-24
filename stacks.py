#!/usr/bin/env python
import os
import pathlib

file_type_by_extension = {'images':
                          ['.jpg', '.jpeg', '.jfif', '.jpe', '.jif', '.jfi',      # JPEG
                           '.jp2', '.j2k', '.jpf', '.jpx', 'jpm', 'mj2',          # JPEG 2000
                           '.tiff', '.tif',                                       # TIFF
                           '.gif',                                                # GIF
                           '.bmp', '.dib',                                        # BMP
                           '.png',                                                # PNG
                           '.pbm', '.pgm', '.ppm', '.pnm',                        # PPM
                           '.webp',                                               # WebP
                           '.heif', '.heic',                                      # HEIF
                           '.3fr', '.ari', '.arw', '.srf', '.sr2', '.bay',        # RAW
                           '.crw', '.cr2', '.cap', '.iiq', '.eip', '.dcs',        # RAW
                           '.dcr', '.drf', '.k25', '.kdc', '.dng', '.erf',        # RAW
                           '.fff', '.mef', '.mos', '.mrw', '.nef', '.nrw',        # RAW
                           '.orf', '.ptx', '.pef', '.pxn', '.r3d', '.raf',        # RAW
                           '.raw', '.rw2', '.rw1', '.rwz', '.x3f'                 # RAW
                           ],
                          'videos':
                          ['.webm', '.mkv', '.flv', '.vob', '.ogv' '.ogg',
                           '.drc', '.gifv', '.mng', '.avi', '.mts', '.m2ts',
                           '.mov', '.qt', '.wmv', '.yuv', '.rm', '.rmvb',
                           '.asf', '.amv', '.mp4', '.m4p', '.m4v', '.mpg',
                           '.mp2', '.mpeg', '.mpe', '.mpv', '.m2v', '.m4v',
                           '.svi', '.3gp', '.3g2', '.mxf', '.roq', '.nsv',
                           '.fl4', '.f4p', '.f4v', '.f4a', '.f4b'
                           ],
                          }


def get_desktop_path():
    return os.path.expanduser("~/Desktop")


def get_file_type(file, types):  # types = file_type_by_extension
    for type, extension in types.items():
        if pathlib.Path(file).suffix.lower() in extension:
            return type


def create_folders(types):     # types = file_type_by_extension
    for type_ in types:
        os.makedirs(type_, exist_ok=True)


if __name__ == "__main__":
    os.chdir(get_desktop_path())  # cd ~/Desktop
    create_folders(file_type_by_extension)
    files = os.listdir()   # ls
    for file in files:
        if get_file_type(file, file_type_by_extension):
            os.rename(file, os.path.join(get_file_type(file,
                                                       file_type_by_extension), file))
    for folder in file_type_by_extension:
        if not os.listdir(folder):
            os.removedirs(folder)
