# Docker での環境構築

流れを以下に記載する

## 1. Python 環境の準備

- docker コンテナの build

    ```bash
    $ cd docker/ros2
    $ cp .env.example .env

    $ docker compose build
    ```

## 2. コンテナ起動

- docker コンテナを起動します

    ```bash
    $ docker compose up
    ```

- これにより、以下の URL から各種サービスにアクセスできるようになる

service|URL
--|:--
jupyter|localhost:{JUPYTER_PORT}
noVNC (Ubuntu)|http://localhost:6080/
