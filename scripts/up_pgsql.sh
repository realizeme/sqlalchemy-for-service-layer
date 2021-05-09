#!/bin/bash

function up() {
    docker run --rm -p 5400:5432 --name postgres-test -e POSTGRES_PASSWORD=1q2w3e4r -d -v pgdata:${pwd}/postgresql postgres
}

up
