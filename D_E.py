#!/usr/bin/env python3
#Write each line of host.max to host.max.new 
#untill line ## BEGIN DD SECTION
#Then write contents of sitelist.txt to host.max.new


fo_host_og = open('host.max', 'r')
fo_host_new = open('host.max.new', 'w')
 
site_line_fo = open('site_list.txt', 'r')
site_line_list = site_line_fo.readlines()
DEBUG = True
if DEBUG:
  print('site_line_list: %s' % site_line_list)

for host_line in fo_host_og.readlines():
  if DEBUG:
    print('\n\n--------------------------\nTop of host_line for loop')
    print('host_line: "%s"' % host_line) 
  fo_host_new.write(host_line)
  if DEBUG:
    print('about to do ## BEGIN DD if')
  if host_line.strip() == '## BEGIN DD SECTION':
    if DEBUG:
      print('break works')
    break
 