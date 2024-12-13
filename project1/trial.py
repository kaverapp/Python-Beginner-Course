import os
import shutil

# defrose=set(dir(os))



# lst=['spawnl', 'O_CREAT', 'SEEK_END', 'execvpe', 'P_DETACH', 
#  'removedirs', 'EX_OK', 'kill', 'fsdecode', 'chdir', 
#  'execle', 'get_inheritable', 'O_SEQUENTIAL', '__spec__',
#    '_wrap_close', '_exit', 'MutableMapping', 'chmod',
#      'execl', 'remove', 'rmdir', 'write', 'set_handle_inheritable',
#        'get_blocking', 'DirEntry', 'spawnle', 'F_OK', 'O_SHORT_LIVED',
#          'execve', 'uname_result', '__name__', 'execlpe', 'lstat',
#            'TMP_MAX', 'access', '_get_exports_list', 'Mapping', '_fspath',
#              'SEEK_CUR', 'getpid', 'sys', 'utime', 'startfile', '_exists', 
#              'set_blocking', 'fspath', 'extsep', 'O_EXCL', 'curdir',
#               'O_TEXT', 'cpu_count', 'rename', 'link', 'P_NOWAIT',
#               'add_dll_directory', 'path', 
#              'device_encoding', 'listdir', 'get_handle_inheritable', 
#              'supports_follow_symlinks', 'waitstatus_to_exitcode', '_Environ', 'execv', '__builtins__',
#               'waitpid', 'W_OK', 'dup2', 'defpath', 'execvp', 'O_TRUNC', 'terminal_size', 'supports_dir_fd',
#                 'GenericAlias', 'spawnve', 'O_NOINHERIT', 'readlink', 'getlogin', 'X_OK', 'walk', 
#                 'get_exec_path', 'times_result', 'fstat', 'pipe', 'unlink', 'O_BINARY',
#                   'O_RDONLY', '__file__', 'read', 'mkdir', 'O_WRONLY', 'P_WAIT', 'SEEK_SET',
#                     'replace', 'statvfs_result', 'urandom', 'dup', 'scandir', 'stat', 'R_OK', 
#                     'ftruncate', 'supports_effective_ids', 'open', 'putenv', 'fsync', 'times',
#                       'truncate', 'abc', 'st', 'abort', 'devnull', 'set_inheritable', 'pathsep', 
#                       '_check_methods', '__doc__', 'closerange', 'PathLike', 'listmounts', 
#                       'supports_bytes_environ', 'supports_fd', 'symlink', '__package__',
#                         'close', 'getcwdb', 'sep', 'spawnv', 'O_RANDOM', 'system', 'unsetenv',
#                           'name', 'fsencode', 'P_OVERLAY', 'umask', '__all__', 'listvolumes', 
#                           'get_terminal_size', 'fdopen', 'error', 'popen', 'execlp', 'getppid',
#                             'altsep', 'linesep', 'stat_result', '__loader__', 'O_APPEND', 'strerror', 
#                             'isatty', 'getcwd', '_AddedDllDirectory', 'lseek', 'environ', 
#                             '_execvpe', '_walk_symlinks_as_files', 'getenv', 'O_RDWR', 'P_NOWAITO',
#                               'renames', 'pardir', 'O_TEMPORARY', 'makedirs', 'listdrives']


def dir(directory):

    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

    if not os.path.exists("images"):

        os.makedirs("images")

    # os.makedirs("images",image_extensions)

    image=[file for file in os.listdir(directory) if file.lower().endswith(image_extensions)]
    
    for img in image:
        file_extension=img.split(".")[-1]
        ext_flder=os.path.join("images",file_extension)

        if not os.path.exists(ext_flder):
            os.makedirs(ext_flder)
        
        src_path=os.path.join(directory,img)
        dst_path=os.path.join(ext_flder,img)

        shutil.move(src_path,dst_path)
        print(f"Moved {image} to {ext_flder}")


dirr=input("enter the directory name:").strip()
dir(dirr)