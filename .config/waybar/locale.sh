#!/bin/bash
echo "Current Locale: $(locale | grep 'LANG' | cut -d= -f2)"

