#coding=utf-8
import os
path_root = os.path.dirname(__file__)
path_config = os.path.join(path_root, "commonTools/configs.conf").replace("\\", "/")
log_dir = os.path.join(path_root, "logs/").replace("\\", "/")
report_dir = os.path.join(path_root, "report/").replace("\\", "/")
execl_dir = os.path.join(path_root, "execldata/").replace("\\", "/")
case_path = os.path.join(path_root,"testcase/").replace("\\","/")