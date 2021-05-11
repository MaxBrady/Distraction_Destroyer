#!/usr/bin/env python3
# You wish to add the lines in site_list.txt to host.max, if they are not already there.
# We are going to use a "## BEGIN DD SECTION" and an "## END DD SECTION" section markers
# to accomplish this.
#
# Procedure:
# Open host.max for reading
# Open host.max.new for writing
# For every line in host.max:
#   Decide whether or not to write it to host.max.new
#   You can also add lines like the contents of site_list.txt to host.max.new
# Close host.max and host.max.new, then:
#   rename host.max to host.max_old
#   rename host.max.new to host.max
# You are done

DEBUG=True

# FIXME(Max): This script fails if anything is 
# added to the end after the DD section.

fo_host_og = open('host.max', 'r')
fo_host_new = open('host.max.new', 'w')
 
site_line_fo = open('site_list.txt', 'r')
site_line_list = site_line_fo.readlines()

# if DEBUG:


#   print('site_line_list: %s' % site_line_list)

# for host_line in fo_host_og.readlines():
#   if DEBUG:
#     print('\n\n--------------------------\nTop of host_line for loop')
#     print('host_line: %s' % host_line) 
#     fo_host_new.write(host_line)

#   for site_line in site_line_list:
#     if DEBUG:
#       print('\n\nTop of site_line for loop')
#     if host_line == site_line:
#       if DEBUG:
#         print('Writing site line to fo_host_new')
#       fo_host_new.write('site_line')
#     else:
#       if DEBUG:
#         print('Writing host_line fo_host_new')
# if DEBUG:
#   print('End of script')