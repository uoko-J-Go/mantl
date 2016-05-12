Certificates
============

.. versionadded:: 1.1

This role generates extra TLS certificates for each node. Currently used as part
of the :docs:`Docker Swarm` addon.

Caution: This will distribute your CA private key to all nodes. This shouldn't
be a real security risk if you're using self-signed certificates.  If you use a
real CA, you'll want to generate certificates and distribute them manually
instead.

Variables
---------

.. data:: cert_options

   Options passed through to the generate-certificate program.
