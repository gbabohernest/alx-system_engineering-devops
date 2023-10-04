#!/usr/bin/env ruby
# This script parses a log file and output info about:
#   [SENDER], [RECIEVER], [FLAGS]

Format = ARGV[0].scan(/from:(.\w+)|to:(.\w+)|flags:([0-9:-]+)/)

sender = Format[0].compact[0]
receiver = Format[1].compact[0]
flags = Format[2].compact[0]

List - [sender, receiver, flags].compact
puts List.join(',')
