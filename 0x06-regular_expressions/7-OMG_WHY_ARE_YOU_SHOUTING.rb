#!/usr/bin/env ruby
# This script create a regex for matching only capital letters

puts ARGV[0].scan(/[A-Z]/).join
