#!/bin/bash

clear 

DEBUG=""
BASE_URL="http://localhost:8000"

execute_test()
{
    METHOD=$1
    URL=$2
    HEADER=$3
    PAYLOAD=$4

    if [ "$DEBUG" == "1" ]
    then
        echo -e "\n##########################################"
        echo -e "\n${HEADER}"
        echo "METHOD=$METHOD"
        echo "URL=$URL"
        echo "HEADER=$HEADER"
        echo "PAYLOAD=$PAYLOAD"
        echo -e "\n##########################################"
    fi

    echo -e "\n${HEADER}"

    if [ "$METHOD" == "GET" ]
    then
        curl -v ${METHOD} ${URL}
    else
        curl -v ${METHOD} -H "Content-Type: application/json" -d "${PAYLOAD}" ${URL}
    fi
    echo -e "\n-----------------------------------------------------------------"
}

# execute_test GET ${BASE_URL}

# # execute request - trailing slash
# execute_test POST ${BASE_URL}/execute/ "Execute request - trailing slash" '{ "id": "'"$(dbus-uuidgen)"'", "algorithm": "tov_solver" }'

# # execute request - non trailing slash
# execute_test POST ${BASE_URL}/execute "Execute request - non trailing slash" '{ "id": "'"$(dbus-uuidgen)"'", "algorithm": "tov_solver" }'

# execute request - non trailing slash
execute_test POST ${BASE_URL}/execute "Execute request - TOV" '{ "id": "'"$(dbus-uuidgen)"'", "algorithm": "tov_solver" }'
