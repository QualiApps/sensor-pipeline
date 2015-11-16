#!/bin/bash

NIFI_HOME=${NIFI_HOME:-"/opt/nifi"}

REVISION=0
NIFI_API_PATH="http://127.0.0.1:8080/nifi-api"
GROUP_ID=""

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
sleep 40

# Create a proccess group
# 1 - group name
# 2 - template id
# 3 - running (True | False)
# 4 - coord array (x y)
function create_group {
    COORD=($4)
    get_version

    RESPONSE_PG=$(curl -X POST "${NIFI_API_PATH}/controller/process-groups/root/process-group-references" -H "Content-Type:application/x-www-form-urlencoded" -d "x=${COORD[0]}&y=${COORD[1]}&version=${REVISION}&name=${1}")

    get_group_id ${RESPONSE_PG}

    if [ "${GROUP_ID}" != "" ]; then
	# Instantiates a template
	get_version
	curl -X POST "${NIFI_API_PATH}/controller/process-groups/${GROUP_ID}/template-instance" -H "Content-Type:application/x-www-form-urlencoded" -d "originX=50.0&originY=50.0&version=${REVISION}&templateId=${2}"
    
	# Start all processors
	if [ ${3} == true ]; then
    	    get_version
    	    curl -X PUT "${NIFI_API_PATH}/controller/process-groups/${GROUP_ID}" -H "Content-Type:application/x-www-form-urlencoded" -d "running=true&version=${REVISION}"
	fi
    
    fi
}

# Create the Sensor group (Main pipeline)
coord=(100.0 100.0)
create_group "Sensor" "1d4dfd36-c513-434e-bce4-13245559a514" false "${coord[*]}"
# Create the Listener group (wait handlers)
coord=(500.0 100.0)
create_group "Listener" "4166652a-735a-43aa-a8bf-20cba9eea397" true "${coord[*]}"

tail -F ${NIFI_HOME}/logs/nifi-app.log
