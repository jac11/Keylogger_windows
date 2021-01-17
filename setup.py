from distutils.core import setup
import py2exe

setup(
    zipfile = None,
    options = {"py2exe": {"compressed": 2,
                          "optimize": 2,
                          "bundle_files": 1,
                          "dist_dir": "dist",
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                         }
              },
    windows=['win_logger.py']
    )
