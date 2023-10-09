#computer_science #bash #practice 
```bash
#!/bin/bash
# scriptbc -- обертка для 'bc’, возвращающая результат вычислений
if ["$1" = "-p" ] ; then
	precision=$2
	shift 2
else
	precision=2 # По умолчанию
fi

bc -q -l << EOF
		scale=$precision
		$*
	quit
EOF
exit 0
```
