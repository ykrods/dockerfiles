# ダウンロードが毎回行われる??ので RUN する意味がない??
# ので一旦つかわない

FROM gradle:7.2.0-jdk8

RUN mkdir /project

WORKDIR /project

RUN gradle init --type kotlin-application \
    --dsl groovy \
    --project-name scratch \
    --package com.example && \
   /project/gradlew build

CMD ["/project/gradlew", "run"]
