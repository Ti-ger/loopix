#!/usr/bin/bash
# Deploy
python setup_mixnode.py 9999 $HOST $HOST $GROUP
# Wait for the controller to create the db
until [ -f /volumes/global/Controller_done ]
do 
	sleep 1
done
cp /volumes/global/example.db example.db
# Run
twistd -y run_mixnode.py
PID=$(cat twistd.pid)
echo "Run on $HOST with PID: $PID"
tail -F /dev/null
