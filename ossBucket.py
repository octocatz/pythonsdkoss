# -*- coding: utf-8 -*-
import oss2
import datetime
from itertools import islice
auth = oss2.Auth ('xxx', 'xxx')
bucket = oss2.Bucket (auth, 'oss-ap-northeast-1.aliyuncs.com', 'xxx')

#TargetFileName
c_file = 'xxx.png'
exist = bucket.object_exists(c_file)
if exist:
    f_meta = bucket.get_object_meta(c_file)
    u_time = f_meta.last_modified
    t = datetime.datetime.fromtimestamp(u_time)
    print (t)
else:
    print ('object not exist')



