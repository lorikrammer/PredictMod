#!/bin/bash

source ./env.sh

if [[ ! $BUILD_ENV ]]; then
    echo No build environment found - Aborting.
    exit 0
fi

case $BUILD_ENV in
    'shell_testing'|'development')
    echo Build environment found $BUILD_ENV. Launch middleware manually.
    ;;
    'production'|'beta')
    docker run -d --restart=always --network predictmod  --name middleware predictmod:v0.3.1-middleware
    ;;
    'docker-dev')
    docker run -d --restart=always -p 8000:8000 --name middleware predictmod:v0.3.1-middleware
    ;;
    *)
    echo Please update your "env.sh" file appropriately.
    ;;
esac
