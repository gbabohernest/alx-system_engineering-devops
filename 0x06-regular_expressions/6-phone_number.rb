#!/usr/bin/env ruby
# This script create a regex for matching 10 digit phone number

puts ARGV[0].scan(/^\d{10}$/).join
