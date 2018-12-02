How to use
===========

- プロジェクトは適宜 `/code` にマウントする
- node_modules は単純にマウント元に作成される(コード読みたい時あるし

::

  $ docker-compose run --rm --service-ports firebase login
  $ docker-compose run --rm --entrypoint=/bin/bash firebase
  $ docker-compose run --rm firebase deploy
