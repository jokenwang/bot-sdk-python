cd $(dirname $0)
dir=$(pwd)
curl -H "Content-Type: application/json" -XPOST -d@$dir/$1 http://127.0.0.1:8080
