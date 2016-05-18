#!/usr/bin/env python
#
# RatToolsDev
#
# The development versions of rattools 
#
# Author P G Jones - 15/10/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import rattools

class RatToolsDev(rattools.RatToolsDevelopment):
    def __init__(self, system):
        """ Initialise dev version."""
        super(RatToolsDev, self).__init__("rattools-dev", system, "root-5.34.21")

class RatTools601(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools601, self).__init__("rattools-6.0.1", system, "root-5.34.34", "rat-6.0.1", "6.0.1")

class RatTools600Alpha(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools600, self).__init__("rattools-6.0.0", system, "root-5.34.34", "rat-6.0.0", "RAT-6.0.0-alpha")

class RatTools531(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools531, self).__init__("rattools-5.3.1", system, "root-5.34.30", "rat-5.3.0", "5.3.1")

class RatTools530(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools530, self).__init__("rattools-5.3.0", system, "root-5.34.30", "rat-5.3.0", "5.3.0")

class RatTools521(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools521, self).__init__("rattools-5.2.1", system, "root-5.34.30", "rat-5.2.1", "5.2.1")

class RatTools52(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools52, self).__init__("rattools-5.2.0", system, "root-5.34.30", "rat-5.2.0", "5.2.0")

class RatTools46(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools46, self).__init__("rattools-4.6.0", system, "root-5.34.18", "rat-4.6.0", "4.6.0")

class RatTools45(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools45, self).__init__("rattools-4.5.0", system, "root-5.34.11", "rat-4.5.0", "4.5.0")

class RatTools44(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools44, self).__init__("rattools-4.4.0", system, "root-5.34.08", "rat-4.4.0", "4.4.0")

class RatTools43Builder423(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools43Builder423, self).__init__("rattools-4.3.0-builder-4.2.3", system, "root-5.34.08", 
                                                   "rat-4.3.0", "release-4.3.0-builder4.2.3")

class RatTools43(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools43, self).__init__("rattools-4.3.0", system, "root-5.34.08", "rat-4.3.0",
                                         "release-4.3.0")

class RatTools42(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools42, self).__init__("rattools-4.2", system, "root-5.34.02", "rat-4.2",
                                        "release-4.20")

class RatTools41(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools41, self).__init__("rattools-4.1", system, "root-5.34.02", "rat-4.1",
                                        "release-4.10")
class RatTools4(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools4, self).__init__("rattools-4", system, "root-5.32.04", "rat-4",
                                        "release-4.00")

class RatTools1(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools1, self).__init__("rattools-1", system, "root-5.32.04", "rat-4",
                                        "ebd71f14121dee64f6d0f01b72730b29b075e6d6")
