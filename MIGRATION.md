# DB Migration

## 설치

### 패키지 설치

- alembic

```bash
$ pipenv install alembic --dev
```

- Postgres 관련 설치

```
$ pipenv install psycopg2-binary
```

- python-dotenv

```
$ pipenv install python-dotenv
```

## 초기화
```
# alembic init <migration folder name>
$ pipenv run alembic init migrations
```

- 초기화 확인
```
$ tree .
.
├── alembic.ini
├── migrations
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
```



## 설정

### Database 생성

```
$ docker exec -it postgres-test /bin/bash
root@ac61c662ee4c:/# psql -U postgres
psql (13.0 (Debian 13.0-1.pgdg100+1))
Type "help" for help.

postgres=# CREATE DATABASE dataops;
```

## 마이그레이션 방법

### 템플릿 생성

```bash
$ pipenv run alembic revision --auto -m "<Comment>"
```

### 마이그레이션
To apply latest schema version, use `upgrade` command.

```bash
$ pipenv run alembic upgrade head
```

## Reference
- [sqlalchemy](https://www.michaelcho.me/article/sqlalchemy-commit-flush-expire-refresh-merge-whats-the-difference)
