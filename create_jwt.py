import time
from cryptography.hazmat.backends.openssl.backend import backend
from cryptography.hazmat.primitives import serialization
import jwt
def read_private_key(filepath, password=None):
    """
    This function will return private key value from the 
    path specified by user
    :param filepath : The path of file containing private key 
    :param password : Password to open private key file 
    :return : The value of private key     
    """
    if password:
        password = password.encode()
    with open(filepath, "rb") as file:
        private_key = serialization.load_pem_private_key(
        file.read(), password=password, backend=backend)
    return private_key

def generate_jwt(client_id, user_id, audience, privatekey_filepath):
    """
    This function will return the JWT token 
    :param client_id : Client id associate with salesforce account
    :param user_id : User id of salesforce account
    :param audience : Url on which salesforce is hosted
    :param privatekey_filepath : path of file where private key is stored
    :return : It wil return jwt token
    """
    try:
        private_key = read_private_key(privatekey_filepath)
        token_expiry = int(time.time()) + (60 * 5)
        header = {"alg": "RS256"}
        payload = {"iss": client_id, "sub": user_id, "aud": audience,
                   "exp": token_expiry}
        salesforce_jwt = jwt.encode(payload, private_key, headers=header,
                                    algorithm='RS256')
        return salesforce_jwt
    except Exception as e:
        raise Exception("Unable to generate JWT", e)


generate_jwt("3MVG9FG3dvS828gK1T0ZTkOIuxTYUhLVp7z47BAIlcfPgPOkSGeDUWBcCwvIN3WNLBWXJLALR235wV9c9JIFX","sparandkar@tripwire.com","https://test.salesforce.com", "/home/AD/sparandkar/CMA_Automation_Salesforce/te-cloud-management-assessor-tests/files/private.pem")

