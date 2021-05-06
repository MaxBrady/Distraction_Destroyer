#!/usr/bin/env python3

fo_host = 'host.max'
blocker = 'somesite'
fo_host = open(fo_host, 'a')
if fo_host != blocker:
  fo_host.write('\n' + blocker)
else: fo_host.close()



 #Things I tried in the last week most likely will scrap
# blocker = """127.0.0.1 youtube.com 
# 127.0.0.1 www.youtube.com 
# 127.0.0.1 amazon.com
# 127.0.0.1 www.amazon.com"""
# #file object 
# fo_host = 'host.max'

# contents_blocker = open(blocker, 'r') 
# fo_host_contents = open(fo_host, 'r')

# if fo_host_contents != contents_blocker:
#   fo_host = open(fo_host, 'a')
#   fo_host.write('\n' + blocker)
# else:
#     fo_host.close()
#append the value of blocker to fo_hosts object
# If blocker contents don't match fo_host contents write blocker contents in fo_host file.
# fo_host = open(fo_host, 'a')
# if fo_host != blocker:
#   fo_host.write('\n' + blocker)
# else: 
#     fo_host.close()

#


#From a couple of weeks ago, most likely closer to the correct way.

# n_from = 'host.max'

# fn_to = 'host.max'

# fo_from = open(fn_from, 'r')
# fo_to = open(fn_to, 'w')

# contents_original = fo_from.read()
# contents_new = contents_original + '127.0.0.1 youtube.com'+ '\n' + '127.0.0.1 www.youtube.com'
# print(contents_new)
# fo_to.write(contents_new)