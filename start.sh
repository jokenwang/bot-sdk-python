#开启服务
WORK_PATH="${PWD}"
export PYTHONPATH=${WORK_PATH}:${PYTHONPATH}

python ./dueros/bot/sdk/samples/Server.py
