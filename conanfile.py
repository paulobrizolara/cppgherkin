#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile
import os

class MyConanFile(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    #Conan dependencies
    requires = (
        "pcre2plus/0.0.4-beta@paulobrizolara/experimental",

        "WafGenerator/0.0.1@paulobrizolara/experimental"
    )

    generators = "Waf"

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin") # From bin to bin
        self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin

    def build(self):
        waf = os.path.join(".", 'waf')
        opts = self.get_options()

        self.run('%s configure build %s' % (waf, opts), cwd = self.conanfile_directory)

    def get_options(self):
        opts = []

        if self.settings.build_type == "Debug":
            opts.append("--debug")
        else:
            opts.append("--release")

        return " ".join(opts)