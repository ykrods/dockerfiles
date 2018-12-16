How to use
===========

- .env に次を追加 `APP_VOLUME_PATH=/path/to/app`
- 以下の感じで

  ::

     # login
     $ docker-compose run --rm --service-ports firebase login

     # shell to init project
     $ docker-compose run --rm --entrypoint=/bin/bash firebase

     # serve
     $ docker-compose run --rm firebase

     # deploy
     $ docker-compose run --rm firebase deploy

備考
====

- node_modules は単純にマウント元に作成される(コード読みたい時あるし
