# A simple setup script to create an executable using PyQt4. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# PyQt4app.py is a very simple type of PyQt4 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import os
from cx_Freeze import setup, Executable

application_title = "Devex"  # what you want to application to be called
main_python_file = "main.py"  # the name of the python file you use to run the program
exec_2 = "db_import_json.py"
exec_3 = "get_txm_sess_table.py"

base = None
# if sys.platform == "win32":
#     base = "Win32GUI"

includes = ["atexit", "re", "numpy.core._methods", "numpy.lib.format"]
include_files = ['Devex.xlsm', 'README.txt', 'db_import_make_json.py', 'db_Import_python.py',
                 'get_sess_table_phx_quick.py', 'Alias_sets/', 'Archive/', 'Data/', 'Excel/',
                 'libs/', 'Plotting_routines/', 'Scratch/', 'Special_Processing/', 'UI/']
packages = ["pkg_resources._vendor", "sqlalchemy.dialects.mssql"]

shortcut_table = [
    ("ProgramMenuShortcut",  # Shortcut
     "ProgramMenuFolder",  # Directory_
     "Devex",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]main.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     'TARGETDIR'  # WkDir
     ),

    ("StartupShortcut",  # Shortcut
     "StartupFolder",  # Directory_
     "Devex",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]main.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     'TARGETDIR'  # WkDir
     ),
    ]

msi_data = {"Shortcut": shortcut_table}

setup(
        name=application_title,
        version="0.1",
        author="Vedant Sharma",
        description="Devex Package",
        options={"build_exe": {"includes": includes, "include_files": include_files, "packages": packages},
                 "bdist_msi": {"upgrade_code": '{56520F3A-DC3A-11E2-B341-002219E9B01E}',
                               "data": msi_data,
                               "initial_target_dir": os.environ['PUBLIC'] + "\AppData\Local\Qorvo\Devex"}},
        executables=[Executable(main_python_file, base=base),
                     Executable(exec_2, base=base),
                     Executable(exec_3, base=base)]
)
