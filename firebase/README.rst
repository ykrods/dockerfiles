How to use
===========

- XXX: プロジェクトのディレクトリは適宜マウントする

::

  $ docker-compose run --rm --user=root firebase /bin/bash -c "chown firebase:firebase /home/firebase/.config"
  $ docker-compose run --rm --service-ports firebase /bin/bash -c "firebase login"
  $ docker-compose run --rm firebase

Note
=====

- XXX: .config のパーミッション変えるのはもうちょっとやり方がありそう
