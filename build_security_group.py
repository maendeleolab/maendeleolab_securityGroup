#!/usr/bin/python3

Goal = '''
to create security groups in aws
Author: Pat@Maendeleolab
'''

#Module imports
import logging, sys, os, json
from datetime import datetime
from time import sleep

#Path to local home and user folder
FPATH = os.environ.get('ENV_FPATH')

#logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p ',\
            filename=FPATH+'/maendeleolab_securityGroup/security_group.log', level=logging.INFO)

#adding flexibility for regions
def region_id(name='us-east-1'):
		return name # e.g: 'us-east-1'

#create resource
def make_security_group(**kwargs):
	try:
		os.system("aws ec2 create-security-group \
			--description " + kwargs['Description'] + "\
			--tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value=" + kwargs['Security_group_name'] + "},\
								  {Key=" + kwargs['Tag_key'] + ",Value=" + kwargs['Tag_value'] + "}]'\
			--group-name " + kwargs['Group_name'] + "\
			--vpc-id " + kwargs['Vpc_Id'] + "\
			--region " + kwargs['Region'] 
		)
		logging.info(f'Created Security Group:{kwargs["Security_group_name"]} in {kwargs["Region"]}...')
		print(f'Created Security Group:{kwargs["Security_group_name"]} in {kwargs["Region"]}...')
	except Exception as err:
		logging.info(err)
		print(f'Logging "make_security_group" in security-group.log...')

def add_security_group_rule(**kwargs):
	try:
		os.system("aws ec2 authorize-security-group-ingress \
			--region " + kwargs['Region'] + " \
			--group-id " + kwargs['Security_group_id'] + "\
		--ip-permissions \
		IpProtocol=" + kwargs['Ip_protocol'] + ",FromPort=" + kwargs['From_port'] + ",ToPort=" + kwargs['To_port'] + ",IpRanges='[{CidrIp=" + kwargs['IP_range'] + "}]' "
		)
		logging.info(f'Created Security Group:{kwargs["Security_group_name"]} in {kwargs["Region"]}...')
	except Exception as err:
		logging.info(err)
		print(f'Logging "add_security_group_rule" in security-group.log...')

def add_security_group_rule_prefix_list(**kwargs):
	try:
		os.system("aws ec2 authorize-security-group-ingress \
			--region " + kwargs['Region'] + " \
			--group-id " + kwargs['Security_group_id'] + "\
		--ip-permissions \
		IpProtocol=" + kwargs['Ip_protocol'] + ",FromPort=" + kwargs['From_port'] + ",ToPort=" + kwargs['To_port'] + ",PrefixListIds='[{PrefixListId=" + kwargs['Prefix_list_id'] + "}]' "
		)
		logging.info(f'Created Security Group:{kwargs["Security_group_name"]} in {kwargs["Region"]}...')
		print(f'Created Security Group:{kwargs["Security_group_name"]} in {kwargs["Region"]}...')
	except Exception as err:
		logging.info(err)
		print('Logging "add_security_group_rule_prefix_list" in security-group.log...')

def update_security_group_rule(**kwargs):
	try:
		os.system("aws ec2 update-security-group-rule-descriptions-ingress \
			--region " + kwargs['Region'] + " \
			--group-id " + kwargs['Security_group_id'] + "\
		--ip-permissions \
		IpProtocol=" + kwargs['Ip_protocol'] + ",FromPort=" + kwargs['From_port'] + ",ToPort=" + kwargs['To_port'] + ",IpRanges='[{CidrIp=" + kwargs['IP_range'] + ",Description=" + kwargs['Security_rule_description'] + "}]' "
		)
		logging.info('Created Security Group:{kwargs["Security_group_name"]} in {kwargs["Region"]}...')
		print('Created Security Group:{kwargs["Security_group_name"]} in {kwargs["Region"]}...')
	except Exception as err:
		logging.info(err)
		print('Logging "update_security_group_rule" in security-group.log...')

