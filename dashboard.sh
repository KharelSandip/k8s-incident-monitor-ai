#!/bin/bash

tmux new -d -s mysession

tmux send-keys -t 0.0 

tmux split-window -h -t mysession 

tmux send-keys -t 0.1 "kubectl port-forward --address 0.0.0.0 service/incident-monitor-service 8080:80" Enter

tmux split-window -v -t mysession 

tmux send-keys -t 0.2 "python3 monitor/pod_monitor.py && python3 monitor/health_check.py" Enter

sleep 0.5

tmux attach -t mysession