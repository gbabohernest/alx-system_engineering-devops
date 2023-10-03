#!/usr/bin/env ruby
# This script create a regex for repetition

puts ARGV[0].scan(/hbt{2, 5}n/).join
