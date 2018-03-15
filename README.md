# rpmbuild-chain

This program builds a series of SRPMs with rpmbuild.

Each resulting RPM is added to a local YUM repository, making them
available as build dependencies for subsequent SRPMs. This is similar
in operation to mockchain, except the RPMs are built in the local system
instead of a dedicated build chroot. This is useful for building a small
series of RPMs that will be installed onto the same system, e.g. during
container builds.

Optionally, any RPMs installed or removed to satisify build dependencies
can be rolled back after the build has finished, provided they are still
available in the configured YUM repositories.

Warning: Installed packages and changes to the system may unknowingly
affect the produced RPMs between builds. In almost every case,
mock/mockchain is the recommended way to build RPMs using consistent
reproducible clean buildroots, especially if they are to be redistributed
to other systems. When satisifying build-dependencies, some packages
may be temporarily uninstalled, so its not recommended to run this on
live production hosts.

This program must be run as "root" in order to install any missing build
dependencies. All other commands (e.g. rpmbuild) are executed under the
specified non-root user to improve security.


## Usage

    usage: __main__.py [-h] [--srpms SRPMS [SRPMS ...]] --user USER
                       [--repo-path REPO_PATH] [--repo-name REPO_NAME]
                       [--build-path BUILD_PATH] [--no-rollback-builddep]
                       [--keep-repo-config] [--allow-scriptlets]
                       [--hookdir HOOKDIR [HOOKDIR ...]] [--lint] [--verbose]
                       [--version]
    
    optional arguments:
      -h, --help            show this help message and exit
      --srpms SRPMS [SRPMS ...]
                            Input SRPM files to build. Use "-" to read list from
                            STDIN (default: None)
      --user USER           Non-privileged user to run rpmbuild (default: None)
      --repo-path REPO_PATH
                            Destination directory to store the built RPMs
                            (default: rpmbuild-chain)
      --repo-name REPO_NAME
                            Name for the YUM repository configuration (default:
                            rpmbuild-chain)
      --build-path BUILD_PATH
                            Directory to build the RPMs in. Use tmpfs for faster
                            builds. Default: tmpdir (default: None)
      --no-rollback-builddep
                            Do not automatically rollback installed RPM
                            BuildRequires (default: False)
      --keep-repo-config    Keep YUM repository configured after exiting (default:
                            False)
      --allow-scriptlets    Do not abort if RPM scriptlets are found. Warning:
                            scriptlets will be run as root when package is
                            installed (default: False)
      --hookdir HOOKDIR [HOOKDIR ...]
                            Hook script directory(s). Valid subdirectories:
                            pre_run pre_build post_build post_run (default: None)
      --lint                Run rpmlint on every package (default: False)
      --verbose
      --version             show program's version number and exit


## Contributions

Patches for fixes are welcome.

- Run "make integ" before opning a pull request. You will be prompted to run sudo to execute the test


## Author

Copyright (C) 2018 Joseph Mullally

License: [MIT](./LICENCE)

Project: https://github.com/jwmullally/rpmbuild-chain
