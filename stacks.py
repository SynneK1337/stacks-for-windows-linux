#!/usr/bin/env python
import os
import pathlib

file_type_by_extension = {
    'Images': [
        '.jpg', '.jpeg', '.jfif', '.jpe', '.jif', '.jfi',      
        '.jp2', '.j2k', '.jpf', '.jpx', 'jpm', 'mj2',          
        '.tiff', '.tif',                                       
        '.gif',                                                
        '.bmp', '.dib',                                        
        '.png',                                                
        '.pbm', '.pgm', '.ppm', '.pnm',                        
        '.webp',                                               
        '.heif', '.heic',                                      
        '.3fr', '.ari', '.arw', '.srf', '.sr2', '.bay',        
        '.crw', '.cr2', '.cap', '.iiq', '.eip', '.dcs',        
        '.dcr', '.drf', '.k25', '.kdc', '.dng', '.erf',        
        '.fff', '.mef', '.mos', '.mrw', '.nef', '.nrw',        
        '.orf', '.ptx', '.pef', '.pxn', '.r3d', '.raf',        
        '.raw', '.rw2', '.rw1', '.rwz', '.x3f'                 
    ],
    'Videos': [
        '.webm', '.mkv', '.flv', '.vob', '.ogv' '.ogg',
        '.drc', '.gifv', '.mng', '.avi', '.mts', '.m2ts',
        '.mov', '.qt', '.wmv', '.yuv', '.rm', '.rmvb',
        '.asf', '.amv', '.mp4', '.m4p', '.m4v', '.mpg',
        '.mp2', '.mpeg', '.mpe', '.mpv', '.m2v', '.m4v',
        '.svi', '.3gp', '.3g2', '.mxf', '.roq', '.nsv',
        '.fl4', '.f4p', '.f4v', '.f4a', '.f4b'
    ],
    'Audio': [
        '.3gp', '.aa', '.aac', '.aax', '.act', '.aiff',
        '.amr', '.ape', '.au', '.awb', '.dct', '.dss',
        '.dvf', '.flac', '.gsm', '.iklax', '.ivs', '.m4a',
        '.m4b', '.m4p', '.mmf', '.mp3', '.mpc', '.msv',
        '.nmf', '.nsf', '.ogg', '.oga', '.mogg', '.opus',
        '.ra', '.rm', '.tta', '.vox', '.wav', '.wma',
        '.wv', '.webm', '.8svx'
    ],
    'Source codes': [
        '.C', '.cc', '.cpp', '.cxx', '.c++', '.h', '.hh',
        '.hpp', '.hxx', '.h++', '.py', '.pyc', '.c',
        '.java', '.class', '.bash', '.sh', '.bat', '.ps1',
        '.perl', '.asm', '.S', '.js', '.html', '.css',
        '.scss', '.ts', '.go', '.rs', '.json', '.bin'
    ],
    'Documents': [
        '.txt', '.doc', '.docx', '.pptx', '.ppt', '.xls',
        '.xlsx', '.md', '.pdf', '.odt', '.ods', '.odp',
        '.odf', '.odb'
    ],
    'Apps': [
        '.exe', '.elf', '.lnk', '.msi'
    ],
    'Archives': [
        '.zip', '.rar', '.7z', '.gz', '.bz2', '.Z', '.lzma',
        '.tar', '.xz'
    ],
    'Adobe files': [
        '.psd', '.aep', '.prproj', '.ai', '.xd'
    ]
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
