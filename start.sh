#开启服务
WORK_PATH="${PWD}"
export PYTHONPATH=${WORK_PATH}:${PYTHONPATH}

python ./dueros/samples/Server.py
