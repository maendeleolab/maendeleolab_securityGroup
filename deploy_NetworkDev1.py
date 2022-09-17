#!/usr/bin/env python3

from maendeleolab_lib import *

maendeleolab_infra = [
        'us-east-1', 
        'us-west-2',
        ]

#Creates a security group, 
#then adds rule with a prefix list reference, 
#finally updates rule with a description
for region in maendeleolab_infra:
    #Security group number 1
    Security_name ="NetworkDev1_Public" #Security group name
    Security_prefix_list ="NetworkDev2_Public" #Prefix list name
    VPC_name ="NetworkDev1" #VPC name
    #creates security group
    make_security_group(
    Description=Security_name,
    Security_group_name=Security_name,
    Tag_key="Type",
    Tag_value="not-billable",
    Group_name=Security_name,
    Vpc_Id=build_vpc.get_VpcId(VPC_name, region),
    Region=region
    )
    #Rule number 1
    #adds more rules to the security group using prefix lists
    add_security_group_rule_prefix_list(
    Security_group_id=get_SecurityGroupId(Security_name, region),
    Security_group_name=Security_name,
    Ip_protocol="icmp", 
    From_port="-1",
    To_port="-1",
    Prefix_list_id=prefix.get_prefix_list_id(Security_prefix_list, region),
    Tag_key="Type",
    Tag_value="not-billable",
    Group_name=Security_name,
    Vpc_Id=build_vpc.get_VpcId(VPC_name, region),
    Region=region
    )
    #updates descriptions 
    update_security_group_rule_prefix_list(
    Security_group_id=get_SecurityGroupId(Security_name, region),
    Security_group_name=Security_name,
    Ip_protocol="icmp", 
    From_port="-1",
    To_port="-1",
    Security_rule_description='Allow ping',
    Prefix_list_id=prefix.get_prefix_list_id(Security_prefix_list, region),
    Tag_key="Type",
    Tag_value="not-billable",
    Group_name=Security_name,
    Vpc_Id=build_vpc.get_VpcId(VPC_name, region),
    Region=region
    )
    #Rule number 2
    Security_prefix_list ="SSH_From_Public" #Prefix list name 
    #adds more rules to the security group using prefix lists
    add_security_group_rule_prefix_list(
    Security_group_id=get_SecurityGroupId(Security_name, region),
    Security_group_name=Security_name,
    Ip_protocol="tcp", 
    From_port="22",
    To_port="22",
    Prefix_list_id=prefix.get_prefix_list_id(Security_prefix_list, region),
    Tag_key="Type",
    Tag_value="not-billable",
    Group_name=Security_name,
    Vpc_Id=build_vpc.get_VpcId(VPC_name, region),
    Region=region
    )
    #updates descriptions 
    update_security_group_rule_prefix_list(
    Security_group_id=get_SecurityGroupId(Security_name, region),
    Security_group_name=Security_name,
    Ip_protocol="tcp", 
    From_port="22",
    To_port="22",
    Security_rule_description='Allow ssh',
    Prefix_list_id=prefix.get_prefix_list_id(Security_prefix_list, region),
    Tag_key="Type",
    Tag_value="not-billable",
    Group_name=Security_name,
    Vpc_Id=build_vpc.get_VpcId(VPC_name, region),
    Region=region
    )
    
    #Security group number 2
    Security_name ="NetworkDev1_Private" #Security group name
    Security_prefix_list ="rfc_1918" #Prefix list name
    VPC_name ="NetworkDev1" #VPC name
    #creates security group
    make_security_group(
    Description=Security_name,
    Security_group_name=Security_name,
    Tag_key="Type",
    Tag_value="not-billable",
    Group_name=Security_name,
    Vpc_Id=build_vpc.get_VpcId(VPC_name, region),
    Region=region
    )
    #Rule number 1
    #adds more rules to the security group using prefix lists
    add_security_group_rule_prefix_list(
    Security_group_id=get_SecurityGroupId(Security_name, region),
    Security_group_name=Security_name,
    Ip_protocol="icmp", 
    From_port="-1",
    To_port="-1",
    Prefix_list_id=prefix.get_prefix_list_id(Security_prefix_list, region),
    Tag_key="Type",
    Tag_value="not-billable",
    Group_name=Security_name,
    Vpc_Id=build_vpc.get_VpcId(VPC_name, region),
    Region=region
    )
    #updates descriptions 
    update_security_group_rule_prefix_list(
    Security_group_id=get_SecurityGroupId(Security_name, region),
    Security_group_name=Security_name,
    Ip_protocol="icmp", 
    From_port="-1",
    To_port="-1",
    Security_rule_description='Allow ping',
    Prefix_list_id=prefix.get_prefix_list_id(Security_prefix_list, region),
    Tag_key="Type",
    Tag_value="not-billable",
    Group_name=Security_name,
    Vpc_Id=build_vpc.get_VpcId(VPC_name, region),
    Region=region
    )
    #Rule number 2
    #adds more rules to the security group using prefix lists
    add_security_group_rule_prefix_list(
    Security_group_id=get_SecurityGroupId(Security_name, region),
    Security_group_name=Security_name,
    Ip_protocol="tcp", 
    From_port="0",
    To_port="65535",
    Prefix_list_id=prefix.get_prefix_list_id(Security_prefix_list, region),
    Tag_key="Type",
    Tag_value="not-billable",
    Group_name=Security_name,
    Vpc_Id=build_vpc.get_VpcId(VPC_name, region),
    Region=region
    )
    #updates descriptions 
    update_security_group_rule_prefix_list(
    Security_group_id=get_SecurityGroupId(Security_name, region),
    Security_group_name=Security_name,
    Ip_protocol="tcp", 
    From_port="0",
    To_port="65535",
    Security_rule_description='Allow All TCP',
    Prefix_list_id=prefix.get_prefix_list_id(Security_prefix_list, region),
    Tag_key="Type",
    Tag_value="not-billable",
    Group_name=Security_name,
    Vpc_Id=build_vpc.get_VpcId(VPC_name, region),
    Region=region
    )

# ---------------------------------- End ----------------------------------
