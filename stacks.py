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
                           ]
                          }


def getDesktopPath():
  if (os.name == 'nt'):
    return os.getenv('HOME')+'\\Desktop\\'  # Windows
  else:
    return os.getenv('HOME')+'/Desktop/'    # *NIX


def getDesktopFiles():
  return os.listdir()


def getFileType(file, types): # types = file_type_by_extension
  for type, extension in types.items():
    if pathlib.Path(file).suffix.lower() in extension:
      return type

def createFolders(types):     # types = file_type_by_extension
  for type in types:
    try:
      os.mkdir(type)
    except:
      pass


if __name__ == "__main__":
  os.chdir(getDesktopPath())  # cd ~/Desktop
  createFolders(file_type_by_extension)
  files = getDesktopFiles()   # ls
  for file in files:
    if os.name == "nt":
      if getFileType(file, file_type_by_extension):
        os.rename(file, (getFileType(file, file_type_by_extension)+"\\"+file))
    else:
      if getFileType(file, file_type_by_extension):
        os.rename(file, (getFileType(file, file_type_by_extension)+"/"+file))
