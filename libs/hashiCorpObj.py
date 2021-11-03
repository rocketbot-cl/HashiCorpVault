import hvac

class HashiCorpObj:

    def __init__(self, url, token, namespace):
        self.url = url
        self.token = token
        self.namespace = namespace
        
        self.client = hvac.Client(
            url=self.url,
            token=self.token,
            namespace=self.namespace
        )
        

    def read_secret(self, path, mount_point="secrets"):
        secret = self.client.secrets.kv.v1.read_secret(path=path, mount_point=mount_point)
        return secret

    def create_or_update_secret(self, path, secret, mount_point):
        secret = self.client.secrets.kv.v1.create_or_update_secret(path=path, secret=secret, mount_point=mount_point)
        if secret.status_code == 204:
            return True
        else:
            return secret.text
    
    def delete_secret(self, path, mount_point):
        secret = self.client.secrets.kv.v1.delete_secret(path=path, mount_point=mount_point)
        if secret.status_code == 204:
            return True
        else:
            return secret.text
