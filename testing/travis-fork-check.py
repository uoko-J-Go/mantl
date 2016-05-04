#!/usr/bin/env python
from __future__ import print_function
import logging
import os
import shlex
import subprocess

def check_travis_repo_slug():
    logging.info("Decrypting OS ssh key")
    cmd = "openssl aes-256-cbc -K {key} -iv {iv} -in ci.enc -out testing/ci -d".format(
            key=os.environ['encrypted_6a9d32f3e0bd_key'],
            iv=os.environ['encrypted_6a9d32f3e0bd_iv'])
    returncode = subprocess.call(shlex.split(cmd))
    if returncode != 0:
        logging.critical("Description failed. This is likely due to commit coming from fork")
        os.environ['MANTL_CI_FORK_CHECK'] = "1"
    else:
        logging.info("Decryption successful")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    check_travis_repo_slug()
