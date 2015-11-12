#!/bin/bash

NIFI_HOME=${NIFI_HOME:-"/opt/nifi"}

REVISION=0
NIFI_API_PATH="http://127.0.0.1:8080/nifi-api"
GROUP_NAME="Sensor"
GROUP_ID=""
TPL_ID="1d4dfd36-c513-434e-bce4-13245559a514"

# Retrieves last revision
function get_version {
    REVISION=$(curl -X GET "${NIFI_API_PATH}/controller/revision" | grep -Po '"version":.*?[^\\],' | awk -F':' '{print $2}' | awk -F',' '{print $1}')
}

# $1 - json response (group)
function get_group_id {
    GROUP_ID=$(echo ${1} | grep -Po '"id":.*?[^\\]"' | head -1 | awk -F':' '{print $2}' | awk -F'"' '{print $2}')
}

# Start the Nifi
${NIFI_HOME}/bin/nifi.sh start
# Waiting before the Nifi-api will be available
sleep 25

# Create a proccess group
get_version

RESPONSE_PG=$(curl -X POST "${NIFI_API_PATH}/controller/process-groups/root/process-group-references" -H "Content-Type:application/x-www-form-urlencoded" -d "x=100.0&y=100.0&version=${REVISION}&name=${GROUP_NAME}")

get_group_id ${RESPONSE_PG}

if [ "${GROUP_ID}" != "" ]; then
    # Instantiates a template (Sensor pipeline)
    get_version
    curl -X POST "${NIFI_API_PATH}/controller/process-groups/${GROUP_ID}/template-instance" -H "Content-Type:application/x-www-form-urlencoded" -d "originX=50.0&originY=50.0&version=${REVISION}&templateId=${TPL_ID}"
    
    # Start all processors
    get_version
    curl -X PUT "${NIFI_API_PATH}/controller/process-groups/${GROUP_ID}" -H "Content-Type:application/x-www-form-urlencoded" -d "running=true&version=${REVISION}"
    
    tail -F ${NIFI_HOME}/logs/nifi-app.log
fi

exit 0