def update_security_group_rule_prefix_list(**kwargs):
	try:
		os.system("aws ec2 update-security-group-rule-descriptions-ingress \
			--region " + kwargs['Region'] + " \
			--group-id " + kwargs['Security_group_id'] + "\
		--ip-permissions \
		IpProtocol=" + kwargs['Ip_protocol'] + ",FromPort=" + kwargs['From_port'] + ",ToPort=" + kwargs['To_port'] + ",PrefixListIds='[{PrefixListId=" + kwargs['Prefix_list_id'] + ",Description=" + kwargs['Security_rule_description'] + "}]' "
		)
		logging.info(f'Created Security Group:{kwargs["Security_group_name"]} in {kwargs["Region"]}...')
	except Exception as err:
		logging.info(err)
		print('Logging "update_security_group_rule_prefix_list" in security-group.log...')

def remove_security_group_rule(**kwargs):
	try:
		os.system("aws ec2 revoke-security-group-ingress \
			--region " + kwargs['Region'] + " \
			--group-id " + kwargs['Security_group_id'] + "\
		--ip-permissions \
		IpProtocol=" + kwargs['Ip_protocol'] + ",FromPort=" + kwargs['From_port'] + ",ToPort=" + kwargs['To_port'] + ",IpRanges='[{CidrIp=" + kwargs['IP_range'] + "}]' "
		)
		logging.info(f'Created Security Group:{kwargs["Security_group_name"]} in {kwargs["Region"]}...')
		print(f'Created Security Group:{kwargs["Security_group_name"]} in {kwargs["Region"]}...')
	except Exception as err:
		logging.info(err)
		print('Logging "remove_security_group_rule" in security-group.log...')

def remove_security_group_rule_prefix_list(**kwargs):
	try:
		os.system("aws ec2 revoke-security-group-ingress \
			--region " + kwargs['Region'] + " \
			--group-id " + kwargs['Security_group_id'] + "\
		--ip-permissions \
		IpProtocol=" + kwargs['Ip_protocol'] + ",FromPort=" + kwargs['From_port'] + ",ToPort=" + kwargs['To_port'] + ",PrefixListIds='[{PrefixListId=" + kwargs['Prefix_list_id'] + "}]' "
		)
		logging.info(f'Created Security Group:{kwargs["Security_group_name"]} in {kwargs["Region"]}...')
		print(f'Created Security Group:{kwargs["Security_group_name"]} in {kwargs["Region"]}...')
	except Exception as err:
		logging.info(err)
		print('Logging "remove_security_group_rule_prefix_list" in security-group.log...')

def get_SecurityGroupId(security_group_name, region='us-east-1'):
	try:
		''' Gets resource id from json output and can be used in deploy scripts '''
		output = os.popen('aws ec2 describe-security-groups --filters Name=tag:Name,Values=' + security_group_name + ' --region '+ region).read()
		security_data = json.loads(str(output))
		data = security_data["SecurityGroups"]#["GroupId"]
		for item in data:
			return item["GroupId"]
	except Exception as err:
		logging.info(err)
		print('Logging "get_SecurityGroupId" in security-group.log...')

def destroy_security_group(security_group_id, region='us-east-1'):
	try:
		os.system("aws ec2 delete-security-group --group-id " + security_group_id + " --region " + region)
		logging.info(f'Deleted Security Group Id:{security_group_id} in region: {region}...')
		print(f'Deleted Security Group Id:{security_group_id} in region: {region}...')
	except Exception as err:
		print('Logging destroy_security_group in security-group.log...')
		logging.info(err)

def erase_security_group(region='us-east-1'):
	try:
		''' Deletes all security groups that do not have any dependencies '''
		output = os.popen('aws ec2 describe-security-groups  --region ' + region).read()
		security_group_data = json.loads(str(output))
		for data in security_group_data['SecurityGroups']:
			destroy_security_group(data['GroupId'], region=region)
			logging.info(f'Delete: {data["GroupId"]} in region: {region}...')
			print(f'Delete: {data["GroupId"]} in region: {region}...')
	
		new_data = json.dumps(data, indent=2)
		print(new_data)
	except Exception as err:
		logging.info(err)
		print('Logging error to security-group.log...')

# ---------------------------------------- End -----------------------------------------------------

