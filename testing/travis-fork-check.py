#!/usr/bin/env python
from __future__ import print_function
import logging
import os
import shlex
import subprocess
import sys

def check_travis_repo_slug():
    if not os.environ['TRAVIS_REPO_SLUG'].startswith('CiscoCloud/'):
        logging.warning("Currently, we can't unlock deploy keys for forks of Mantl, so we are skipping the build")
        sys.exit(0)
    else:
        logging.info("Decrypting OS ssh key")
        cmd = "openssl aes-256-cbc -K {key} -iv {iv} -in ci.enc -out testing/ci -d".format(
                key=os.environ['encrypted_6a9d32f3e0bd_key'],
                iv=os.environ['encrypted_6a9d32f3e0bd_iv'])
        sys.exit(subprocess.call(shelx.split(cmd)))
