Docker Swarm
============

.. versionadded:: 1.1

Set up Docker Swarm on a Mesos cluster. Swarm runs independently of Mesos &
Kubernetes, and manages its own scheduling. Run this playbook after running
the core playbook (sample.yml).

Variables
---------

You can use these variables to customize your Sarm installation. It's highly
recommended to set :data:`SUBNET`.

.. data:: dummy_var

   Lipsum orem
