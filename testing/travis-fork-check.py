#!/usr/bin/env python
from __future__ import print_function
import os
import subprocess
import sys

def check_travis_repo_slug():
    if 'encrypted_6a9d32f3e0bd_key' not in os.environ:
        sys.stderr.write("Decryption disabled. Setting MANTL_CI_FORK_CHECK to 1")
        print("1")
    else:
        sys.stderr.write("Decrypting OS ssh key")
        cmd = ["openssl",
                "aes-256-cbc",
                "-K", os.environ['encrypted_6a9d32f3e0bd_key'],
                "-iv", os.environ['encrypted_6a9d32f3e0bd_iv'],
                "-in", "ci.enc",
                "-out", "testing/ci",
                ]
        returncode = subprocess.call(cmd)
        if returncode != 0:
            sys.exit("Decryption failed!")
        else:
            sys.stderr.write("Decryption successful")

if __name__ == "__main__":
    check_travis_repo_slug()
