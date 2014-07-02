#!/usr/bin/env python
#
# snoing
#
# Entry script decides what to do
#
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import sys
try:
    import packagemanager
except ImportError:
    print "Error: Source the snoing environment file."
    sys.exit(1)
import optparse
import textlogger
import installmode
import snoing_exceptions
import system
import os
import pickle

def print_error_message():
    """Print a standard error message if snoing fails."""
    print "Snoing has failed, please consult the above error messages or the snoing.log file."
    print "More help available in the snoplus companion."
    sys.exit(1)

if __name__ == "__main__":
    default_file_path = os.path.join(os.path.dirname(__file__), "settings.pkl")
    if os.path.isfile(default_file_path):
        default_file = open(default_file_path, "r")
        defaults = pickle.load(default_file)
        default_file.close()
        try:
            a = defaults["rat_install_path"]
        except KeyError, e:
            try:
                a = defaults['cache_path']
                defaults = {"cache_path" : defaults['cache_path'], "rat_install_path" : defaults['install_path'],
                            "dependency_install_path" : defaults["install_path"]}
            except KeyError, e:
                defaults = {"cache_path" : defaults['cache'], "rat_install_path" : defaults['install'],
                            "dependency_install_path" : defaults["install"]}
    else: # No defaults to load, thus create
        defaults = {"cache_path" : "cache", "rat_install_path" : "install",
                    "dependency_install_path" : "install"}
    # First build the options and parse the calling command
    parser = optparse.OptionParser(usage = "usage: %prog [options] [package]", version="%prog 2.0")
    parser.add_option("-c", type="string", dest="cache_path", help="Cache path.", 
                      default=defaults["cache_path"])
    parser.add_option("-i", type="string", dest="rat_install_path", help="Install path.", 
                      default=defaults["rat_install_path"])
    parser.add_option("-v", action="store_true", dest="verbose", help="Verbose Install?", 
                      default=False)
    parser.add_option("-a", action="store_true", dest="all", help="All packages?")
    parser.add_option("-k", action="store_true", dest="clean", help="Clean temporary files.")
    parser.add_option("--Ac", type="string", dest="curl_arguments", help=optparse.SUPPRESS_HELP)
    parser.add_option("--Ar", type="string", dest="root_arguments", help=optparse.SUPPRESS_HELP)
    parser.add_option("--Ag", type="string", dest="geant4_arguments", help=optparse.SUPPRESS_HELP)

    installerGroup = optparse.OptionGroup(parser, "Optional Install modes", 
                                          ("Default snoing action is to install non graphically, i.e."
                                           " no viewer. This can be changed with the -g option."))
    installerGroup.add_option("-g", action="store_true", dest="graphical", help="Graphical install?", 
                              default=False)
    installerGroup.add_option("-x", action="store_true", dest="grid", help="Grid install (NO X11)?", 
                              default=False)
    parser.add_option_group(installerGroup)

    actionGroup = optparse.OptionGroup(parser, "Optional Actions", 
                                       ("Default snoing action is to install the specified package,"
                                        " which defaults to rat-dev."))
    actionGroup.add_option("-q", action="store_true", dest="query", help="Query Package Status?")
    actionGroup.add_option("-r", action="store_true", dest="remove", help="Remove the package?")
    actionGroup.add_option("-R", action="store_true", dest="force_remove", help=optparse.SUPPRESS_HELP, 
                           default=False)
    actionGroup.add_option("-d", action="store_true", dest="dependency", help="Install dependencies only?")
    actionGroup.add_option("-D", dest="dependency_install_path", help="Install dependencies to alternative location?",
                           default=defaults["dependency_install_path"])
    actionGroup.add_option("-p", action="store_true", dest="progress", help="Progress/update the package?")
    parser.add_option_group(actionGroup)

    githubGroup = optparse.OptionGroup(parser, "Github authentication Options", 
                                       "Supply a username or a github token, not both.")
    githubGroup.add_option("-u", type="string", dest="username", help="Github username")
    githubGroup.add_option("-t", type="string", dest="token", help="Github token")
    parser.add_option_group(githubGroup)
    (options, args) = parser.parse_args()
    # Dump the new defaults
    defaults["cache_path"] = options.cache_path
    defaults["rat_install_path"] = options.rat_install_path
    defaults["dependency_install_path"] = options.rat_install_path
    dependency_install_path = options.rat_install_path
    if options.dependency_install_path:
        # Install dependencies to an alternative location
        defaults['dependency_install_path'] = options.dependency_install_path
        dependency_install_path = options.dependency_install_path
    default_file = open(default_file_path, "w")
    pickle.dump(defaults, default_file)
    default_file.close()

    # Now create the logger, direct logging to snoing.log file
    logger = textlogger.TextLogger(os.path.join(os.path.dirname(__file__), "snoing.log"), options.verbose)
    # Now create the system
    if options.grid and options.graphical:
        print_error_message()
    elif options.grid:
        install_mode = installmode.Grid
    elif options.graphical:
        logger.error("The graphical mode `-g` is obsolete, please reinstall your software without it.")
        install_mode = installmode.Graphical
    else:
        install_mode = installmode.Normal
    # Sort out the extra arguments
    opt_args = {"root":[],"geant4":[],"curl":[]}
    if options.root_arguments is not None:
        opt_args["root"] = options.root_arguments.split()
    if options.geant4_arguments is not None:
        opt_args["geant4"] = options.geant4_arguments.split()
    if options.curl_arguments is not None:
        opt_args["curl"] = options.curl_arguments.split()
    try:
        install_system = system.System(logger, options.cache_path, options.rat_install_path, dependency_install_path, install_mode, opt_args)
    except snoing_exceptions.InstallModeException, e:
        print e.args[0], "The existing installation is ", installmode.Text[e.SystemMode], ". You've requested the installation to be ", installmode.Text[e.CommandMode]
        print "You can install to a new path using the -i option or delete the existing installation and start again."
        print_error_message()
    except snoing_exceptions.SystemException, e:
        print e.args[0], ":", e.Details
        print_error_message()
    if options.clean:
        install_system.clean_cache()
    # Now create the package manage and populate it
    package_manager = packagemanager.PackageManager(install_system, logger)
    package_manager.register_packages(os.path.join(os.path.dirname(__file__), "versions"))
    package_manager.authenticate(options.username, options.token)
    # Default action is to assume installing, check for other actions
    try:
        if options.all: # Wish to act on all packages
            if options.query: # Nothing todo, done automatically
                pass
            elif options.remove: # Wish to remove all packages
                shutil.rmtree(install_system.get_install_path())
                try:
                    shutil.rmtree(install_system.get_rat_install_path())
                except OSError:
                    pass # Path not there
            elif options.dependency: # Doesn't make sense
                Log.warn("Input options don't make sense.")
                PrintErrorMessage()
            elif options.progress: # Update all installed
                package_manager.update_all()
            else: # Wish to install all
                package_manager.install_all()
        else: # Only act on one package
            if options.grid == False: # Default local package
                package_name = "rat-dev"
            else: # Default grid package
                package_name = "rat-4.5.0"
            if len(args) != 0:
                package_name = args[0]
            if options.query: # Wish to query the package
                logger.set_state("Checking package %s install status" % package_name)
                if package_manager.check_installed(package_name):
                    logger.package_installed(package_name)
                else:
                    logger.error(package_name + " is not installed")
            elif options.remove or options.force_remove: # Wish to remove the package
                package_manager.remove_package( package_name, options.force_remove )
            elif options.dependency: # Wish to install only the dependencies
                package_manager.install_dependencies( package_name )
            elif options.progress: # Wish to update the package
                package_manager.update_package( package_name )
            else: # Wish to install the package
                package_manager.install_package( package_name )
    except snoing_exceptions.PackageException, e:
        print e.Package, ":", e
        print_error_message()
