#!/usr/bin/env python
#
# SnoplusPackage
#
# Base class for packages that can be installed by snoing.
#
# Author M Mottram - 2014/07/02 <m.mottram@qmul.ac.uk>: First revision
####################################################################################################
import localpackage
import os

class SnoplusPackage(localpackage.LocalPackage):
    """ Class for packages that are SNO+ software """

    def __init__(self, name, system):
        """ Initialise the package."""
        super(SnoplusPackage, self).__init__(name, system)
        # Just override the install path of localpackage
        self._install_path = os.path.join(self._system.get_rat_install_path(), self._name)
        return
