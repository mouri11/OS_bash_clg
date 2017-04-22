#!/bin/bash
read -p "Enter a number:" a
seq -s "*" 1 $a | bc
