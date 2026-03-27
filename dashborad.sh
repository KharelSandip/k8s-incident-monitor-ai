#!/bin/bash

tmux new -d -s mysession

tmux send-keys -t 0.0 "echo hello word 0 "

tmux split-window -h -t mysession 

tmux send-keys -t 0.1 "echo hello world 1 "

tmux split-window -v -t mysession 

tmux send-keys -t 0.2 "echo hellow world 2"

tmux attach -t mysession