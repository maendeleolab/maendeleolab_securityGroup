#!/usr/bin/python3

import os, sys, pprint, itertools
from build_security_group import region_id, make_security_group, add_security_group_rule
from build_security_group import add_security_group_rule_prefix_list
from build_security_group import update_security_group_rule, update_security_group_rule_prefix_list
from build_security_group import remove_security_group_rule, remove_security_group_rule_prefix_list
from build_security_group import destroy_security_group, erase_security_group, get_SecurityGroupId
# path to your home folder /home/username
FPATH = os.environ.get('ENV_FPATH')#ENV_FPATH is a var in your environment variable file
sys.path.append(FPATH+'/maendeleolab_securityGroup')
sys.path.append(FPATH+'/maendeleolab_subnet')
sys.path.append(FPATH+'/maendeleolab_vpc')
sys.path.append(FPATH+'/maendeleolab_prefixList')
import build_security_group
import build_subnet
import build_vpc
import build_prefix_list as prefix

