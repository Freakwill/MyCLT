#!/bin/sh

:<<EOF
update the packages of python

s: sudo, u: not sudo -- udo, l: show list again, m: install last module
h: help
EOF

list=`pip list --format columns --outdate`  # execute pip, and get the output
echo "$list"

last_module=""
mode=u

echo "Input q to quit, input h for help."

while true
do
	read -p "please input module name: " module
    if [ $module == m -o -z $module ]
        # upgrade the last module again
    then
        if [ -n $last_module ]
        then
            echo "Upgrade ${last_module[@]} again."
            pip install --upgrade ${last_module[@]} -i https://pypi.tuna.tsinghua.edu.cn/simple
        else
            echo "Please input a valid string."
        fi
	elif [ $module == q ]   # to quit
	then
	    echo "Finished. Have a good time ^_^"
		break
	elif [ $module == s ]
    then
        echo "sudo mode on"
        mode=s
    elif [ $module == u ]
    then
        echo "sudo mode off"
        mode=u
    elif [ $module == l ]
    then
        echo "$list"
    elif [ $module == h ]
    then
        echo "s: sudo, u: not sudo -- udo, l: show list again, m: install last module, h: help"
    else
        last_module=$module
        echo "Start to upgrade $last_module."
        if [ $mode == u ]
        then
            pip install --upgrade ${module[@]} -i https://pypi.tuna.tsinghua.edu.cn/simple
        else
            sudo pip install --upgrade ${module[@]} -i https://pypi.tuna.tsinghua.edu.cn/simple
        fi
	fi
done
