import requests
import json

# Takes a Python dictionary, and stores the dictionary (as JSON) on IPFS. Return the Content Identifier (CID) of the data stored.
def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	
	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
	
	headers = {
		"Content-Type": "application/json",
		"pinata_api_key": '32da54258de0a42b7ee8',
		"pinata_secret_api_key": '677a570558e7bfa28cfa68f9d0cd1d837946a0ff317cce8873eea2d73719f909'
	}

	response = requests.post(url, json={"pinataContent":data}, headers=headers)

	if response.status_code == 200:
		cid = response.json()['IpfsHash']
	else:
		raise Exception(f"Error pin_to_ipfs: {response.text}")
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE    
	IPFS_GATEWAY = f"https://gateway.pinata.cloud/ipfs/{cid}"
	
	response = requests.get(IPFS_GATEWAY)

	if response.status_code == 200:
		data = response.json()
	else:
		raise Exception(f"Error get_from_ipfs: {response.text}")

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data

