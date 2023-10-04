#!/usr/bin/env ruby
# This script parses a log file and output info about:
#   [SENDER], [RECIEVER], [FLAGS]

input_string = ARGV[0]
pattern = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
matches = input_string.scan(pattern)
output = matches.join(",")
puts output
